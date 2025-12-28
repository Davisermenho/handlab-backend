# Guia de Configuração e Políticas Operacionais (V1.1.1)
Este guia operacional consolida configurações de Banco, Backend e Front-end para implementar o sistema integralmente conforme o RAG do arquivo REGRAS_SISTEMAS.md (V1.1), adicionando práticas, checklists e testes. É o documento de referência para “não deixar nada solto”.

Premissas
- RAG canônico: REGRAS_SISTEMAS.md (V1.1), incluindo a atualização 5.3.1 (obrigatoriedades do front).
- SGBD: Neon PostgreSQL 17 com pgcrypto (gen_random_uuid()).
- Paradigma: Nada acontece fora de vínculo; nada relevante é apagado; histórico imutável com auditoria.
- Escopo V1: clube único; temporadas derivadas por data; atleta com participações sazonais; staff exclusivo.

Sumário
1. Arquitetura e princípios
2. Banco de Dados (DDL, índices, triggers, seed, saúde)
3. Backend (API, regras, auditoria, segurança, erros)
4. Front-end (UI/UX, validações, comportamentos)
5. DevOps (ambiente, migrações, observabilidade, backup)
6. Matriz de conformidade RAG (onde cada regra é aplicada)
7. Fluxo de provisionamento e operação
8. Checklists por camada
9. Testes automatizados essenciais
10. Anexos (glossário, modelos de payload, mensagens de erro)

1) Arquitetura e princípios
- Camadas:
  - DB: integridade estrutural via PK/FK, índices, CHECKs, triggers, auditoria append-only e soft delete.
  - Backend: validações, derivação sazonal, gating operacional, auditoria, endpoints e fluxos.
  - Front-end: experiência guiada, campos obrigatórios/condicionais, alertas, rascunhos, restrições de goleira.
- Princípios aplicados:
  - Vínculos e exclusividade (R6–R9, RDB9–RDB10).
  - Auditoria imutável de ações críticas (R31–R32, RDB5).
  - Categoria por temporada, não global (RD1–RD2).
  - Provisionamento sem bloqueio: criar vínculos mínimos automaticamente (Seção 3 do RAG).

2) Banco de Dados
2.1 DDL mínimo (domínio principal)
- Tabelas de domínio com PK UUID: users, persons, memberships, teams, team_registrations, games, trainings, convocations, athlete_states, audit_logs, athletes, athlete_photos.
- Lookups com PK integer (allowlist): roles, categories, defensive_positions, offensive_positions, schooling_levels, permissions, role_permissions.
- Campos chave:
  - Temporal: timestamptz (UTC) (RDB3).
  - Soft delete: deleted_at + deleted_reason (exceto allowlist RDB4.1).
  - Auditoria: audit_logs append-only (RDB5) com actor_id, action, timestamp, context, old/new.

2.2 Índices e constraints
- Unicidade:
  - users.email: UNIQUE lower(email).
  - athletes.email: UNIQUE parcial lower(email) WHERE email IS NOT NULL.
  - athletes.rg, athletes.cpf: UNIQUE sobre versão normalizada (sem máscara).
- CHECKs e FKs:
  - shirt_number BETWEEN 1 AND 99.
  - FKs para posições defensivas/ofensivas, escolaridade e categorias.
  - Regra de goleira (RD13): se main_defensive_position_id = 5 então main_offensive_position_id IS NULL (CHECK + validação backend).
- Exclusividade de vínculos:
  - memberships: índices parciais para 1 vínculo ativo por pessoa (staff) e 1 vínculo ativo por pessoa+temporada (atleta).
  - team_registrations: períodos não sobrepostos por pessoa+equipe+temporada; novas linhas para reativação (RDB10).
- Jogos e treinos:
  - TRG_games_block_update_finalized: bloqueia UPDATE em status=finalizado; exceção exclusivamente para finalizado -> em_revisao via ação auditada (6.1.2).
  - Treinos >24h exigem admin_note (RDB13).

2.3 Triggers essenciais
- updated_at BEFORE UPDATE (tabelas de domínio).
- athlete_age_at_registration ON INSERT/UPDATE (quando registered_at/birth_date mudam).
- audit_logs: bloqueio de UPDATE/DELETE (append-only).
- games: bloqueio de UPDATE quando finalizado; reabertura auditada.

2.4 Seed mínimo (RDB14)
- Criar: organização/clube único, roles, superadmin (users.is_superadmin = true), uma temporada (start_date/end_date), categorias globais, equipe institucional.
- Verificações:
  - Temporada ativa ou planejada futura.
  - Equipe Institucional existente (para provisionamento de atletas sem equipe competitiva).

2.5 Saúde e manutenção
- Health checks SQL:
  - Vínculos sem temporada: SELECT de memberships WHERE season_id IS NULL → deve retornar vazio.
  - Atletas sem team_registration na temporada: SELECT de atletas ativos sem participação vigente na temporada → apenas permitido se em Equipe Institucional.
  - Jogos finalizados com UPDATE posterior: consulta audit_logs “game_reopen” e diffs subsequentes.
- Particionamento/retention lógico:
  - Particionar audit_logs por temporada/ano; nunca deletar, apenas arquivar.

3) Backend (API)
3.1 Autenticação e segurança
- Login: email normalizado + senha (8+ caracteres, política configurável).
- Autorização por papel + vínculo sazonal ativo (R3, R6–R9).
- Padrão JWT com escopos por papel e equipe (RF7, R26).
- Rate limiting e auditoria: todas as ações críticas registradas (R31–R32).

3.2 Endpoints obrigatórios
- POST /users
  - Cria usuário (staff/atleta) + associa ao clube (R34) + membership sazonal. Para atleta, cria team_registration na Equipe Institucional (Seção 3 do RAG).
  - Eventos: user_create, membership_create, team_registration_create, user_provision_auto_link.
  - Erros:
    - Sem temporada ativa/planejada: 409 + hint “criar temporada seed” (Seção 8 do RAG).
    - Sem equipe institucional: 409 + hint “criar Equipe Institucional”.
- POST /teams/{team_id}/registrations
  - Move atleta entre equipes: encerra participação vigente (team_registration_close), cria nova (team_registration_create); sem sobreposição (RDB10).
- POST /teams/{team_id}/set-coach
  - Define treinador responsável; auditoria role_change (RF7).
- GET /athletes/{id}
  - Retorna foto URL, idade atual (derivada), categoria por temporada (derivada) e pendências operacionais.
- Jogos e treinos:
  - POST /games, PATCH /games/{id}/finalize, PATCH /games/{id}/reopen (admin), DELETE lógico /games/{id}.
  - POST /trainings, PATCH /trainings/{id} (janela R40/R27), com admin_note após 24h.
- Estatísticas e correções:
  - POST /stats, PATCH /stats/{id} com admin_note (R23–R24, RDB12).

3.3 Validações e gating
- Cadastro:
  - Staff: name, email(login), password obrigatórios.
  - Atleta: conforme 5.3.1 atualização de obrigatoriedades (name≥3, birth_date, RG, CPF, phone, defensiva obrigatória; ofensiva condicional à não-goleira).
- Operar em equipe (Seção 7 do RAG):
  - Atleta: RG/CPF/defensiva válidos; team_registration vigente na equipe competitiva; RD13 aplicado.
  - Treinador: definido como responsável (RF7).
- Goleira (RD13):
  - Bloquear offensive_position na goleira e tempo/estatísticas de linha; goleiro-linha (RD22) só para atletas de linha.
- Convocação:
  - Validar limite 16 atletas (RD18) ao salvar convocação.
  - Bloquear participação sem convocação (RP3).
- Temporada:
  - Estados derivados (6.1.1); reabertura de jogo conforme RF15 e 6.1.2 (ver “feature flag” abaixo).

3.4 Auditoria
- Ações mínimas (Seção 9 do RAG): user_create, membership_create, team_registration_create/close, role_change/membership_reactivate, athlete_state_change, game_finalize/reopen/soft_delete, stat_correction.
- Contexto: actor_id, entity_id, payload diffs old/new, timestamps UTC, motivo (admin_note quando exigido).

3.5 Erros e mensagens
- Padrões de resposta:
  - 400: validação de campos (detalhar campo e regra violada).
  - 401/403: autenticação/escopo insuficiente.
  - 409: conflito de regras do RAG (ex.: sobreposição temporal, limite de 16, sem temporada/equipe institucional).
  - 422: integridade estrutural (RF20).
- Mensagens devem referenciar regra quando aplicável (ex.: “Violação RD13: goleira não pode receber posição ofensiva”).

3.6 Configurações opcionais (feature flags)
- ALLOW_DIRIGENTE_REABRIR_JOGO=true|false
  - true: Coordenador e Dirigente podem reabrir (seguir 6.1.2).
  - false: somente Coordenador (seguir RF15).
- MEMBERSHIP_SEM_TEMPORADA_ATIVA
  - future: criar membership com start_at na virada da próxima planejada (Seção 8).
  - block: bloquear cadastro e solicitar temporada seed.

4) Front-end (UI/UX)
4.1 Ficha de cadastro da atleta
- Obrigatórios: athlete_name≥3, birth_date, athlete_rg, athlete_cpf, athlete_phone, main_defensive_position_id.
- Condicional: main_offensive_position_id obrigatório apenas se defensiva ≠ goleira.
- Opcionais: nickname, shirt_number(1–99), secondary positions, athlete_email (opcional, único quando preenchido), guardian_name/phone, schooling_id, foto até 5MB, endereço estruturado (CEP → autopreenchimento; tudo opcional).
- Somente leitura: athlete_age (derivado), category (derivada por temporada), athlete_photo_url (derivada após upload).
- Não pedir equipe no cadastro (provisionamento sem bloqueio).

4.2 Fichas de staff
- Obrigatórios: name, email(login), password.
- Não pedir equipe; operação depende de definição posterior de responsabilidade (RF7).

4.3 Comportamentos essenciais
- RD13: ocultar/invalidar campo ofensivo se defensiva=goleira; bloquear inputs de tempo/estatísticas de linha para goleira.
- Pendências operacionais pós-cadastro: banner “mover para equipe competitiva”, “definir treinador responsável”.
- Notificações críticas (RF24) bloqueiam ação até confirmação.
- Offline (RF25): sincronizar eventos preservando ordem temporal; resolver conflitos (R41).

5) DevOps
5.1 Variáveis de ambiente
- DB_DSN, DB_SCHEMA_VERSION, JWT_SECRET, RATE_LIMITS, FEATURE_FLAGS (ALLOW_DIRIGENTE_REABRIR_JOGO, MEMBERSHIP_SEM_TEMPORADA_ATIVA).
- STORAGE: escolha entre BYTEA (MVP) ou objeto (S3) para fotos; limite 5MB; whitelist de MIME.

5.2 Migrações e seed
- Processo:
  - Executar migrações DDL (PK/FK/índices/CHECKs/triggers).
  - Rodar seed mínimo (org, roles, superadmin, temporada, equipe institucional, categories).
- Health gates pós-deploy:
  - Verificar temporada ativa/planejada.
  - Verificar equipe institucional.
  - Verificar índices únicos (email, RG, CPF).

5.3 Observabilidade
- Logs de auditoria (append-only) + logs de aplicação; correlação por actor_id e ação.
- Métricas:
  - Taxa de falhas de validação (400) por endpoint.
  - Conflitos (409) por regra (RD/ RF/ RDB).
  - Latência de sincronização offline (RF25).
  - Contagem de reaberturas de jogos (RF15/6.1.2).

5.4 Backup e retenção
- Backups periódicos do banco; partição de audit_logs por temporada; nunca deletar, apenas arquivar.
- Teste de restore trimestral.

6) Matriz de conformidade RAG (resumo aplicado)
- DB: R4, R20, R29, R35; RDB1–RDB14 (estrutura, auditoria, triggers, seed).
- Backend: R1–R3, R5–R8, R10–R13, R15–R17, R19, R23–R25, R28, R30–R34, R37–R39; RF5, RF21, RF31; RD1–RD3, RD5, RD7–RD10, RD14–RD15, RD18, RD20, RD27, RD30, RD33–RD34, RD38, RD40, RD42, RD49–RD52, RD53–RD54, RD58, RD60–RD61, RD63–RD64, RD66–RD72, RD74, RD76, RD79, RD86–RD88, RD90–RD91; RP1–RP2, RP4–RP6, RP9, RP13, RP15, RP19–RP20.
- Backend+Front: R9, R14, R18, R40–R42; RF1–RF4, RF6–RF30; RD4, RD6, RD11–RD13, RD16–RD17, RD19, RD21–RD26, RD28–RD29, RD31–RD32, RD35–RD37, RD39, RD41, RD43–RD48, RD55–RD57, RD59, RD62, RD65, RD73, RD75, RD77–RD80, RD81–RD85, RD89; RP3, RP7–RP8, RP10–RP12, RP14, RP16–RP18.
- Front: 5.3.1 (obrigatoriedades e comportamentos).

7) Fluxo de provisionamento e operação (sequência recomendada)
- Seed: criar clube único, categorias, superadmin, temporada, equipe institucional.
- Configurar feature flags (reabertura e membership sem temporada).
- Cadastro:
  - Dirigente → Coordenador → Treinador → Atleta (RF1).
  - Backend cria vínculos mínimos automaticamente; atleta entra na Equipe Institucional (Seção 3).
- Vinculação posterior:
  - Atleta: mover para equipe competitiva (encerra institucional; cria nova linha) (RDB10).
  - Treinador: definir responsável da equipe (RF7).
- Operação sazonal:
  - Criar jogos/treinos; validar convocação, limite de 16; finalizar jogo; reabrir quando necessário via ação administrativa auditada.
  - Correções com admin_note; dashboards só refletem dados validados (RF29, RD85).

8) Checklists por camada
8.1 DB
- [ ] pgcrypto habilitado; PKs UUID nas tabelas de domínio.
- [ ] Índices únicos: lower(users.email), lower(athletes.email) parcial, RG/CPF normalizados.
- [ ] CHECKs: shirt_number; goleira sem ofensiva; UF ‘AA’.
- [ ] Triggers: updated_at; age_at_registration; audit_logs append-only; games bloqueio finalizado.
- [ ] Seed: clube, roles, superadmin, temporada, equipe institucional, categories.

8.2 Backend
- [ ] Endpoints obrigatórios criados com validações e auditoria.
- [ ] Derivação de categoria por temporada no GET; não persistir no perfil global.
- [ ] Gating operacional (Seção 7 do RAG) implementado.
- [ ] Feature flags aplicadas para RF15/6.1.2 e membership sem temporada.
- [ ] Erros com referência de regra (ex.: “Violação RP3”).

8.3 Front-end
- [ ] Ficha atleta obedecendo 5.3.1 (obrigatórios/condicionais/opcionais/somente leitura).
- [ ] RD13 aplicado: ocultar ofensiva na goleira; bloquear estatísticas de linha.
- [ ] Não pedir equipe no cadastro; exibir pendências.
- [ ] Notificações críticas (RF24); offline (RF25); resolução de conflitos (R41).

9) Testes automatizados essenciais
- Provisionamento
  - [ ] POST /users (atleta) sem equipe → cria membership + team_registration institucional + auditoria.
  - [ ] Sem temporada ativa: comportamento conforme flag (future vs block).
  - [ ] Sem equipe institucional: 409 com mensagem específica.
- Movimentação
  - [ ] Encerrar e criar team_registration sem sobreposição; estatísticas preservadas (RD87).
- Goleira
  - [ ] Defensiva=Goleira → ofensiva NULL; lançar tempo/estatísticas de linha → bloquear.
- Jogos
  - [ ] Finalizar → bloqueio de UPDATE; reabrir via endpoint autorizado → em_revisao; nova finalização reativa bloqueio.
  - [ ] Convocação >16 → bloquear; participação sem convocação → bloquear.
- Disciplina
  - [ ] Suspensa: flag “Atleta Irregular”; estatísticas contam normalmente (RD16).
- Conflitos
  - [ ] Edição simultânea → registrar conflito e exigir decisão (R41).

10) Anexos
10.1 Glossário resumido
- Membership: vínculo pessoa+papel+clube+temporada.
- Team registration: participação temporal da atleta em uma equipe por temporada.
- Estados de atleta: ativa, lesionada, dispensada.
- Rascunho: registro sem efeito operacional/analítico; visível à comissão.

10.2 Exemplos de payload (resumo)
- Cadastro atleta (POST /users):
```json
{
  "role": "athlete",
  "athlete_name": "Fulana Exemplo",
  "birth_date": "2010-05-12",
  "athlete_rg": "12.345.678-9",
  "athlete_cpf": "123.456.789-09",
  "athlete_phone": "+55 11 91234-5678",
  "main_defensive_position_id": 3,
  "main_offensive_position_id": 4,
  "athlete_email": "fulana@example.com",
  "zip_code": "01001-000"
}
```
- Movimentar atleta (POST /teams/{team_id}/registrations):
```json
{
  "athlete_id": "uuid",
  "season_id": "uuid",
  "start_at": "2025-01-10T12:45:00Z"
}
```

Notas finais
- Este guia complementa e operacionaliza o RAG. Em qualquer dúvida, a regra esportiva prevalece sobre a operacional (RF31) e a integridade sobre a usabilidade (RF21).

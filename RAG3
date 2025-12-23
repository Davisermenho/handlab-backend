Aqui está a ordem de prompts para iniciar e concluir a Fase 3 — Definição do contrato da API, com instruções práticas para usar no Copilot/Codex no VS Code:

1) hl-brief — Briefing inicial do agente
- Objetivo: fixar como contexto os arquivos docs/fluxo-backend-oficial_Version12 (1).md e docs/regras-sistema-v1.1_Version2.md, alinhar outputs esperados e evitar ambiguidade.
- Como usar:
  - No editor, insira o snippet “hl-brief” (prefixo → Tab).
  - Preencha a fase com “FASE 3 — Definição do contrato da API”.
  - No Copilot Chat, anexe os dois arquivos como contexto (Add context ou @workspace citando os caminhos) e cole o briefing.
  - Solicite confirmação de entendimento e exija que o agente liste os outputs que irá gerar (arquivos, funções, testes, OpenAPI).
- O que o agente deve prometer entregar:
  - OpenAPI rascunho para o(s) recurso(s) de interesse.
  - Esqueleto de routers FastAPI com docstrings citando regras (IDs R/RF/RD/RP).
  - Mapeamento de erros conforme “Contrato de erros por regra”.

2) hl-phase3 — FASE 3: Contrato da API (endpoints + erros)
- Objetivo: definir o contrato do recurso e esqueleto de rotas com paginação/filtros/ordenação e códigos de erro mapeados às regras.
- Como usar:
  - No editor, insira “hl-phase3” (prefixo → Tab), substitua o placeholder pelo recurso alvo (ex.: Athlete, Team, Game) e cole no Copilot Chat.
  - Exija que o agente:
    - Versione todos os endpoints sob /v1.
    - Inclua paginação padrão (page/limit ou cursor), ordenação e filtros coerentes com o domínio.
    - Mapeie respostas de erro usando o “Contrato de erros por regra” (ex.: 409_conflict_membership_active, 409_edit_finalized_game, 422_age_category_violation).
    - Anote em cada endpoint as Regras aplicáveis (IDs R/RF/RD/RP) nas docstrings.
    - Entregue:
      - Um arquivo OpenAPI (openapi.yaml ou openapi.json) com os endpoints, parâmetros, schemas e responses.
      - Esqueleto de routers em app/api/v1/routers/<recurso>.py com Depends(get_db) e docstrings citando as regras e exemplos de erros.
- Dicas de verificação:
  - O OpenAPI deve conter: paths, métodos, parâmetros (query/path), schemas (request/response), responses (2xx/4xx com payloads padronizados).
  - Os erros precisam referenciar o “Contrato de erros por regra” e usar o schema ErrorResponse.
  - Os endpoints devem citar explicitamente regras relevantes (ex.: R16, RD13, RF15).


3) hl-validate-rules — Checklist de validação (Matriz + DoD da Fase 3)
- Objetivo: garantir que o contrato está alinhado à Matriz de enforcement, ao Contrato de erros e à Definition of Done da Fase 3.
- Como usar:
  - Insira “hl-validate-rules” e cole no Copilot Chat.
  - Peça que o agente:
    - Liste as regras aplicadas por endpoint com referências (arquivo/linha).
    - Enumere os erros potenciais por rota (código, status, payload).
    - Verifique se paginação/ordenção/filtros estão definidos e documentados no OpenAPI.
    - Indique como exportar o OpenAPI (ex.: gerar openapi.json via app.openapi()) e onde salvar.
- Aceite quando:
  - OpenAPI está completo e coerente com o domínio.
  - Erros estão mapeados às regras e usam o schema ErrorResponse.
  - As docstrings citam as regras e o OpenAPI inclui exemplos de responses de erro.

4) (Opcional) hl-pr — Template de PR (resumo técnico)
- Objetivo: preparar a descrição do PR para revisão do contrato.
- Como usar:
  - Insira “hl-pr”, preencha os placeholders e peça ao agente o texto do PR.
  - Inclua: Regras impactadas, erros adicionados, arquivos OpenAPI e routers gerados, observações técnicas.

Pré-condições antes de iniciar a Fase 3
- Fase 2 concluída ou, no mínimo, estrutura básica do app disponível (para gerar/validar OpenAPI).
- Fluxo e Regras anexados ao chat como contexto.

Critérios de aceitação (Definition of Done — Fase 3)
- OpenAPI revisado, versionado sob /v1 e aprovado.
- Convenções de erro, paginação e tipos de ID definidas e documentadas.
- Endpoints anotados com regras (IDs) e mapeamento de erros conforme “Contrato de erros por regra”.
- Esqueleto de routers gerado com docstrings citando regras e exemplos de respostas de erro.

{
  "Briefing inicial do agente (Copilot/Codex)": {
    "prefix": "hl-brief",
    "description": "Briefing para orientar Copilot/Codex a usar o fluxo e regras como fonte de verdade.",
    "body": [
      "Use exclusivamente docs/fluxo-backend-oficial.md e docs/regras-sistema-v1.1_Version2.md como fonte de verdade.",
      "- Siga a fase atual: ${1:FASE 2 — Núcleo do backend|FASE 3 — Definição do contrato|FASE 5 — CRUDs|FASE 6 — Endurecimento}.",
      "- Aplique a “Matriz de enforcement das regras”.",
      "- Use o “Contrato de erros por regra” nos responses HTTP.",
      "- Gere testes com nomes que citem as regras (ex.: test_RDB9_...).",
      "- Se algo não estiver especificado, faça 1 pergunta objetiva e aguarde.",
      "Antes de gerar código, confirme entendimento e liste os outputs esperados (arquivos, funções, testes)."
    ]
  },
  "Diagnóstico Alembic ↔ Neon (RESULTADOS)": {
    "prefix": "hl-diagnose",
    "description": "Solicita ao agente o diagnóstico não-destrutivo e devolução do bloco RESULTADOS.",
    "body": [
      "Rode o diagnóstico NÃO-DESTRUTIVO Alembic ↔ Neon conforme docs/fluxo-backend-oficial.md (FASE 1).",
      "- Não aplique alterações no banco.",
      "- Se possível, gere dry-run (alembic upgrade head --sql) e reporte linhas.",
      "Devolva exatamente neste formato:",
      "",
      "RESULTADOS",
      "repo_heads:",
      "- <hash_head_1> <mensagem>",
      "- <hash_head_2> <mensagem>  (se houver)",
      "",
      "db_current: <None|current head|hash_atual>",
      "",
      "has_alembic_version_table: <true|false>",
      "alembic_version_num: <hash_ou_vazio>",
      "",
      "last_3_migrations:",
      "- <arquivo_1.py>",
      "- <arquivo_2.py>",
      "- <arquivo_3.py>",
      "",
      "dry_run_generated: <yes|no>",
      "dry_run_file: <review.sql|n/a>",
      "dry_run_lines: <número_de_linhas_ou_n/a>"
    ]
  },
  "FASE 2 — Núcleo do backend (implementação)": {
    "prefix": "hl-phase2",
    "description": "Pede a implementação da FASE 2 com arquivos e garantias.",
    "body": [
      "Implemente a FASE 2 — Núcleo do backend conforme docs/fluxo-backend-oficial.md.",
      "Arquivos:",
      "- app/core/config.py",
      "- app/core/db.py",
      "- app/api/v1/routers/health.py",
      "- app/main.py",
      "- tests/conftest.py (fixture com isolamento transacional via savepoint).",
      "Requisitos:",
      "- Engine com pool_pre_ping e future=True.",
      "- get_db com commit/rollback e fechamento.",
      "- healthcheck_db executando SELECT 1.",
      "Entregue os arquivos, imports corretos e testes que validem o isolamento transacional e o /v1/health."
    ]
  },
  "FASE 3 — Contrato da API (endpoints + erros)": {
    "prefix": "hl-phase3",
    "description": "Define endpoints, paginação e contrato de erros mapeado às regras.",
    "body": [
      "Defina o contrato da API para o recurso ${1:<Recurso>} conforme FASE 3 em docs/fluxo-backend-oficial.md.",
      "Inclua:",
      "- Versionamento /v1.",
      "- Paginação padrão (page/limit ou cursor), ordenação e filtros.",
      "- Erros mapeados do “Contrato de erros por regra”.",
      "- Em cada endpoint, anote as Regras aplicáveis (IDs R/RF/RD/RP).",
      "Entregue um rascunho OpenAPI e esqueleto de routers com docstrings citando as regras e exemplos de respostas de erro."
    ]
  },
  "CRUD com RDB10 — TeamRegistration (sem sobreposição)": {
    "prefix": "hl-crud-rdb10",
    "description": "Gera CRUD completo aplicando RDB10 e retornos 409 para período sobreposto.",
    "body": [
      "Gerar CRUD completo de ${1:TeamRegistration} conforme FASE 5.",
      "Aplicar RDB10:",
      "- Períodos não sobrepostos para pessoa+equipe+temporada.",
      "- Reativação cria nova linha (novo UUID), sem reabrir anterior.",
      "Erros:",
      "- Em conflito de período, retornar 409 (cite RDB10) com payload do “Contrato de erros por regra”.",
      "Produzir:",
      "- Model SQLAlchemy, Schemas Pydantic, Service com fronteira transacional, Route com Depends(get_db).",
      "- Testes unitários e de integração: test_RDB10_periodos_sem_sobreposicao; garantir ausência de N+1; índices críticos.",
      "Citar as regras nas docstrings e nomes dos testes."
    ]
  },
  "Endurecimento — Jogos finalizados e reabertura (RF15/RDB13)": {
    "prefix": "hl-games-rf15",
    "description": "Implementa bloqueio de edição em jogos finalizados e fluxo de reabertura.",
    "body": [
      "Implemente RF15/RDB13 conforme docs/fluxo-backend-oficial.md:",
      "- Jogo finalizado é somente leitura (bloqueio de UPDATE).",
      "- Reabertura muda status para em_revisao e registra audit_log (acao=game_reopen).",
      "- Nova finalização reativa bloqueio e registra audit_log (acao=game_finalize).",
      "Handler global de exceções:",
      "- Mapear tentativa de edição em finalizado para 409_edit_finalized_game.",
      "Testes:",
      "- test_RF15_reabertura",
      "- test_RDB13_bloqueio_update_finalizado"
    ]
  },
  "Temporada interrompida (RF5.2)": {
    "prefix": "hl-season-rf52",
    "description": "Aplica bloqueios e cancelamentos automáticos após interrupted_at.",
    "body": [
      "Aplique RF5.2 (Temporada interrompida):",
      "- Bloquear criação/edição de novos eventos a partir de interrupted_at.",
      "- Cancelar automaticamente jogos futuros (status ‘cancelado’; manter histórico; sem novos dados operacionais).",
      "Erro:",
      "- 409_season_interrupted_locked conforme ‘Contrato de erros por regra’.",
      "Gerar testes de serviço e rota cobrindo cenários antes/depois de interrupted_at."
    ]
  },
  "Validação contra Matriz e Contrato de Erros": {
    "prefix": "hl-validate-rules",
    "description": "Checklist de validação das regras e erros após gerar código.",
    "body": [
      "Valide a solução contra:",
      "- Matriz de enforcement das regras (seção dedicada).",
      "- Contrato de erros por regra.",
      "- Definition of Done da fase em execução.",
      "Liste:",
      "- Quais regras foram aplicadas e onde (arquivo/linha).",
      "- Quais erros podem ocorrer por rota e seus payloads.",
      "- Quais testes cobrem cada regra e como executá-los."
    ]
  },
  "Migration com dry-run e checklist": {
    "prefix": "hl-migration",
    "description": "Solicita geração de migration, SQL de dry-run e checklist de segurança/rollback.",
    "body": [
      "Gere uma migration para ${1:descrição da mudança} usando Alembic.",
      "- Traga o SQL de dry-run (alembic upgrade head --sql) em review.sql (não aplicar no banco).",
      "- Forneça checklist:",
      "  1) Impacto em produção (DDL, locks, índices).",
      "  2) Plano de rollback (downgrade seguro ou scripts compensatórios).",
      "  3) Validação pós-migração (consultas e smoke tests).",
      "  4) Referência às Regras afetadas (IDs) e testes relacionados."
    ]
  },
  "Template de PR — Regras e migrações": {
    "prefix": "hl-pr",
    "description": "Resumo de PR com regras impactadas, erros adicionados e status de migrations.",
    "body": [
      "PR — Resumo",
      "Regras impactadas: ${1:RDB9, RF15}",
      "Validações/erros adicionados: ${2:409_conflict_membership_active}",
      "Migrations: ${3:sim|nao}",
      "Dry-run anexo: ${4:review.sql|n/a}",
      "Testes:",
      "- ${5:test_RDB9_exclusividade_vinculo_staff}",
      "- ${6:test_RF15_reabertura_bloqueia_dashboards}",
      "Observações:",
      "- ${7:Notas técnicas e riscos}"
    ]
  }
}



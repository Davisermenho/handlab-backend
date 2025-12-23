{
  "metadata": {
    "titulo": "FLUXO DE TRABALHO DO BACKEND (OFICIAL)",
    "formato_original": "markdown",
    "versao": "1.0.0",
    "gerado_em": "2025-12-23",
    "autor_login": "Davisermenho",
    "idioma": "pt-BR",
    "objetivo_documento": "Documento objetivo para orientar desenvolvimento assistido (Copilot/Codex) no VS Code. Estrutura padronizada, comandos, templates e critérios de pronto (Definition of Done) por fase."
  },
  "sumario": [
    { "titulo": "FASE 0 — Pré-condições do projeto (cumprida)", "anchor_id": "fase-0-pre-condicoes-do-projeto-cumprida" },
    { "titulo": "FASE 1 — Infraestrutura (diagnóstico Alembic ↔ Neon) — cumprida", "anchor_id": "fase-1-infraestrutura-diagnostico-alembic-neon-cumprida" },
    { "titulo": "Cenario: Neon já existente com tabelas (referência)", "anchor_id": "cenario-neon-ja-existente-com-tabelas-referencia", "subsecao_de": "FASE 1 — Infraestrutura (diagnóstico Alembic ↔ Neon) — cumprida" },
    { "titulo": "FASE 2 — Núcleo do backend", "anchor_id": "fase-2-nucleo-do-backend" },
    { "titulo": "FASE 3 — Definição do contrato da API", "anchor_id": "fase-3-definicao-do-contrato-da-api" },
    { "titulo": "FASE 4 — FastAPI mínimo", "anchor_id": "fase-4-fastapi-minimo" },
    { "titulo": "FASE 5 — CRUDs (execução)", "anchor_id": "fase-5-cruds-execucao" },
    { "titulo": "FASE 6 — Endurecimento", "anchor_id": "fase-6-endurecimento" },
    { "titulo": "FASE 7 — Produção (Go-Live)", "anchor_id": "fase-7-producao-go-live" },
    { "titulo": "FASE 8 — Produção-ready (Checklist)", "anchor_id": "fase-8-producao-ready-checklist" },
    { "titulo": "Matriz de enforcement das regras (resumo)", "anchor_id": "matriz-de-enforcement-das-regras-resumo" },
    { "titulo": "Contrato de erros por regra", "anchor_id": "contrato-de-erros-por-regra" },
    { "titulo": "Blueprints de DB (RDB)", "anchor_id": "blueprints-de-db-rdb" },
    { "titulo": "Convenções de referência às regras", "anchor_id": "convencoes-de-referencia-as-regras" },
    { "titulo": "Convenções e estrutura de pastas", "anchor_id": "convencoes-e-estrutura-de-pastas" },
    { "titulo": "Templates mínimos (copiar/colar)", "anchor_id": "templates-minimos-copiar-colar" },
    { "titulo": "Comandos (cheatsheet)", "anchor_id": "comandos-cheatsheet" },
    { "titulo": "Prompts prontos para Copilot/Codex", "anchor_id": "prompts-prontos-para-copilot-codex" },
    { "titulo": "Variáveis de ambiente (.env exemplo)", "anchor_id": "variaveis-de-ambiente-env-exemplo" },
    { "titulo": "CI/CD básico (esqueleto)", "anchor_id": "ci-cd-basico-esqueleto" },
    { "titulo": "Arquivos a ignorar (.gitignore sugerido)", "anchor_id": "arquivos-a-ignorar-gitignore-sugerido" },
    { "titulo": "Definition of Done por fase", "anchor_id": "definition-of-done-por-fase" },
    { "titulo": "Status final do backend", "anchor_id": "status-final-do-backend" }
  ],
  "fases": {
    "fase_0_pre_condicoes_projeto": {
      "titulo": "FASE 0 — Pré-condições do projeto (cumprida)",
      "anchor_id": "fase-0-pre-condicoes-do-projeto-cumprida",
      "objetivo": "Consolidar domínio e escopo do produto.",
      "tarefas": [
        "Entender o domínio.",
        "Listar entidades principais.",
        "Definir regras de negócio de alto nível."
      ],
      "entregaveis": [
        "Lista de recursos (ex.: persons, users, organizations).",
        "Regras do sistema disponíveis ao Codex/Copilot (arquivo de regras anexado).",
        "Nenhum código é produzido nesta fase."
      ],
      "status": "Cumprida"
    },
    "fase_1_infraestrutura": {
      "titulo": "FASE 1 — Infraestrutura (diagnóstico Alembic ↔ Neon) — cumprida",
      "anchor_id": "fase-1-infraestrutura-diagnostico-alembic-neon-cumprida",
      "objetivo": "Validar alinhamento entre migrations do repositório (Alembic) e o banco Neon, sem alterar o schema.",
      "diagnostico_executado": {
        "repo_head": "3e2898989f01",
        "db_current": "3e2898989f01",
        "has_alembic_version_table": true,
        "dry_run_gerado": {
          "arquivo": "review.sql",
          "linhas": 2278
        },
        "conclusao": "Banco alinhado ao HEAD. Nenhuma ação corretiva necessária. Prosseguir para a Fase 2."
      },
      "boas_praticas_consolidadas": [
        "Adicionar review.sql ao .gitignore.",
        "Segregar DATABASE_URL por ambiente.",
        "Manter tasks no VS Code para diagnóstico não-destrutivo."
      ],
      "cenario_referencia_neon_existente_com_tabelas": {
        "anchor_id": "cenario-neon-ja-existente-com-tabelas-referencia",
        "diagnostico_nao_destrutivo": [
          "Heads do repositório: alembic heads",
          "Revisão atual do banco: alembic current",
          "Verificar existência da tabela alembic_version (via psql ou SQLAlchemy).",
          "Listar as 3 migrations mais recentes (alembic/versions).",
          "Opcional: gerar dry-run de upgrade (alembic upgrade head --sql > review.sql) para revisão humana."
        ],
        "decisoes_por_cenario": [
          "Banco já no HEAD (db_current == repo_head): nenhuma ação.",
          "Banco não versionado (sem alembic_version), mas schema correto: alembic stamp <HEAD>.",
          "Banco atrás do HEAD: revisar dry-run e aplicar alembic upgrade head.",
          "Múltiplos HEADs no repo: alembic merge e depois seguir conforme estado do banco.",
          "Divergência real de schema: alembic revision --autogenerate (revisar), depois alembic upgrade head."
        ],
        "status": "Cumprida (com evidências acima). Seção mantida para referência."
      }
    },
    "fase_2_nucleo_backend": {
      "titulo": "FASE 2 — Núcleo do backend",
      "anchor_id": "fase-2-nucleo-do-backend",
      "momento": "Após o banco e migrations estarem funcionais.",
      "tarefas": [
        "Implementar config.py.",
        "Implementar database.py.",
        "Implementar get_db.",
        "Implementar db_context.",
        "Implementar get_db_with_context.",
        "Implementar autenticação simulada (mock).",
        "Implementar permissões simuladas (mock)."
      ],
      "entregaveis": [
        "Sessão de banco disponível.",
        "Contexto de execução definido.",
        "Identidade e permissões simuladas configuradas.",
        "FastAPI pode subir apenas para endpoints de health/debug se necessário."
      ]
    },
    "fase_3_definicao_contrato_api": {
      "titulo": "FASE 3 — Definição do contrato da API",
      "anchor_id": "fase-3-definicao-do-contrato-da-api",
      "momento": "Antes de qualquer CRUD.",
      "tarefas": [
        "Definir endpoints (URLs) com prefixo de versão (/v1).",
        "Definir métodos HTTP por operação.",
        "Definir estados de recurso (ex.: active, archived).",
        "Definir regras e códigos de erro (403, 404, 409, 422).",
        "Padronizar resposta de erro: { code, message, details? }.",
        "Definir convenções de rotas (plural, PATCH vs PUT).",
        "Definir tipos de IDs (UUID vs inteiro).",
        "Definir paginação (page/limit ou cursor), ordenação e filtros.",
        "Publicar e revisar o OpenAPI.",
        "Anotar cada endpoint com as Regras relacionadas (IDs) e erros potenciais do Contrato de erros por regra."
      ],
      "entregaveis": [
        "Contrato estável e aprovado.",
        "OpenAPI revisado e versionado.",
        "Nenhum CRUD implementado ainda."
      ]
    },
    "fase_4_fastapi_minimo": {
      "titulo": "FASE 4 — FastAPI mínimo",
      "anchor_id": "fase-4-fastapi-minimo",
      "momento": "Após o contrato definido e aprovado.",
      "tarefas": [
        "Criar main.py.",
        "Criar rota /health.",
        "Criar routers vazios (placeholders) com prefixos e tags conforme o contrato."
      ],
      "entregaveis": [
        "API operacional mínima.",
        "OpenAPI acessível e consistente com o contrato.",
        "Sem CRUDs implementados."
      ]
    },
    "fase_5_cruds_execucao": {
      "titulo": "FASE 5 — CRUDs (execução)",
      "anchor_id": "fase-5-cruds-execucao",
      "momento": "Após o contrato aprovado e API mínima criada.",
      "tarefas_por_recurso": [
        "Model (SQLAlchemy).",
        "Schemas (Pydantic).",
        "Service (regras + transação, fronteira de transação declarada).",
        "Route (FastAPI com Depends, validação e permissão).",
        "Testes: unitários e de integração com DB; isolamento transacional (rollback por teste/fixture); smoke tests de fluxos críticos; meta de cobertura definida; implementar validações do serviço conforme Matriz de enforcement; cada validação e teste devem citar a Regra no nome/comentário."
      ],
      "garantias_qualidade": [
        "Evitar N+1 (selectinload/joinedload).",
        "Validar índices críticos.",
        "Garantir validações de entrada e de negócio alinhadas ao contrato."
      ],
      "entregaveis": [
        "CRUDs consistentes e cobertos por testes.",
        "Redução de retrabalho por aderência ao contrato."
      ]
    },
    "fase_6_endurecimento": {
      "titulo": "FASE 6 — Endurecimento",
      "anchor_id": "fase-6-endurecimento",
      "momento": "Após os primeiros CRUDs estarem funcionando.",
      "tarefas": [
        "Implementar permissões reais (RBAC) e escopos.",
        "Tornar transações explícitas; tratar idempotência quando necessário.",
        "Validar auditoria (logs de ações críticas, imutáveis).",
        "Implementar handler global de exceções: mapear IntegrityError para 409; padronizar mensagens conforme contrato de erro.",
        "Consolidar cobertura de testes.",
        "Configurar e estabilizar CI básico.",
        "Cobertura de regras críticas ≥ 90% (RDB4, RDB5, RDB9, RDB10, RDB13, RF15, RF5.2, R13/R14, RD13/RD22)."
      ],
      "entregaveis": [
        "Segurança e integridade elevadas.",
        "Qualidade assegurada por pipeline e testes."
      ]
    },
    "fase_7_producao_go_live": {
      "titulo": "FASE 7 — Produção (Go-Live)",
      "anchor_id": "fase-7-producao-go-live",
      "momento": "Sistema funcional e validado internamente.",
      "tarefas": {
        "autenticacao": [
          "JWT (access/refresh), expiração e revogação.",
          "Hash de senhas quando aplicável."
        ],
        "versao_api": [
          "Versionamento /v1 e política de breaking changes."
        ],
        "seguranca": [
          "CORS por ambiente.",
          "Security headers (X-Content-Type-Options, X-Frame-Options, Referrer-Policy, entre outros).",
          "Bloquear rotas de debug em produção.",
          "Rate limiting básico quando necessário."
        ],
        "observabilidade": [
          "Logging estruturado (request_id, user_id).",
          "Healthcheck incluindo DB e status de migrations.",
          "Métricas (Prometheus) e tracing (OpenTelemetry) opcionais."
        ],
        "performance_operacoes": [
          "Ajustar pool do DB e número de workers (uvicorn/gunicorn).",
          "Definir política de cache quando aplicável."
        ],
        "banco_migrations": [
          "Definir política de naming e rollback de migrations.",
          "Executar Alembic via CI.",
          "Separar seeds de migrations."
        ],
        "ci_cd": [
          "Lint/format/type-check.",
          "Executar migrations e smoke tests no pipeline.",
          "Variáveis de ambiente segregadas por ambiente.",
          "Branch Neon por PR (opcional)."
        ]
      },
      "entregaveis": [
        "Deploy apto para produção.",
        "Pipeline confiável.",
        "Operação monitorada."
      ]
    },
    "fase_8_producao_ready_checklist": {
      "titulo": "FASE 8 — Produção-ready (Checklist)",
      "anchor_id": "fase-8-producao-ready-checklist",
      "checklist": {
        "configuracao_e_segredos_12_factor": [
          "Configuração via variáveis de ambiente.",
          "Segredos (DB/JWT) seguros e rotacionáveis."
        ],
        "contrato_e_documentacao": [
          "OpenAPI publicado e revisado.",
          "README com: setup local, execução de testes, execução de migrations.",
          "Este fluxo documentado no repositório.",
          "Changelog/semver quando aplicável."
        ],
        "seguranca_minima": [
          "CORS e headers aplicados.",
          "Rotas de debug desativadas em produção.",
          "Validação de payload ativa.",
          "Rate limiting quando aplicável."
        ],
        "observabilidade": [
          "Logs com correlação.",
          "Logs de erro centralizados.",
          "Healthcheck ampliado (DB + migrations)."
        ],
        "performance": [
          "Índices críticos validados.",
          "Paginação obrigatória em listagens.",
          "Ausência de N+1 nas rotas críticas."
        ],
        "banco_e_auditoria": [
          "Alembic controlado por CI.",
          "Política de rollback definida.",
          "Auditoria imutável verificada."
        ],
        "ci_cd": [
          "Pipelines com lint/format/type-check.",
          "Migrations e smoke tests no CI.",
          "Gate de merge por falha.",
          "Variáveis por ambiente.",
          "Branch Neon por PR (opcional)."
        ]
      }
    }
  },
  "matriz_enforcement_regras": [
    {
      "regra": "RDB9 (exclusividade de vínculo)",
      "camada": "DB + Backend",
      "enforcement": "Índices/constraints p/ 1 vínculo ativo por staff e 1 por pessoa+temporada (atleta) + validação de serviço",
      "teste_minimo": "tests/membership/test_RDB9_exclusividade.py"
    },
    {
      "regra": "RDB10 (team_registrations por período)",
      "camada": "DB + Backend",
      "enforcement": "Períodos não sobrepostos p/ pessoa+equipe+temporada; reativação cria nova linha",
      "teste_minimo": "tests/teams/test_RDB10_periodos.py"
    },
    {
      "regra": "RF15/RDB13 (jogo finalizado/reabertura)",
      "camada": "DB + Backend",
      "enforcement": "Trigger bloqueia UPDATE quando finalizado; reabertura muda status p/ em_revisao com audit log",
      "teste_minimo": "tests/games/test_RF15_reabertura.py"
    },
    {
      "regra": "R13/R14 (dispensada encerra participações)",
      "camada": "Backend",
      "enforcement": "Ao mudar p/ “dispensada”, encerra team_registrations vigentes; reativações criam novas linhas",
      "teste_minimo": "tests/athletes/test_R13_dispensa_encerramento.py"
    },
    {
      "regra": "RD13/RD22 (goleira vs atleta de linha)",
      "camada": "Backend + Front",
      "enforcement": "Bloquear stats/tempo de linha para goleira; goleiro-linha só p/ atletas de linha",
      "teste_minimo": "tests/stats/test_RD13_goalkeeper_rules.py"
    },
    {
      "regra": "RF5.2 (temporada interrompida)",
      "camada": "Backend",
      "enforcement": "Bloquear novos eventos após interrupted_at; cancelar jogos futuros",
      "teste_minimo": "tests/seasons/test_RF52_interrupcao.py"
    },
    {
      "regra": "R16/RD1-RD2 (faixa etária/categoria)",
      "camada": "Backend",
      "enforcement": "Validar atuação só na própria categoria ou acima",
      "teste_minimo": "tests/athletes/test_R16_categoria.py"
    },
    {
      "regra": "R35/RDB5 (logs imutáveis)",
      "camada": "DB",
      "enforcement": "audit_logs append-only; triggers bloqueiam UPDATE/DELETE",
      "teste_minimo": "tests/audit/test_R35_immutability.py"
    }
  ],
  "contrato_erros_por_regra": [
    {
      "id": "409_conflict_membership_active",
      "regras_relacionadas": ["RDB9"],
      "http_status": 409,
      "exemplo_resposta": {
        "code": "conflict_membership_active",
        "message": "Já existe vínculo ativo",
        "details": { "regra": "RDB9" }
      }
    },
    {
      "id": "409_edit_finalized_game",
      "regras_relacionadas": ["RDB13", "RF15"],
      "http_status": 409,
      "exemplo_resposta": {
        "code": "edit_finalized_game",
        "message": "Jogo finalizado é somente leitura",
        "details": { "regra": "RDB13" }
      }
    },
    {
      "id": "422_invalid_goalkeeper_stat",
      "regras_relacionadas": ["RD13"],
      "http_status": 422,
      "exemplo_resposta": {
        "code": "invalid_goalkeeper_stat",
        "message": "Goleira não pode registrar estatística de linha",
        "details": { "regra": "RD13" }
      }
    },
    {
      "id": "409_season_interrupted_locked",
      "regras_relacionadas": ["RF5.2", "R37"],
      "http_status": 409,
      "exemplo_resposta": {
        "code": "season_locked",
        "message": "Temporada interrompida: criação/edição bloqueada",
        "details": { "regra": "RF5.2" }
      }
    },
    {
      "id": "403_permission_denied",
      "regras_relacionadas": ["R25", "R26"],
      "http_status": 403,
      "exemplo_resposta": {
        "code": "permission_denied",
        "message": "Permissão insuficiente",
        "details": { "regra": "R25" }
      }
    },
    {
      "id": "422_age_category_violation",
      "regras_relacionadas": ["R16", "RD1", "RD2"],
      "http_status": 422,
      "exemplo_resposta": {
        "code": "age_category_violation",
        "message": "Atuação abaixo da categoria não permitida",
        "details": { "regra": "R16" }
      }
    }
  ],
  "blueprints_db_rdb": [
    {
      "id": "RDB9",
      "titulo": "exclusividade de vínculo ativo (índice parcial)",
      "sql": {
        "staff_unico_por_pessoa": "CREATE UNIQUE INDEX ux_membership_active_staff\n  ON membership(person_id)\n  WHERE role IN ('COACH','COORDINATOR','DIRECTOR') AND end_at IS NULL;",
        "athlete_unico_por_pessoa_temporada": "CREATE UNIQUE INDEX ux_membership_active_athlete\n  ON membership(person_id, season_id)\n  WHERE role = 'ATHLETE' AND end_at IS NULL;"
      }
    },
    {
      "id": "RDB10",
      "titulo": "períodos não sobrepostos em team_registrations",
      "nota": "Se não usar EXCLUDE, garantir no backend e registrar CHECKs simples (start_at < end_at)."
    },
    {
      "id": "RDB4",
      "titulo": "exclusão lógica obrigatória",
      "nota": "Tabelas-chave com deleted_at TIMESTAMPTZ NULL e deleted_reason TEXT NOT NULL quando deleted_at IS NOT NULL."
    },
    {
      "id": "RDB13",
      "titulo": "jogo finalizado imutável",
      "sql": {
        "function": "CREATE OR REPLACE FUNCTION trg_block_update_finalized() RETURNS trigger AS $$\nBEGIN\n  IF NEW.status = 'finalizado' AND OLD.status = 'finalizado' THEN\n    RAISE EXCEPTION 'jogo finalizado é somente leitura';\n  END IF;\n  RETURN NEW;\nEND; $$ LANGUAGE plpgsql;",
        "trigger": "CREATE TRIGGER trg_games_block_update_finalized\n  BEFORE UPDATE ON games\n  FOR EACH ROW\n  WHEN (OLD.status = 'finalizado' AND NEW.status = 'finalizado')\n  EXECUTE FUNCTION trg_block_update_finalized();"
      }
    }
  ],
  "convencoes_referencia_regras": {
    "comentarios_docstrings": [
      "Enforce RDB10: proibir sobreposição de períodos (service/team_registrations.py)"
    ],
    "nomes_testes": [
      "test_RDB9_exclusividade_vinculo_staff",
      "test_RF15_reabertura_bloqueia_dashboards"
    ],
    "mensagens_commit_conventional_commits": [
      "feat(membership): enforce RDB9 exclusividade de vínculo ativo",
      "fix(games): respeitar RDB13 ao atualizar jogo finalizado"
    ],
    "pr_template_resumo": {
      "regras_impactadas": ["RDB9", "RF15"],
      "validacoes_erros_adicionados": ["409_conflict_membership_active"],
      "migracoes": "sim/não; dry-run anexo"
    }
  },
  "convencoes_estrutura_pastas": {
    "estrutura_sugerida_texto": "backend/\n  app/\n    core/            # config, security, logging, db\n    models/          # SQLAlchemy models\n    schemas/         # Pydantic schemas\n    services/        # regras + transações\n    api/\n      v1/\n        routers/     # endpoints por recurso\n        deps/        # Depends (get_db, auth, perms)\n    tests/\n      integration/\n      unit/\n    main.py\n  alembic/\n  alembic.ini\n  .env.example",
    "convencoes": [
      "Rotas: /v1/<recurso> (plural).",
      "IDs: UUID v4 (preferencial).",
      "Paginação: ?page=1&limit=50 ou cursor (padronizar na Fase 3).",
      "Erros: { code, message, details? }.",
      "Commits: Conventional Commits (feat:, fix:, docs:, chore:).",
      "Branches: feat/<escopo>, fix/<escopo>."
    ]
  },
  "templates_minimos": [
    {
      "nome": "main.py",
      "caminho": "app/main.py",
      "linguagem": "python",
      "conteudo": "from fastapi import FastAPI\nfrom app.api.v1.routers import health\n\ndef create_app() -> FastAPI:\n    app = FastAPI(title=\"HandLab API\", version=\"1.0.0\")\n    app.include_router(health.router, prefix=\"/v1\")\n    return app\n\napp = create_app()\n"
    },
    {
      "nome": "api/v1/routers/health.py",
      "caminho": "app/api/v1/routers/health.py",
      "linguagem": "python",
      "conteudo": "from fastapi import APIRouter\nfrom app.core.db import healthcheck_db\n\nrouter = APIRouter(tags=[\"health\"])\n\n@router.get(\"/health\")\ndef health():\n    return {\"status\": \"ok\", \"db\": healthcheck_db()}\n"
    },
    {
      "nome": "core/config.py",
      "caminho": "app/core/config.py",
      "linguagem": "python",
      "conteudo": "from pydantic_settings import BaseSettings\n\nclass Settings(BaseSettings):\n    DATABASE_URL: str\n    ENV: str = \"local\"\n\n    class Config:\n        env_file = \".env\"\n\nsettings = Settings()\n"
    },
    {
      "nome": "core/db.py",
      "caminho": "app/core/db.py",
      "linguagem": "python",
      "conteudo": "from sqlalchemy import create_engine, text\nfrom sqlalchemy.orm import sessionmaker\nfrom app.core.config import settings\n\nengine = create_engine(settings.DATABASE_URL, pool_pre_ping=True, future=True)\nSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)\n\ndef get_db():\n    db = SessionLocal()\n    try:\n        yield db\n        db.commit()\n    except:\n        db.rollback()\n        raise\n    finally:\n        db.close()\n\ndef healthcheck_db():\n    with engine.connect() as conn:\n        conn.execute(text(\"SELECT 1\"))\n    return \"ok\"\n"
    },
    {
      "nome": "tests/conftest.py",
      "caminho": "app/tests/conftest.py",
      "linguagem": "python",
      "conteudo": "import pytest\nimport sqlalchemy as sa\nfrom sqlalchemy.orm import sessionmaker\n\nfrom app.core.db import engine\n\n@pytest.fixture\ndef db():\n    # Conexão e transação raiz\n    connection = engine.connect()\n    transaction = connection.begin()\n\n    # Session ligada à conexão da transação raiz\n    TestingSessionLocal = sessionmaker(bind=connection, autocommit=False, autoflush=False, future=True)\n    session = TestingSessionLocal()\n\n    # Savepoint para cada teste\n    session.begin_nested()\n\n    # Recria savepoint após commits dentro do teste\n    @sa.event.listens_for(session, \"after_transaction_end\")\n    def restart_savepoint(sess, trans):\n        if trans.nested and not trans._parent.nested:\n            sess.begin_nested()\n\n    try:\n        yield session\n    finally:\n        session.close()\n        transaction.rollback()\n        connection.close()\n"
    },
    {
      "nome": "schemas/error.py",
      "caminho": "app/schemas/error.py",
      "linguagem": "python",
      "conteudo": "from pydantic import BaseModel\nfrom typing import Any, Optional\n\nclass ErrorResponse(BaseModel):\n    code: str\n    message: str\n    details: Optional[Any] = None\n"
    }
  ],
  "comandos_cheatsheet": {
    "ambiente": [
      "python -m venv .venv && source .venv/bin/activate",
      "pip install -r requirements.txt"
    ],
    "alembic_diagnostico_nao_destrutivo_neon": [
      "echo \"$DATABASE_URL\"",
      "alembic heads",
      "alembic current",
      "ls -lt alembic/versions | head -3",
      "alembic upgrade head --sql > review.sql"
    ],
    "alembic_acoes_seguras_pos_diagnostico": [
      "alembic stamp <HEAD>",
      "alembic upgrade head",
      "alembic revision --autogenerate -m \"reconcile schema\"",
      "alembic merge -m \"merge heads\" <rev1> <rev2> [...]"
    ],
    "testes": [
      "pytest -q"
    ],
    "lint_format": [
      "ruff check . && ruff format .",
      "black . && isort . && flake8 ."
    ],
    "execucao": [
      "uvicorn app.main:app --reload"
    ]
  },
  "prompts_prontos_para_copilot_codex": [
    "Gerar CRUD completo para o recurso X seguindo: models em app/models, schemas em app/schemas, service com transação e validações, route em app/api/v1/routers/X.py com Depends(get_db) e permissões mock. Incluir testes unitários e de integração com fixture db.",
    "Criar handler global de exceções que converta IntegrityError em HTTP 409 com ErrorResponse padrão.",
    "Adicionar paginação page/limit na rota GET /v1/<recurso> com validação de limites e ordenação por created_at desc.",
    "Otimizar consulta de <recurso> para evitar N+1 usando selectinload em relacionamentos.",
    "Escrever Alembic revision para criar tabela <nome> com PK UUID e índices em (created_at) e (foreign_key).",
    "Criar tasks do VS Code para diagnóstico Alembic ↔ Neon e executar dry-run não-destrutivo (gerando review.sql) antes de upgrades em ambientes críticos."
  ],
  "variaveis_ambiente_env_exemplo": {
    "conteudo_texto": "ENV=local\nDATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname\nJWT_SECRET=change-me\nJWT_EXPIRES_MINUTES=15\nCORS_ORIGINS=http://localhost:3000\n",
    "valores_exemplo": {
      "ENV": "local",
      "DATABASE_URL": "postgresql+psycopg2://user:pass@host:5432/dbname",
      "JWT_SECRET": "change-me",
      "JWT_EXPIRES_MINUTES": 15,
      "CORS_ORIGINS": "http://localhost:3000"
    }
  },
  "ci_cd_basico_esqueleto": {
    "passos_minimos": [
      "Instalar dependências.",
      "Executar linters/formatadores/type-check.",
      "Subir banco de teste.",
      "Executar alembic upgrade head.",
      "Executar pytest -q.",
      "Exportar artefato do OpenAPI via script Python."
    ],
    "script_export_openapi": "python - << 'PY'\nfrom app.main import app\nimport json\nopen(\"openapi.json\", \"w\").write(json.dumps(app.openapi()))\nPY\n",
    "politica": [
      "Qualquer falha bloqueia merge.",
      "Migrations sempre executadas no CI.",
      "Variáveis segregadas por ambiente.",
      "Em ambientes de release, gerar e revisar dry-run (--sql) antes de aplicar migrations."
    ]
  },
  "gitignore_sugerido": {
    "conteudo_texto": "# Alembic dry-runs\nreview.sql\n",
    "itens": [
      "review.sql"
    ]
  },
  "definition_of_done_por_fase": {
    "fase_0": [
      { "item": "Regras do sistema disponíveis ao Codex/Copilot.", "done": true },
      { "item": "Entidades principais identificadas.", "done": true },
      { "item": "Sem código produzido.", "done": true }
    ],
    "fase_1": [
      { "item": "DATABASE_URL válido e segregado por ambiente.", "done": true },
      { "item": "Diagnóstico Alembic ↔ Neon executado.", "done": true },
      { "item": "Estado definido: no HEAD (repo/db = 3e2898989f01).", "done": true },
      { "item": "review.sql ignorado no git (.gitignore).", "done": true }
    ],
    "fase_2": [
      { "item": "config.py, db.py e get_db implementados.", "done": false },
      { "item": "Autenticação e permissões mock implementadas.", "done": false },
      { "item": "/v1/health responde com sucesso (se exposto).", "done": false }
    ],
    "fase_3": [
      { "item": "OpenAPI revisado, versionado (/v1) e aprovado.", "done": false },
      { "item": "Convenções de erro, paginação e tipos de ID definidas.", "done": false }
    ],
    "fase_4": [
      { "item": "Routers vazios por recurso criados.", "done": false },
      { "item": "OpenAPI acessível e coerente com o contrato.", "done": false }
    ],
    "fase_5": [
      { "item": "Model, Schema, Service, Route e Testes por recurso concluídos.", "done": false },
      { "item": "Ausência de N+1 nas rotas críticas.", "done": false },
      { "item": "Índices verificados.", "done": false }
    ],
    "fase_6": [
      { "item": "RBAC real implementado.", "done": false },
      { "item": "Handler global de exceções configurado.", "done": false },
      { "item": "Auditoria validada.", "done": false },
      { "item": "CI básico executando com sucesso.", "done": false }
    ],
    "fase_7": [
      { "item": "JWT (access/refresh) operacional.", "done": false },
      { "item": "CORS e headers configurados.", "done": false },
      { "item": "Health inclui DB e migrations.", "done": false },
      { "item": "Pipeline executa migrations e smoke tests.", "done": false }
    ],
    "fase_8": [
      { "item": "README completo (setup, testes, migrations).", "done": false },
      { "item": "OpenAPI publicado.", "done": false },
      { "item": "Alembic via CI e política de rollback definida.", "done": false },
      { "item": "Logging estruturado ativo.", "done": false }
    ]
  },
  "status_final_backend": {
    "criterios_encerramento": [
      "Infraestrutura concluída.",
      "Núcleo concluído.",
      "Contrato concluído.",
      "CRUDs concluídos.",
      "Permissões concluídas.",
      "Transações concluídas.",
      "Testes concluídos.",
      "CI concluído.",
      "Operacionalização concluída."
    ],
    "observacao": "Quando todos os critérios forem atendidos, o backend está encerrado."
  }
}

{
  "source_file": "regras_sistema_v1.1.json",
  "chunking_strategy": {
    "type": "por_secao_com_faixas",
    "descricao": "Chunks por grandes seções do documento, dividindo listas extensas em faixas de IDs (ex.: R1-R15).",
    "conteudo": "completo",
    "observacoes": [
      "Cada chunk embute o conteúdo completo das partes referenciadas.",
      "Faixas podem ser ajustadas conforme preferência de tamanho (itens ou caracteres)."
    ]
  },
  "chunks": [
    {
      "id": "chunk-01",
      "titulo": "Metadados e Sumário",
      "paths": [
        "/metadata",
        "/sumario"
      ],
      "conteudo": {
        "/metadata": {
          "versao_documento": "V1.1",
          "gerado_em": "2025-12-23",
          "autor_login": "Davisermenho",
          "idioma": "pt-BR",
          "titulo": "REGRAS DO SISTEMA (V1.1)"
        },
        "/sumario": [
          "1. Regras Estruturais",
          "2. Regras Operacionais - V1 (Consolidadas)",
          "3. Regras de Domínio Esportivo - Definitivas",
          "4. Visibilidade do Perfil Atleta",
          "5. Regras de Participação da Atleta - Definitivas",
          "6. Regras de Configuração do Banco - V1",
          "6.1 Esquema técnico (temporadas e jogos)",
          "7. Organização das Regras por Camada de Configuração"
        ]
      },
      "approx_item_count": 2
    },
    {
      "id": "chunk-02",
      "titulo": "Regras Estruturais (R1-R15)",
      "paths": [
        "/regras_estruturais/0",
        "/regras_estruturais/1",
        "/regras_estruturais/2",
        "/regras_estruturais/3",
        "/regras_estruturais/4",
        "/regras_estruturais/5",
        "/regras_estruturais/6",
        "/regras_estruturais/7",
        "/regras_estruturais/8",
        "/regras_estruturais/9",
        "/regras_estruturais/10",
        "/regras_estruturais/11",
        "/regras_estruturais/12",
        "/regras_estruturais/13",
        "/regras_estruturais/14"
      ],
      "conteudo": {
        "/regras_estruturais/0": { "id": "R1", "titulo": "Pessoa", "descricao": "Pessoa representa o indivíduo real e é independente de função esportiva." },
        "/regras_estruturais/1": { "id": "R2", "titulo": "Usuário", "descricao": "Usuário representa acesso ao sistema. Apenas o Super Administrador pode existir sem vínculo organizacional." },
        "/regras_estruturais/2": { "id": "R3", "titulo": "Super Administrador", "descricao": "Existe exatamente um Super Administrador estrutural, vitalício, imutável e não removível. Possui autoridade máxima e pode ignorar travas operacionais; toda ação crítica é auditada." },
        "/regras_estruturais/3": { "id": "R4", "titulo": "Papéis do sistema", "descricao": "Papéis organizacionais válidos: Dirigente, Coordenador, Treinador, Atleta." },
        "/regras_estruturais/4": { "id": "R5", "titulo": "Papéis não acumuláveis", "descricao": "Uma pessoa não pode ter múltiplos papéis ativos simultaneamente. Mudanças de papel exigem encerramento de vínculo e criação de novo, sem sobreposição temporal." },
        "/regras_estruturais/5": { "id": "R6", "titulo": "Vínculo organizacional", "descricao": "Toda atuação no sistema ocorre por meio de vínculo entre pessoa, papel, clube e temporada." },
        "/regras_estruturais/6": { "id": "R7", "titulo": "Vínculo ativo e exclusividade", "descricao": "Regra geral: uma pessoa possui apenas um vínculo ativo. Exceção: atleta pode ter múltiplos vínculos ativos simultâneos em equipes diferentes, desde que as competições permitam. Papéis Dirigente, Coordenador e Treinador são exclusivos.", "observacao": "Para atleta, múltiplos vínculos por temporada são realizados via team_registrations (ver RDB10)." },
        "/regras_estruturais/7": { "id": "R8", "titulo": "Temporada obrigatória", "descricao": "Todo vínculo ativo deve estar associado a uma temporada." },
        "/regras_estruturais/8": { "id": "R9", "titulo": "Encerramento de vínculo", "descricao": "Encerramento é manual, solicitado pelo usuário e validado pelo Coordenador (ou Dirigente quando exigido). O encerramento automático ocorre apenas no fim da vigência/temporada quando não há renovação." },
        "/regras_estruturais/9": { "id": "R10", "titulo": "Encerramento automático de temporada", "descricao": "Ao final da temporada o sistema encerra automaticamente todos os vínculos ativos, impedindo extensão temporal ou reativação retroativa." },
        "/regras_estruturais/10": { "id": "R11", "titulo": "Histórico imutável", "descricao": "Vínculos encerrados jamais são apagados ou alterados retroativamente." },
        "/regras_estruturais/11": { "id": "R12", "titulo": "Atleta como papel permanente", "descricao": "Atleta é papel permanente no histórico: uma pessoa nunca deixa de ser atleta no histórico, embora não possa acumular papéis simultaneamente." },
        "/regras_estruturais/12": { "id": "R13", "titulo": "Estados operacionais da atleta", "descricao": "Estados válidos: ativa, lesionada, dispensada. Estado não equivale a encerramento de vínculo, exceto em \"dispensada\".", "complemento_v1_1": "Ao mudar para “dispensada”, o sistema encerra imediatamente todas as participações em equipes (team_registrations) ativas da temporada, mantendo o membership de atleta da temporada para histórico/consulta. Reativações criam novas linhas em team_registrations (novo UUID) a partir da data de reativação, sem reabrir registros encerrados." },
        "/regras_estruturais/13": { "id": "R14", "titulo": "Impacto dos estados", "impacto_dos_estados": { "ativa": "Participa de tudo.", "lesionada": "Participa normalmente de jogos e treinos; estatísticas (de jogo e de treino) entram nos agregados; o sistema exibe alertas e visibilidade específica; pode receber comunicação específica.", "dispensada": "Aparece apenas em histórico; não entra em estatísticas; não recebe comunicação operacional." } },
        "/regras_estruturais/14": { "id": "R15", "titulo": "Categorias globais", "descricao": "Categorias são globais e definidas exclusivamente por idade." }
      },
      "range_ids": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15"],
      "approx_item_count": 15
    },
    {
      "id": "chunk-03",
      "titulo": "Regras Estruturais (R16-R43)",
      "paths": [
        "/regras_estruturais/15",
        "/regras_estruturais/16",
        "/regras_estruturais/17",
        "/regras_estruturais/18",
        "/regras_estruturais/19",
        "/regras_estruturais/20",
        "/regras_estruturais/21",
        "/regras_estruturais/22",
        "/regras_estruturais/23",
        "/regras_estruturais/24",
        "/regras_estruturais/25",
        "/regras_estruturais/26",
        "/regras_estruturais/27",
        "/regras_estruturais/28",
        "/regras_estruturais/29",
        "/regras_estruturais/30",
        "/regras_estruturais/31",
        "/regras_estruturais/32",
        "/regras_estruturais/33",
        "/regras_estruturais/34",
        "/regras_estruturais/35",
        "/regras_estruturais/36",
        "/regras_estruturais/37",
        "/regras_estruturais/38",
        "/regras_estruturais/39",
        "/regras_estruturais/40",
        "/regras_estruturais/41",
        "/regras_estruturais/42"
      ],
      "conteudo": {
        "/regras_estruturais/15": { "id": "R16", "titulo": "Regra etária obrigatória", "descricao": "A atleta pode atuar na sua categoria ou em categorias acima, nunca em categorias abaixo." },
        "/regras_estruturais/16": { "id": "R17", "titulo": "Múltiplas equipes", "descricao": "A participação da atleta em equipes é temporal, vinculada à temporada, e pode ser encerrada antes do término por decisão administrativa auditável." },
        "/regras_estruturais/17": { "id": "R18", "titulo": "Treinos", "descricao": "Treinos são eventos operacionais, editáveis dentro dos limites do sistema (R40), históricos e usados para carga, presença e análise." },
        "/regras_estruturais/18": { "id": "R19", "titulo": "Jogos", "descricao": "Jogos são eventos oficiais e, após finalizados, são imutáveis como evento; alterações só ocorrem por reabertura (RF15)." },
        "/regras_estruturais/19": { "id": "R20", "titulo": "Estatísticas primárias", "descricao": "Estatísticas primárias estão sempre vinculadas a um jogo." },
        "/regras_estruturais/20": { "id": "R21", "titulo": "Estatísticas agregadas", "descricao": "Estatísticas agregadas são derivadas e recalculáveis; nunca são fonte primária." },
        "/regras_estruturais/21": { "id": "R22", "titulo": "Métricas de treino", "descricao": "Dados de treino são métricas operacionais (carga, PSE, assiduidade) e não substituem estatísticas primárias de jogo." },
        "/regras_estruturais/22": { "id": "R23", "titulo": "Correção permitida com justificativa", "descricao": "Correções em estatísticas são permitidas somente com justificativa obrigatória, identificação do responsável e data/hora." },
        "/regras_estruturais/23": { "id": "R24", "titulo": "Preservação do dado anterior", "descricao": "O dado corrigido substitui o anterior para fins operacionais; o valor anterior é preservado apenas para auditoria, sem efeito analítico." },
        "/regras_estruturais/24": { "id": "R25", "titulo": "Permissões por papel", "descricao": "Permissões são definidas por papel e aplicadas via vínculo." },
        "/regras_estruturais/25": { "id": "R26", "titulo": "Escopo implícito", "escopo_por_papel": { "Treinador": "Acesso apenas às suas equipes.", "Coordenador": "Acesso total a dados operacionais e esportivos.", "Dirigente": "Acesso administrativo.", "Atleta": "Acesso restrito aos próprios dados." } },
        "/regras_estruturais/26": { "id": "R27", "titulo": "Troca de função", "descricao": "Não existe troca direta de papel." },
        "/regras_estruturais/27": { "id": "R28", "titulo": "Transição obrigatória", "descricao": "O vínculo atual é encerrado, um novo vínculo é criado, sem sobreposição temporal." },
        "/regras_estruturais/28": { "id": "R29", "titulo": "Exclusão lógica", "descricao": "Nenhuma entidade relevante é apagada fisicamente." },
        "/regras_estruturais/29": { "id": "R30", "titulo": "Reativação de vínculo", "descricao": "Vínculos podem ser reativados desde que não violem exclusividade, não alterem histórico passado e passem a valer somente a partir da data de reativação." },
        "/regras_estruturais/30": { "id": "R31", "titulo": "Ações críticas auditáveis", "descricao": "São obrigatoriamente auditadas: correção de estatística, encerramento de vínculo, reativação de vínculo, exclusão lógica de jogo, mudança de estado de atleta." },
        "/regras_estruturais/31": { "id": "R32", "titulo": "Log obrigatório", "descricao": "Todo evento crítico deve registrar quem, quando, o quê e contexto." },
        "/regras_estruturais/32": { "id": "R33", "titulo": "Regra de ouro do sistema", "descricao": "Nada acontece fora de um vínculo. Nada relevante é apagado. Nada histórico é sobrescrito sem rastro." },
        "/regras_estruturais/33": { "id": "R34", "titulo": "Clube único na V1", "descricao": "Existe exatamente um clube no sistema na V1; não há suporte a múltiplos clubes." },
        "/regras_estruturais/34": { "id": "R35", "titulo": "Imutabilidade dos logs", "descricao": "Logs de auditoria são absolutamente imutáveis, não podendo ser alterados ou removidos, nem pelo Super Administrador." },
        "/regras_estruturais/35": { "id": "R36", "titulo": "Autoridade de correção de estatísticas", "descricao": "Correções de estatísticas podem ser realizadas por qualquer papel durante temporada ativa, obedecendo R23 e R24. Após encerramento da temporada, apenas Coordenador e Dirigente, via ação administrativa auditada." },
        "/regras_estruturais/36": { "id": "R37", "titulo": "Edição após encerramento da temporada", "descricao": "Após o encerramento da temporada, qualquer edição de dados operacionais ou esportivos só pode ocorrer por ação administrativa auditada, sem reabertura temporal." },
        "/regras_estruturais/37": { "id": "R38", "titulo": "Obrigatoriedade de equipe para atleta", "descricao": "A atleta não pode existir em uma temporada sem estar vinculada a pelo menos uma equipe (competitiva ou institucional, ver R39). Criação ou reativação de vínculo de atleta exige associação imediata a uma equipe." },
        "/regras_estruturais/38": { "id": "R39", "titulo": "Atividades sem equipe competitiva", "descricao": "Atividades sem equipe (avaliações, testes, captação) devem ser vinculadas à Equipe Institucional ou Grupo de Avaliação." },
        "/regras_estruturais/39": { "id": "R40", "titulo": "Limite temporal de edição de treinos", "descricao": "O autor tem 10 minutos para correções rápidas. Após esse prazo, até 24 horas, qualquer edição exige aprovação ou perfil de nível superior. Após 24 horas, o registro é somente leitura, exceto por ação administrativa auditada." },
        "/regras_estruturais/40": { "id": "R41", "titulo": "Resolução de conflitos de edição", "descricao": "Em conflito simultâneo de edição, o sistema registra o conflito, bloqueia a sobrescrita automática e exige decisão explícita de usuário autorizado, com auditoria." },
        "/regras_estruturais/41": { "id": "R42", "titulo": "Modo somente leitura sem vínculo", "descricao": "Usuários sem vínculo ativo não podem operar no sistema. Atletas mantêm acesso somente leitura ao próprio histórico pessoal e estatísticas individuais, sem interação nem dados coletivos." },
        "/regras_estruturais/42": { "id": "R43", "titulo": "Hierarquia formal", "descricao": "1. Dirigente (Super Administrador) > 2. Coordenador > 3. Treinador/Staff > 4. Atleta." }
      },
      "range_ids": ["R16","R17","R18","R19","R20","R21","R22","R23","R24","R25","R26","R27","R28","R29","R30","R31","R32","R33","R34","R35","R36","R37","R38","R39","R40","R41","R42","R43"],
      "approx_item_count": 28
    },
    {
      "id": "chunk-04",
      "titulo": "Regras Operacionais (RF1-RF15)",
      "paths": [
        "/regras_operacionais_v1_consolidadas/0",
        "/regras_operacionais_v1_consolidadas/1",
        "/regras_operacionais_v1_consolidadas/2",
        "/regras_operacionais_v1_consolidadas/3",
        "/regras_operacionais_v1_consolidadas/4",
        "/regras_operacionais_v1_consolidadas/5",
        "/regras_operacionais_v1_consolidadas/6",
        "/regras_operacionais_v1_consolidadas/7",
        "/regras_operacionais_v1_consolidadas/8",
        "/regras_operacionais_v1_consolidadas/9",
        "/regras_operacionais_v1_consolidadas/10",
        "/regras_operacionais_v1_consolidadas/11",
        "/regras_operacionais_v1_consolidadas/12",
        "/regras_operacionais_v1_consolidadas/13",
        "/regras_operacionais_v1_consolidadas/14"
      ],
      "conteudo": {
        "/regras_operacionais_v1_consolidadas/0": { "id": "RF1", "titulo": "Cadeia hierárquica de criação de pessoas e usuários", "descricao": "Dirigentes criam coordenadores. Coordenadores criam treinadores. Treinadores criam atletas. A criação gera automaticamente o papel correspondente." },
        "/regras_operacionais_v1_consolidadas/1": { "id": "RF2", "titulo": "Identidade baseada em papel", "descricao": "Pessoas só existem no sistema se identificadas como dirigente, coordenador, treinador ou atleta." },
        "/regras_operacionais_v1_consolidadas/2": { "id": "RF3", "titulo": "Usuário sem vínculo ativo", "descricao": "Usuários (exceto Super Administrador) não podem operar no sistema sem vínculo ativo; atletas mantêm acesso somente leitura ao próprio histórico (ver R42)." },
        "/regras_operacionais_v1_consolidadas/3": { "id": "RF4", "titulo": "Criação de temporadas", "descricao": "Dirigentes, coordenadores e treinadores podem criar temporadas, inclusive futuras." },
        "/regras_operacionais_v1_consolidadas/4": {
          "id": "RF5",
          "titulo": "Encerramento de temporada",
          "descricao": "Nenhuma temporada pode ser encerrada manualmente após iniciada; o encerramento ocorre de forma automática ao fim do período anual.",
          "subregras_v1_1": [
            { "id": "RF5.1", "titulo": "Cancelamento antes do início", "descricao": "Permitido apenas se a temporada não possuir dados vinculados (equipes, jogos, treinos, convocações, participações, etc.). Havendo dados, é obrigatório mover/encerrar esses registros antes do cancelamento. Tudo é auditado." },
            { "id": "RF5.2", "titulo": "Interrupção após início (força maior)", "descricao": "Não há encerramento manual. A temporada recebe o estado operacional “Interrompida” a partir da data do evento; o sistema bloqueia criação/edição de novos eventos e cancela automaticamente jogos futuros. A end_date permanece inalterada. Tudo é auditado." }
          ]
        },
        "/regras_operacionais_v1_consolidadas/5": { "id": "RF6", "titulo": "Criação de equipes", "descricao": "Dirigentes e coordenadores podem criar equipes. Equipes podem existir temporariamente sem atletas vinculadas." },
        "/regras_operacionais_v1_consolidadas/6": { "id": "RF7", "titulo": "Alteração de treinador responsável pela equipe", "descricao": "A troca pode ser feita por dirigente ou coordenador, é auditável e não altera histórico passado." },
        "/regras_operacionais_v1_consolidadas/7": { "id": "RF8", "titulo": "Encerramento de equipes", "descricao": "Equipes encerradas deixam de operar, permanecem em histórico e não participam de relatórios ativos." },
        "/regras_operacionais_v1_consolidadas/8": { "id": "RF9", "titulo": "Criação de registros esportivos", "descricao": "Jogos, treinos e estatísticas podem ser criados por coordenadores e treinadores." },
        "/regras_operacionais_v1_consolidadas/9": { "id": "RF10", "titulo": "Registro de presença em treinos", "descricao": "Podem registrar presença: dirigentes, coordenadores e treinadores." },
        "/regras_operacionais_v1_consolidadas/10": { "id": "RF11", "titulo": "Convocação e recusa de atleta", "descricao": "Atletas podem recusar convocações; a recusa exige justificativa registrada; a convocação permanece no histórico com status atualizado." },
        "/regras_operacionais_v1_consolidadas/11": { "id": "RF12", "titulo": "Edição de treinos", "descricao": "Segue R40." },
        "/regras_operacionais_v1_consolidadas/12": { "id": "RF13", "titulo": "Conflito de edição", "descricao": "Segue R41." },
        "/regras_operacionais_v1_consolidadas/13": { "id": "RF14", "titulo": "Finalização de jogos", "descricao": "Jogos podem ser finalizados por dirigentes, coordenadores e treinadores." },
        "/regras_operacionais_v1_consolidadas/14": { "id": "RF15", "titulo": "Reabertura e exclusão lógica de jogos", "descricao": "Reabertura é permitida apenas pelo Coordenador e sempre via ação administrativa auditada. Ao reabrir, o mesmo registro do jogo retorna ao status “Em Revisão” (sem criação de nova versão/snapshot). As estatísticas deixam de alimentar dashboards até a nova finalização. Exclusão lógica de jogo pode ser feita por Coordenador ou Dirigente, sempre auditada.", "atualizacao_v1_1": true }
      },
      "range_ids": ["RF1","RF2","RF3","RF4","RF5","RF6","RF7","RF8","RF9","RF10","RF11","RF12","RF13","RF14","RF15"],
      "approx_item_count": 15
    },
    {
      "id": "chunk-05",
      "titulo": "Regras Operacionais (RF16-RF31)",
      "paths": [
        "/regras_operacionais_v1_consolidadas/15",
        "/regras_operacionais_v1_consolidadas/16",
        "/regras_operacionais_v1_consolidadas/17",
        "/regras_operacionais_v1_consolidadas/18",
        "/regras_operacionais_v1_consolidadas/19",
        "/regras_operacionais_v1_consolidadas/20",
        "/regras_operacionais_v1_consolidadas/21",
        "/regras_operacionais_v1_consolidadas/22",
        "/regras_operacionais_v1_consolidadas/23",
        "/regras_operacionais_v1_consolidadas/24",
        "/regras_operacionais_v1_consolidadas/25",
        "/regras_operacionais_v1_consolidadas/26",
        "/regras_operacionais_v1_consolidadas/27",
        "/regras_operacionais_v1_consolidadas/28",
        "/regras_operacionais_v1_consolidadas/29",
        "/regras_operacionais_v1_consolidadas/30"
      ],
      "conteudo": {
        "/regras_operacionais_v1_consolidadas/15": { "id": "RF16", "titulo": "Alteração do estado da atleta", "descricao": "O estado (ativa, lesionada, dispensada) pode ser alterado por dirigentes, coordenadores e treinadores; toda alteração é auditável." },
        "/regras_operacionais_v1_consolidadas/16": { "id": "RF17", "titulo": "Encerramento manual de vínculos e participações", "descricao": "Coordenadores e treinadores podem encerrar participações de atletas em equipes. Encerramento de vínculos de treinadores ou coordenadores exige aprovação explícita do dirigente." },
        "/regras_operacionais_v1_consolidadas/17": { "id": "RF18", "titulo": "Salvamento de rascunhos", "descricao": "O sistema permite salvar registros incompletos como rascunho; rascunhos não produzem efeitos operacionais nem analíticos." },
        "/regras_operacionais_v1_consolidadas/18": { "id": "RF19", "titulo": "Violação de regras", "descricao": "Quando uma regra é violada, o sistema alerta o usuário, permite salvar quando não estrutural e exige correção antes da efetivação." },
        "/regras_operacionais_v1_consolidadas/19": { "id": "RF20", "titulo": "Prioridade operacional", "descricao": "O sistema prioriza alertas e orientação ao usuário; bloqueios só ocorrem quando a integridade estrutural está em risco." },
        "/regras_operacionais_v1_consolidadas/20": { "id": "RF21", "titulo": "Regra suprema de decisão", "descricao": "Em conflito entre usabilidade e integridade dos dados, a integridade sempre prevalece. Regras automáticas do sistema sempre se sobrepõem à ação humana." },
        "/regras_operacionais_v1_consolidadas/21": { "id": "RF22", "titulo": "Visibilidade de rascunhos", "descricao": "Registros em rascunho são visíveis para toda a comissão técnica, não apenas para quem criou." },
        "/regras_operacionais_v1_consolidadas/22": { "id": "RF23", "titulo": "Duplicação de registros", "descricao": "O sistema permite duplicar treinos, jogos e equipes, sempre gerando um novo registro independente." },
        "/regras_operacionais_v1_consolidadas/23": { "id": "RF24", "titulo": "Notificações obrigatórias", "descricao": "Notificações críticas do sistema bloqueiam ações até serem lidas e confirmadas pelo usuário." },
        "/regras_operacionais_v1_consolidadas/24": { "id": "RF25", "titulo": "Operação offline", "descricao": "O sistema permite registro offline durante jogos, com sincronização posterior, preservando ordem temporal e integridade dos dados." },
        "/regras_operacionais_v1_consolidadas/25": { "id": "RF26", "titulo": "Versionamento visível", "descricao": "Alterações relevantes exibem versionamento visível (antes/depois), além do log técnico interno." },
        "/regras_operacionais_v1_consolidadas/26": { "id": "RF27", "titulo": "Janela de desfazer/editar", "descricao": "O usuário que realizou a ação pode editar ou desfazer por até 10 minutos. Após esse prazo, o registro é travado e apenas um superior hierárquico pode alterar, sempre com auditoria. Para treinos, aplicar também R40; para jogos, aplicar RF15." },
        "/regras_operacionais_v1_consolidadas/27": { "id": "RF28", "titulo": "Comentários e anotações livres", "descricao": "O sistema permite comentários/anotações livres em jogos, treinos e atletas; esses comentários não alteram dados estatísticos." },
        "/regras_operacionais_v1_consolidadas/28": { "id": "RF29", "titulo": "Atualização de relatórios e dashboards", "descricao": "Relatórios e dashboards refletem dados com atraso controlado, somente após validação dos registros." },
        "/regras_operacionais_v1_consolidadas/29": { "id": "RF30", "titulo": "Alertas automáticos", "descricao": "O sistema possui alertas automáticos para inconsistências de dados e riscos esportivos (ex.: excesso de carga, acúmulo disciplinar)." },
        "/regras_operacionais_v1_consolidadas/30": { "id": "RF31", "titulo": "Prioridade entre regras", "descricao": "Em qualquer conflito entre regra esportiva e regra operacional, a regra esportiva sempre prevalece automaticamente." }
      },
      "range_ids": ["RF16","RF17","RF18","RF19","RF20","RF21","RF22","RF23","RF24","RF25","RF26","RF27","RF28","RF29","RF30","RF31"],
      "approx_item_count": 16
    },
    {
      "id": "chunk-06",
      "titulo": "Domínio Esportivo (RD1-RD30)",
      "paths": [
        "/regras_dominio_esportivo_definitivas/0",
        "/regras_dominio_esportivo_definitivas/1",
        "/regras_dominio_esportivo_definitivas/2",
        "/regras_dominio_esportivo_definitivas/3",
        "/regras_dominio_esportivo_definitivas/4",
        "/regras_dominio_esportivo_definitivas/5",
        "/regras_dominio_esportivo_definitivas/6",
        "/regras_dominio_esportivo_definitivas/7",
        "/regras_dominio_esportivo_definitivas/8",
        "/regras_dominio_esportivo_definitivas/9",
        "/regras_dominio_esportivo_definitivas/10",
        "/regras_dominio_esportivo_definitivas/11",
        "/regras_dominio_esportivo_definitivas/12",
        "/regras_dominio_esportivo_definitivas/13",
        "/regras_dominio_esportivo_definitivas/14",
        "/regras_dominio_esportivo_definitivas/15",
        "/regras_dominio_esportivo_definitivas/16",
        "/regras_dominio_esportivo_definitivas/17",
        "/regras_dominio_esportivo_definitivas/18",
        "/regras_dominio_esportivo_definitivas/19",
        "/regras_dominio_esportivo_definitivas/20",
        "/regras_dominio_esportivo_definitivas/21",
        "/regras_dominio_esportivo_definitivas/22",
        "/regras_dominio_esportivo_definitivas/23",
        "/regras_dominio_esportivo_definitivas/24",
        "/regras_dominio_esportivo_definitivas/25",
        "/regras_dominio_esportivo_definitivas/26",
        "/regras_dominio_esportivo_definitivas/27",
        "/regras_dominio_esportivo_definitivas/28",
        "/regras_dominio_esportivo_definitivas/29"
      ],
      "conteudo": {
        "/regras_dominio_esportivo_definitivas/0": { "id": "RD1", "titulo": "Cálculo de idade esportiva", "descricao": "A idade da atleta é determinada pela idade no início da temporada; essa idade é referência oficial para toda a temporada." },
        "/regras_dominio_esportivo_definitivas/1": { "id": "RD2", "titulo": "Fixação de categoria na temporada", "descricao": "A categoria da atleta é definida no início da temporada e permanece inalterada até o fim da mesma." },
        "/regras_dominio_esportivo_definitivas/2": { "id": "RD3", "titulo": "Atuação em categorias superiores", "descricao": "A atleta pode atuar em categorias acima da sua, sem limite, desde que esteja vinculada às equipes correspondentes." },
        "/regras_dominio_esportivo_definitivas/3": { "id": "RD4", "titulo": "Participação em jogos", "descricao": "A atleta só pode participar de um jogo se estiver na convocação/lista oficial (o mesmo documento de autorização). Vínculo com equipe não implica participação automática." },
        "/regras_dominio_esportivo_definitivas/4": { "id": "RD5", "titulo": "Estatísticas individuais", "descricao": "As estatísticas individuais pertencem exclusivamente à atleta, acumulam ao longo da temporada e da carreira, e não são fragmentadas por equipe ou categoria." },
        "/regras_dominio_esportivo_definitivas/5": { "id": "RD6", "titulo": "Substituições e tempo de jogo", "descricao": "O sistema registra entrada e saída de atletas; esses registros compõem o tempo de participação no jogo." },
        "/regras_dominio_esportivo_definitivas/6": { "id": "RD7", "titulo": "Critério de participação oficial", "descricao": "Participação disciplinar: presença em súmula (banco + quadra). Participação estatística: tempo efetivo em quadra." },
        "/regras_dominio_esportivo_definitivas/7": { "id": "RD8", "titulo": "Validação de jogos interrompidos", "descricao": "Estatísticas só são válidas se o jogo for oficialmente validado; jogos interrompidos e não validados não geram estatísticas." },
        "/regras_dominio_esportivo_definitivas/8": { "id": "RD9", "titulo": "Empréstimo/cessão temporária", "descricao": "A atleta só pode atuar por outra equipe mediante vínculo explícito, ainda que temporário." },
        "/regras_dominio_esportivo_definitivas/9": { "id": "RD10", "titulo": "Jogos amistosos", "descricao": "Jogos amistosos geram estatísticas individuais separadas das estatísticas de jogos oficiais." },
        "/regras_dominio_esportivo_definitivas/10": { "id": "RD11", "titulo": "Posições em quadra", "descricao": "As atletas podem exercer múltiplas posições, variáveis por jogo." },
        "/regras_dominio_esportivo_definitivas/11": { "id": "RD12", "titulo": "Mudança de posição durante o jogo", "descricao": "O sistema registra mudanças de posição ao longo do jogo, preservando a sequência temporal." },
        "/regras_dominio_esportivo_definitivas/12": { "id": "RD13", "titulo": "Goleira", "descricao": "A goleira é exclusiva da posição e não atua como jogadora de linha na temporada nem no jogo; não é contabilizada como atleta de linha para minutagem tática.", "complemento_v1_1": "O sistema bloqueia o lançamento de tempo em quadra e estatísticas típicas de atleta de linha para uma goleira. RD22 (goleiro-linha) aplica-se exclusivamente a atletas de linha." },
        "/regras_dominio_esportivo_definitivas/13": { "id": "RD14", "titulo": "Capitã", "descricao": "A função de capitã não é registrada no sistema." },
        "/regras_dominio_esportivo_definitivas/14": { "id": "RD15", "titulo": "Convocação", "descricao": "Uma atleta vinculada à equipe pode não ser convocada para um jogo, sem impacto automático em vínculo ou estado." },
        "/regras_dominio_esportivo_definitivas/15": { "id": "RD16", "titulo": "Suspensão e punição", "descricao": "Suspensão/punição gera impedimento esportivo de participação; o sistema sinaliza \"Atleta Irregular\" nas telas de escalação e não bloqueia automaticamente a súmula.", "complemento_v1_1": "Lançamentos de tempo em quadra e eventos são permitidos, com alerta e flag “Atleta Irregular”. Essas estatísticas contam normalmente nos agregados (temporada/carreira), mantendo a marcação de irregularidade." },
        "/regras_dominio_esportivo_definitivas/16": { "id": "RD17", "titulo": "Acúmulo disciplinar", "descricao": "O sistema controla acúmulo de cartões/faltas e aplica impactos automáticos previstos (ex.: alertas de irregularidade), sem suspensão automática." },
        "/regras_dominio_esportivo_definitivas/17": { "id": "RD18", "titulo": "Limite de atletas por jogo", "descricao": "O sistema valida o limite máximo de 16 atletas relacionadas por jogo; relações acima do limite são bloqueadas." },
        "/regras_dominio_esportivo_definitivas/18": { "id": "RD19", "titulo": "Lesão durante o jogo", "descricao": "Lesão ocorrida em jogo altera imediatamente o estado da atleta a partir do evento, sem reescrever dados anteriores." },
        "/regras_dominio_esportivo_definitivas/19": { "id": "RD20", "titulo": "Estatísticas coletivas", "descricao": "Estatísticas coletivas da equipe são derivadas automaticamente das estatísticas individuais; não existe lançamento manual independente." },
        "/regras_dominio_esportivo_definitivas/20": { "id": "RD21", "titulo": "Sistemas defensivos", "descricao": "O sistema registra sistemas defensivos e suas variações ao longo do jogo." },
        "/regras_dominio_esportivo_definitivas/21": { "id": "RD22", "titulo": "Goleiro-linha", "descricao": "Qualquer atleta de linha pode assumir a função de goleiro-linha, com estatísticas de goleiro; é uma situação tática distinta de substituição comum.", "complemento_v1_1": "Aplica-se apenas a atletas de linha. Não se aplica a atletas registradas como goleira na temporada." },
        "/regras_dominio_esportivo_definitivas/22": { "id": "RD23", "titulo": "Tiros de 7 metros", "descricao": "Tiros de 7 metros possuem estatística específica separada." },
        "/regras_dominio_esportivo_definitivas/23": { "id": "RD24", "titulo": "Exclusão de 2 minutos", "descricao": "A exclusão de 2 minutos deve registrar o evento, controlar tempo, gerenciar retorno e refletir impacto numérico em quadra." },
        "/regras_dominio_esportivo_definitivas/24": { "id": "RD25", "titulo": "Cartão vermelho", "descricao": "O cartão vermelho encerra a participação apenas no jogo em que ocorreu." },
        "/regras_dominio_esportivo_definitivas/25": { "id": "RD26", "titulo": "Pedidos de tempo (time-out)", "descricao": "Pedidos de tempo registram o momento e a equipe solicitante." },
        "/regras_dominio_esportivo_definitivas/26": { "id": "RD27", "titulo": "Posse de bola", "descricao": "A posse de bola é inferida pelas ações; não é evento explícito independente." },
        "/regras_dominio_esportivo_definitivas/27": { "id": "RD28", "titulo": "Transições ataque-defesa", "descricao": "Transições ataque-defesa são eventos analisáveis separadamente." },
        "/regras_dominio_esportivo_definitivas/28": { "id": "RD29", "titulo": "Erros técnicos", "descricao": "Erros técnicos são registrados como estatística e geram impacto tático/disciplinar conforme regras definidas." },
        "/regras_dominio_esportivo_definitivas/29": { "id": "RD30", "titulo": "Critério de vitória", "descricao": "Em caso de empate, o sistema suporta prorrogação e tiros de 7 metros decisivos, registrando cada fase como parte do mesmo jogo." }
      },
      "range_ids": ["RD1","RD2","RD3","RD4","RD5","RD6","RD7","RD8","RD9","RD10","RD11","RD12","RD13","RD14","RD15","RD16","RD17","RD18","RD19","RD20","RD21","RD22","RD23","RD24","RD25","RD26","RD27","RD28","RD29","RD30"],
      "approx_item_count": 30
    },
    {
      "id": "chunk-07",
      "titulo": "Domínio Esportivo (RD31-RD60)",
      "paths": [
        "/regras_dominio_esportivo_definitivas/30",
        "/regras_dominio_esportivo_definitivas/31",
        "/regras_dominio_esportivo_definitivas/32",
        "/regras_dominio_esportivo_definitivas/33",
        "/regras_dominio_esportivo_definitivas/34",
        "/regras_dominio_esportivo_definitivas/35",
        "/regras_dominio_esportivo_definitivas/36",
        "/regras_dominio_esportivo_definitivas/37",
        "/regras_dominio_esportivo_definitivas/38",
        "/regras_dominio_esportivo_definitivas/39",
        "/regras_dominio_esportivo_definitivas/40",
        "/regras_dominio_esportivo_definitivas/41",
        "/regras_dominio_esportivo_definitivas/42",
        "/regras_dominio_esportivo_definitivas/43",
        "/regras_dominio_esportivo_definitivas/44",
        "/regras_dominio_esportivo_definitivas/45",
        "/regras_dominio_esportivo_definitivas/46",
        "/regras_dominio_esportivo_definitivas/47",
        "/regras_dominio_esportivo_definitivas/48",
        "/regras_dominio_esportivo_definitivas/49",
        "/regras_dominio_esportivo_definitivas/50",
        "/regras_dominio_esportivo_definitivas/51",
        "/regras_dominio_esportivo_definitivas/52",
        "/regras_dominio_esportivo_definitivas/53",
        "/regras_dominio_esportivo_definitivas/54",
        "/regras_dominio_esportivo_definitivas/55",
        "/regras_dominio_esportivo_definitivas/56",
        "/regras_dominio_esportivo_definitivas/57",
        "/regras_dominio_esportivo_definitivas/58",
        "/regras_dominio_esportivo_definitivas/59"
      ],
      "conteudo": {
        "/regras_dominio_esportivo_definitivas/30": { "id": "RD31", "titulo": "Duração do jogo", "descricao": "A duração do jogo é configurável por competição." },
        "/regras_dominio_esportivo_definitivas/31": { "id": "RD32", "titulo": "Intervalo", "descricao": "O intervalo influencia o controle de tempo e eventos." },
        "/regras_dominio_esportivo_definitivas/32": { "id": "RD33", "titulo": "Prorrogação", "descricao": "A prorrogação segue regras próprias por categoria e competição." },
        "/regras_dominio_esportivo_definitivas/33": { "id": "RD34", "titulo": "Tiros de 7m decisivos - elegibilidade", "descricao": "Todas as atletas relacionadas podem cobrar tiros de 7 metros decisivos." },
        "/regras_dominio_esportivo_definitivas/34": { "id": "RD35", "titulo": "Tiros de 7m decisivos - registro", "descricao": "O sistema registra quem cobrou e o resultado, sem impor ordem fixa." },
        "/regras_dominio_esportivo_definitivas/35": { "id": "RD36", "titulo": "Substituições durante exclusão", "descricao": "Durante exclusão de 2 minutos, substituições são permitidas normalmente, respeitando o impacto numérico." },
        "/regras_dominio_esportivo_definitivas/36": { "id": "RD37", "titulo": "Retorno da exclusão", "descricao": "O retorno da atleta excluída ocorre apenas ao término do tempo regulamentar da exclusão." },
        "/regras_dominio_esportivo_definitivas/37": { "id": "RD38", "titulo": "Acúmulo de exclusões", "descricao": "O sistema aplica automaticamente cartão vermelho após três exclusões na mesma partida." },
        "/regras_dominio_esportivo_definitivas/38": { "id": "RD39", "titulo": "Faltas ofensivas", "descricao": "Faltas ofensivas geram impacto tático automático, além do registro estatístico." },
        "/regras_dominio_esportivo_definitivas/39": { "id": "RD40", "titulo": "Vantagem", "descricao": "A aplicação de vantagem é ignorada no modelo." },
        "/regras_dominio_esportivo_definitivas/40": { "id": "RD41", "titulo": "Defesas de goleira", "descricao": "Defesas da goleira são registradas como estatística específica." },
        "/regras_dominio_esportivo_definitivas/41": { "id": "RD42", "titulo": "Rebotes", "descricao": "Rebotes não são registrados no modelo estatístico." },
        "/regras_dominio_esportivo_definitivas/42": { "id": "RD43", "titulo": "Contra-ataque", "descricao": "Contra-ataques são registrados manualmente como evento." },
        "/regras_dominio_esportivo_definitivas/43": { "id": "RD44", "titulo": "Assistência", "descricao": "Assistência possui definição rígida e padronizada no sistema." },
        "/regras_dominio_esportivo_definitivas/44": { "id": "RD45", "titulo": "Arremesso bloqueado", "descricao": "Arremesso bloqueado é ação defensiva separada." },
        "/regras_dominio_esportivo_definitivas/45": { "id": "RD46", "titulo": "Bolas perdidas", "descricao": "Bolas perdidas são registradas por tipo." },
        "/regras_dominio_esportivo_definitivas/46": { "id": "RD47", "titulo": "Recuperação de bola", "descricao": "Recuperação de bola é evento próprio, não inferido automaticamente." },
        "/regras_dominio_esportivo_definitivas/47": { "id": "RD48", "titulo": "Faltas defensivas", "descricao": "Faltas defensivas impactam o controle disciplinar automático, além do registro estatístico." },
        "/regras_dominio_esportivo_definitivas/48": { "id": "RD49", "titulo": "Tempo efetivo de jogo", "descricao": "O sistema calcula tempo efetivo em quadra por atleta, além do tempo corrido." },
        "/regras_dominio_esportivo_definitivas/49": { "id": "RD50", "titulo": "Encerramento antecipado do jogo", "descricao": "O jogo pode ser encerrado antecipadamente conforme regra da competição." },
        "/regras_dominio_esportivo_definitivas/50": { "id": "RD51", "titulo": "Tipos de jogo", "descricao": "O sistema distingue: jogo oficial, jogo amistoso, treino-jogo. Cada tipo possui tratamento estatístico próprio." },
        "/regras_dominio_esportivo_definitivas/51": { "id": "RD52", "titulo": "Convivência de jogos", "descricao": "Jogos oficiais e amistosos podem coexistir na mesma competição." },
        "/regras_dominio_esportivo_definitivas/52": { "id": "RD53", "titulo": "Mando de jogo", "descricao": "O mando de jogo não gera impacto estatístico." },
        "/regras_dominio_esportivo_definitivas/53": { "id": "RD54", "titulo": "Local do jogo", "descricao": "O local do jogo é informativo/formativo, sem impacto em regras." },
        "/regras_dominio_esportivo_definitivas/54": { "id": "RD55", "titulo": "Placar por período", "descricao": "O sistema registra placar parcial por período." },
        "/regras_dominio_esportivo_definitivas/55": { "id": "RD56", "titulo": "WO", "descricao": "Vitória por ausência (WO) é suportada." },
        "/regras_dominio_esportivo_definitivas/56": { "id": "RD57", "titulo": "Abandono de jogo", "descricao": "O sistema suporta registro de abandono de jogo." },
        "/regras_dominio_esportivo_definitivas/57": { "id": "RD58", "titulo": "Empate", "descricao": "Empates são permitidos em competições." },
        "/regras_dominio_esportivo_definitivas/58": { "id": "RD59", "titulo": "Controle do relógio", "descricao": "O relógio para automaticamente em exclusões e pedidos de tempo." },
        "/regras_dominio_esportivo_definitivas/59": { "id": "RD60", "titulo": "Tempo efetivo", "descricao": "O tempo efetivo considera apenas paralisações oficiais." }
      },
      "range_ids": ["RD31","RD32","RD33","RD34","RD35","RD36","RD37","RD38","RD39","RD40","RD41","RD42","RD43","RD44","RD45","RD46","RD47","RD48","RD49","RD50","RD51","RD52","RD53","RD54","RD55","RD56","RD57","RD58","RD59","RD60"],
      "approx_item_count": 30
    },
    {
      "id": "chunk-08",
      "titulo": "Domínio Esportivo (RD61-RD91)",
      "paths": [
        "/regras_dominio_esportivo_definitivas/60",
        "/regras_dominio_esportivo_definitivas/61",
        "/regras_dominio_esportivo_definitivas/62",
        "/regras_dominio_esportivo_definitivas/63",
        "/regras_dominio_esportivo_definitivas/64",
        "/regras_dominio_esportivo_definitivas/65",
        "/regras_dominio_esportivo_definitivas/66",
        "/regras_dominio_esportivo_definitivas/67",
        "/regras_dominio_esportivo_definitivas/68",
        "/regras_dominio_esportivo_definitivas/69",
        "/regras_dominio_esportivo_definitivas/70",
        "/regras_dominio_esportivo_definitivas/71",
        "/regras_dominio_esportivo_definitivas/72",
        "/regras_dominio_esportivo_definitivas/73",
        "/regras_dominio_esportivo_definitivas/74",
        "/regras_dominio_esportivo_definitivas/75",
        "/regras_dominio_esportivo_definitivas/76",
        "/regras_dominio_esportivo_definitivas/77",
        "/regras_dominio_esportivo_definitivas/78",
        "/regras_dominio_esportivo_definitivas/79",
        "/regras_dominio_esportivo_definitivas/80",
        "/regras_dominio_esportivo_definitivas/81",
        "/regras_dominio_esportivo_definitivas/82",
        "/regras_dominio_esportivo_definitivas/83",
        "/regras_dominio_esportivo_definitivas/84",
        "/regras_dominio_esportivo_definitivas/85",
        "/regras_dominio_esportivo_definitivas/86",
        "/regras_dominio_esportivo_definitivas/87",
        "/regras_dominio_esportivo_definitivas/88",
        "/regras_dominio_esportivo_definitivas/89",
        "/regras_dominio_esportivo_definitivas/90"
      ],
      "conteudo": {
        "/regras_dominio_esportivo_definitivas/60": { "id": "RD61", "titulo": "Prorrogação e estatísticas", "descricao": "Estatísticas da prorrogação são separadas do tempo normal." },
        "/regras_dominio_esportivo_definitivas/61": { "id": "RD62", "titulo": "Múltiplos jogos no mesmo dia", "descricao": "A atleta pode atuar em múltiplos jogos no mesmo dia; o sistema permite, emite alerta e monitora carga total, notificando coordenador e treinador." },
        "/regras_dominio_esportivo_definitivas/62": { "id": "RD63", "titulo": "Limite diário", "descricao": "Não existe limite adicional de jogos por dia além da regra de alerta de carga." },
        "/regras_dominio_esportivo_definitivas/63": { "id": "RD64", "titulo": "Banco de reservas", "descricao": "Atleta pode iniciar no banco e não entrar em quadra sem penalidade." },
        "/regras_dominio_esportivo_definitivas/64": { "id": "RD65", "titulo": "Ausência não justificada", "descricao": "Ausência não justificada gera impacto disciplinar." },
        "/regras_dominio_esportivo_definitivas/65": { "id": "RD66", "titulo": "Participação no banco", "descricao": "Estar no banco conta como participação disciplinar oficial." },
        "/regras_dominio_esportivo_definitivas/66": { "id": "RD67", "titulo": "Advertência verbal", "descricao": "Advertência verbal não é registrada." },
        "/regras_dominio_esportivo_definitivas/67": { "id": "RD68", "titulo": "Cartão amarelo", "descricao": "Cartão amarelo não gera impacto automático futuro." },
        "/regras_dominio_esportivo_definitivas/68": { "id": "RD69", "titulo": "Duplo amarelo", "descricao": "Não existe conceito de duplo amarelo." },
        "/regras_dominio_esportivo_definitivas/69": { "id": "RD70", "titulo": "Suspensão automática", "descricao": "Não existe suspensão automática por acúmulo disciplinar." },
        "/regras_dominio_esportivo_definitivas/70": { "id": "RD71", "titulo": "Defesa com os pés", "descricao": "Defesa com os pés da goleira não é estatística separada." },
        "/regras_dominio_esportivo_definitivas/71": { "id": "RD72", "titulo": "Saída da goleira", "descricao": "Saída da goleira da área não é registrada como evento." },
        "/regras_dominio_esportivo_definitivas/72": { "id": "RD73", "titulo": "Interceptação defensiva", "descricao": "Interceptação defensiva é estatística própria." },
        "/regras_dominio_esportivo_definitivas/73": { "id": "RD74", "titulo": "Bloqueio defensivo", "descricao": "Bloqueio defensivo não gera posse automática." },
        "/regras_dominio_esportivo_definitivas/74": { "id": "RD75", "titulo": "Defesa de 7m", "descricao": "Defesa de tiro de 7m é estatística distinta." },
        "/regras_dominio_esportivo_definitivas/75": { "id": "RD76", "titulo": "Arremesso após falta", "descricao": "Arremesso após falta não é tratado como situação especial." },
        "/regras_dominio_esportivo_definitivas/76": { "id": "RD77", "titulo": "Contra-ataque (arremesso)", "descricao": "Arremesso em contra-ataque possui estatística própria." },
        "/regras_dominio_esportivo_definitivas/77": { "id": "RD78", "titulo": "Gol contra", "descricao": "Gol contra é registrado no sistema." },
        "/regras_dominio_esportivo_definitivas/78": { "id": "RD79", "titulo": "Gol anulado", "descricao": "Não existe registro de gol anulado." },
        "/regras_dominio_esportivo_definitivas/79": { "id": "RD80", "titulo": "Zona de arremesso", "descricao": "O local/zona do arremesso é registrado." },
        "/regras_dominio_esportivo_definitivas/80": { "id": "RD81", "titulo": "Superioridade/inferioridade numérica", "descricao": "O sistema registra situações ativas de superioridade/inferioridade numérica." },
        "/regras_dominio_esportivo_definitivas/81": { "id": "RD82", "titulo": "Sistema ofensivo", "descricao": "Mudanças de sistema ofensivo são registradas." },
        "/regras_dominio_esportivo_definitivas/82": { "id": "RD83", "titulo": "Jogadas ensaiadas", "descricao": "Jogadas ensaiadas são identificadas como tal." },
        "/regras_dominio_esportivo_definitivas/83": { "id": "RD84", "titulo": "Marcação individual", "descricao": "Marcação individual é registrada como evento tático." },
        "/regras_dominio_esportivo_definitivas/84": { "id": "RD85", "titulo": "Estatísticas em tempo real", "descricao": "Estatísticas são calculadas em tempo real para Live-Scouting e Logs de Atividade. Relatórios, dashboards e rankings usam dados validados." },
        "/regras_dominio_esportivo_definitivas/85": { "id": "RD86", "titulo": "Correções e ranking", "descricao": "Correções estatísticas afetam rankings automaticamente." },
        "/regras_dominio_esportivo_definitivas/86": { "id": "RD87", "titulo": "Estatísticas após troca de equipe", "descricao": "Estatísticas da atleta permanecem preservadas após troca de equipe." },
        "/regras_dominio_esportivo_definitivas/87": { "id": "RD88", "titulo": "Comparação entre temporadas", "descricao": "Estatísticas são comparáveis entre temporadas diferentes." },
        "/regras_dominio_esportivo_definitivas/88": { "id": "RD89", "titulo": "Jogos de referência técnica", "descricao": "Jogos podem ser marcados como referência técnica." },
        "/regras_dominio_esportivo_definitivas/89": { "id": "RD90", "titulo": "Reset disciplinar por temporada", "descricao": "Penalidades disciplinares são resetadas ao final de cada temporada." },
        "/regras_dominio_esportivo_definitivas/90": { "id": "RD91", "titulo": "Ranking coletivo", "descricao": "O ranking coletivo é definido exclusivamente pelo saldo de gols." }
      },
      "range_ids": ["RD61","RD62","RD63","RD64","RD65","RD66","RD67","RD68","RD69","RD70","RD71","RD72","RD73","RD74","RD75","RD76","RD77","RD78","RD79","RD80","RD81","RD82","RD83","RD84","RD85","RD86","RD87","RD88","RD89","RD90","RD91"],
      "approx_item_count": 31
    },
    {
      "id": "chunk-09",
      "titulo": "Visibilidade do Perfil Atleta",
      "paths": [
        "/visibilidade_perfil_atleta"
      ],
      "conteudo": {
        "/visibilidade_perfil_atleta": {
          "itens": [
            {
              "numero": 1,
              "titulo": "Dados pessoais (próprios)",
              "pode_visualizar": [
                "Nome completo",
                "Apelido esportivo",
                "Data de nascimento",
                "Categoria da temporada",
                "Equipes vinculadas",
                "Posições registradas",
                "Foto (se existir)"
              ],
              "nao_pode_visualizar": [
                "Dados estruturais editáveis"
              ]
            },
            {
              "numero": 2,
              "titulo": "Estado esportivo",
              "pode_visualizar": [
                "Estado atual",
                "Histórico de estados"
              ],
              "nao_pode_visualizar": [
                "Justificativas médicas detalhadas",
                "Alteração do próprio estado"
              ]
            },
            {
              "numero": 3,
              "titulo": "Dados médicos e sensíveis (LGPD)",
              "pode_visualizar": [
                "Status esportivo (apta/inapta)",
                "Restrições gerais"
              ],
              "nao_pode_visualizar": [
                "CID",
                "Diagnóstico detalhado",
                "Observações médicas internas",
                "Notas confidenciais"
              ]
            },
            {
              "numero": 4,
              "titulo": "Treinos",
              "pode_visualizar": [
                "Calendário de treinos",
                "Presença",
                "Carga individual (quando liberado)",
                "Observações públicas"
              ],
              "nao_pode_visualizar": [
                "Carga planejada do grupo",
                "Avaliações internas",
                "Comparativos com outras atletas"
              ]
            },
            {
              "numero": 5,
              "titulo": "Jogos",
              "pode_visualizar": [
                "Jogos convocados",
                "Jogos não convocados (agenda)",
                "Resultado final",
                "Tempo em quadra",
                "Posição exercida",
                "Eventos pessoais"
              ],
              "nao_pode_visualizar": [
                "Anotações táticas",
                "Avaliações de outras atletas",
                "Decisões internas de escalação"
              ]
            },
            {
              "numero": 6,
              "titulo": "Estatísticas individuais",
              "pode_visualizar": [
                "Estatísticas individuais completas",
                "Evolução por jogo/temporada",
                "Comparativo consigo mesma"
              ],
              "nao_pode_visualizar": [
                "Ranking completo da equipe",
                "Estatísticas de outras atletas (exceto se liberado futuramente)"
              ]
            },
            {
              "numero": 7,
              "titulo": "Convocações e comunicação",
              "pode": [
                "Receber convocações",
                "Confirmar presença",
                "Recusar convocação com justificativa",
                "Visualizar comunicados oficiais"
              ],
              "nao_pode": [
                "Criar comunicados",
                "Responder fora do fluxo previsto"
              ]
            },
            {
              "numero": 8,
              "titulo": "Disciplina",
              "pode_visualizar": [
                "Cartões",
                "Exclusões",
                "Suspensões vigentes",
                "Histórico disciplinar pessoal"
              ],
              "nao_pode_visualizar": [
                "Regras internas de punição",
                "Histórico disciplinar de outras atletas"
              ]
            },
            {
              "numero": 9,
              "titulo": "Histórico esportivo",
              "pode_visualizar": [
                "Temporadas passadas",
                "Equipes anteriores",
                "Estatísticas históricas pessoais",
                "Mesmo após troca de equipe, mudança de categoria ou fim de temporada"
              ]
            },
            {
              "numero": 10,
              "titulo": "O que a atleta nunca vê",
              "nao_pode_visualizar": [
                "Dados de outras atletas",
                "Relatórios técnicos",
                "Dados financeiros",
                "Dados médicos detalhados",
                "Logs de auditoria",
                "Pendências administrativas",
                "Rankings estratégicos internos"
              ]
            }
          ],
          "regra_sintese_atleta": "A atleta vê tudo que diz respeito a si mesma, nada que exponha outras pessoas e nada que comprometa decisão técnica ou governança."
        }
      },
      "approx_item_count": 1
    },
    {
      "id": "chunk-10",
      "titulo": "Regras de Participação da Atleta (RP1-RP20) + Síntese",
      "paths": [
        "/regras_participacao_atleta_definitivas",
        "/regra_sintese_participacao"
      ],
      "conteudo": {
        "/regras_participacao_atleta_definitivas": [
          { "id": "RP1", "titulo": "Definição de participação", "descricao": "Participação disciplinar é definida pela presença em súmula (banco + quadra). Participação estatística exige tempo efetivo em quadra." },
          { "id": "RP2", "titulo": "Convocada sem entrada em quadra", "descricao": "Atleta convocada que não entra em quadra é participante disciplinar, mas não é participante estatística." },
          { "id": "RP3", "titulo": "Convocação obrigatória", "descricao": "Participação em jogo exige convocação/lista oficial prévia; participação sem convocação é bloqueada pelo sistema." },
          { "id": "RP4", "titulo": "Escopo da participação", "descricao": "A participação da atleta é considerada em jogos, treinos e atividades extras (avaliações, testes, captação)." },
          { "id": "RP5", "titulo": "Ausência em treino", "descricao": "Ausência em treino gera carga = 0, impacto negativo no percentual de assiduidade e reflexo nas métricas do período." },
          { "id": "RP6", "titulo": "Participação em treino", "descricao": "Toda participação em treino gera métricas esportivas obrigatórias, incluindo dados objetivos e subjetivos." },
          { "id": "RP7", "titulo": "Atleta lesionada", "descricao": "Atleta lesionada pode participar de treinos adaptados; lesão não implica exclusão automática de atividades." },
          { "id": "RP8", "titulo": "Treino adaptado", "descricao": "Treino adaptado é registrado como tipo específico de participação." },
          { "id": "RP9", "titulo": "Atleta dispensada", "descricao": "Atleta dispensada aparece nos relatórios da temporada e no histórico, mas não participa de novos eventos." },
          { "id": "RP10", "titulo": "Validação da participação", "descricao": "Toda participação registrada deve ser validada pelo Coordenador." },
          { "id": "RP11", "titulo": "Contestação de participação", "descricao": "A atleta pode contestar registros incorretos por solicitação formal ao Coordenador." },
          { "id": "RP12", "titulo": "Participação parcial", "descricao": "Participações parciais exigem registro obrigatório de tempo efetivo." },
          { "id": "RP13", "titulo": "Impacto da participação", "descricao": "A participação impacta estatísticas objetivas, avaliações internas subjetivas e relatórios esportivos/operacionais." },
          { "id": "RP14", "titulo": "Múltiplas equipes no mesmo dia", "descricao": "A atleta pode participar de múltiplas equipes no mesmo dia; o sistema permite, emite alerta e monitora carga total, notificando coordenador e treinador." },
          { "id": "RP15", "titulo": "Amistoso vs jogo oficial", "descricao": "Participações em jogos amistosos e oficiais são registradas normalmente e contam separadamente para estatísticas e índices." },
          { "id": "RP16", "titulo": "Atleta suspensa", "descricao": "Atleta suspensa pode ser relacionada, mas sua participação em quadra é irregular e o sistema sinaliza a irregularidade." },
          { "id": "RP17", "titulo": "Alerta por restrição", "descricao": "A participação é sinalizada como irregular se houver punição disciplinar ativa ou restrição médica ativa." },
          { "id": "RP18", "titulo": "Atividade sem equipe", "descricao": "A atleta pode participar de atividades sem equipe vinculada, desde que associadas à Equipe Institucional/Grupo de Avaliação." },
          { "id": "RP19", "titulo": "Dupla natureza do registro", "descricao": "Toda participação gera registro esportivo e registro administrativo." },
          { "id": "RP20", "titulo": "Mudança de equipe", "descricao": "Ao mudar de equipe, a participação passada permanece vinculada à equipe original, preservando contexto histórico." }
        ],
        "/regra_sintese_participacao": "A atleta participa quando está presente, com controle, validação e rastreabilidade, sem reescrever o passado e sem perder contexto esportivo."
      },
      "range_ids": ["RP1","RP2","RP3","RP4","RP5","RP6","RP7","RP8","RP9","RP10","RP11","RP12","RP13","RP14","RP15","RP16","RP17","RP18","RP19","RP20"],
      "approx_item_count": 21
    },
    {
      "id": "chunk-11",
      "titulo": "Configuração do Banco (RDB1-RDB14)",
      "paths": [
        "/regras_configuracao_banco_v1"
      ],
      "conteudo": {
        "/regras_configuracao_banco_v1": [
          { "id": "RDB1", "titulo": "SGBD e extensões", "descricao": "Banco PostgreSQL 17 (Neon) com extensão pgcrypto habilitada para uso de gen_random_uuid()." },
          { "id": "RDB2", "titulo": "Chaves primárias e nomes", "descricao": "PKs são UUID com default gen_random_uuid(). Constraints e índices usam nomes semânticos (pk_, fk_, ux_, ix_, ck_, trg_)." },
          { "id": "RDB3", "titulo": "Timezone e colunas temporais", "descricao": "Colunas temporais usam timestamptz em UTC; conversão e exibição são responsabilidade da UI." },
          { "id": "RDB4", "titulo": "Exclusão lógica", "descricao": "Tabelas-chave usam deleted_at + deleted_reason. deleted_reason é obrigatória quando deleted_at não é null. DELETE físico é bloqueado por trigger." },
          { "id": "RDB5", "titulo": "Auditoria imutável", "descricao": "audit_logs é append-only: apenas INSERT. UPDATE/DELETE são bloqueados por trigger. Logs registram quem, quando, ação, contexto e old/new." },
          { "id": "RDB6", "titulo": "Super Administrador único", "descricao": "Existe exatamente um Super Administrador. Unicidade garantida por índice parcial único em users (is_superadmin = true); seed inicial cria esse usuário." },
          { "id": "RDB7", "titulo": "Papéis e estados", "descricao": "Papéis são definidos em tabela de roles. Estado da atleta é validado por CHECK e possui histórico dedicado com FK." },
          { "id": "RDB8", "titulo": "Temporadas", "descricao": "Temporadas possuem start_date e end_date com CHECK start_date < end_date. Status \"ativa\" é derivado por data; sem EXCLUDE no MVP. (obrigação do backend)" },
          { "id": "RDB9", "titulo": "Vínculos e exclusividade", "descricao": "membership possui start_at/end_at e índices parciais para garantir 1 vínculo ativo por pessoa (staff) e 1 vínculo ativo por pessoa+temporada (atleta)." },
          { "id": "RDB10", "titulo": "Múltiplos vínculos de atleta", "descricao": "team_registrations usa uma linha por período ativo (start_at, end_at) por pessoa+equipe+temporada. Reativações criam novas linhas (novo UUID), sem reabrir a anterior. O backend garante que períodos não se sobreponham para a mesma pessoa+equipe+temporada. Convocações/participações referenciam a linha vigente no momento do evento.", "atualizacao_v1_1": true },
          { "id": "RDB11", "titulo": "Categorias globais", "descricao": "Categorias são globais com min_age/max_age e CHECK min_age <= max_age. Sem EXCLUDE de sobreposição no MVP." },
          { "id": "RDB12", "titulo": "Correções de estatística", "descricao": "Correções exigem admin_note obrigatório e geram log em audit_logs com old/new, sem versionamento completo." },
          { "id": "RDB13", "titulo": "Imutabilidade de jogos e treinos", "descricao": "Trigger bloqueia UPDATE em jogo finalizado. Reabertura é auditada. Treinos com mais de 24h exigem admin_note para edição." },
          { "id": "RDB14", "titulo": "Seed mínimo", "descricao": "Banco novo deve conter: org única, roles, superadmin e uma temporada. Categorias e equipe são opcionais." }
        ]
      },
      "range_ids": ["RDB1","RDB2","RDB3","RDB4","RDB5","RDB6","RDB7","RDB8","RDB9","RDB10","RDB11","RDB12","RDB13","RDB14"],
      "approx_item_count": 14
    },
    {
      "id": "chunk-12",
      "titulo": "Esquema Técnico — Temporadas",
      "paths": [
        "/esquema_tecnico/temporadas_estados_campos_transicoes"
      ],
      "conteudo": {
        "/esquema_tecnico/temporadas_estados_campos_transicoes": {
          "campos_adicionais_recomendados": [
            { "nome": "canceled_at", "tipo": "timestamptz", "descricao": "Cancelamento pré-início; ver RF5.1", "nullable": true },
            { "nome": "interrupted_at", "tipo": "timestamptz", "descricao": "Interrupção pós-início; ver RF5.2", "nullable": true }
          ],
          "status_derivado": {
            "planejada": "now < start_date AND canceled_at IS NULL",
            "ativa": "start_date <= now AND now <= end_date AND interrupted_at IS NULL AND canceled_at IS NULL",
            "interrompida": "interrupted_at IS NOT NULL AND canceled_at IS NULL",
            "cancelada": "canceled_at IS NOT NULL (somente permitido se não houver dados vinculados; ver RF5.1)",
            "encerrada": "now > end_date AND canceled_at IS NULL (independente de interrupção)"
          },
          "transicoes_permitidas": [
            { "de": "planejada", "para": "ativa", "tipo": "automatica_por_data", "detalhe": "Virada de start_date" },
            { "de": "planejada", "para": "cancelada", "tipo": "acao_administrativa_auditada", "pre_condicao": "Sem dados vinculados" },
            { "de": "ativa", "para": "interrompida", "tipo": "acao_administrativa_auditada", "observacao": "Na V1 não há retorno para ativa" },
            { "de": "interrompida", "para": "encerrada", "tipo": "automatica_por_data", "detalhe": "Virada de end_date; não há encerramento manual" },
            { "de": "ativa", "para": "encerrada", "tipo": "automatica_por_data", "detalhe": "Virada de end_date; não há encerramento manual" }
          ],
          "efeitos_operacionais_por_estado": {
            "interrompida": "Bloqueia criação/edição de novos eventos a partir de interrupted_at; cancela jogos futuros (status “cancelado”/deleted_reason apropriado); vínculos continuam válidos no histórico; dashboards não recebem novos dados dessa temporada após a interrupção.",
            "cancelada": "Temporada fica inelegível para operação; objetos ligados a ela permanecem em histórico apenas se existirem (idealmente, cancelamento só ocorre sem dados; ver RF5.1); nada produz efeito operacional/analítico."
          }
        }
      },
      "approx_item_count": 1
    },
    {
      "id": "chunk-13",
      "titulo": "Esquema Técnico — Jogos",
      "paths": [
        "/esquema_tecnico/jogos_triggers_bloqueio_reabertura"
      ],
      "conteudo": {
        "/esquema_tecnico/jogos_triggers_bloqueio_reabertura": {
          "estados_de_jogo": [
            "rascunho",
            "em_revisao",
            "finalizado"
          ],
          "trigger_bloqueio_TRG_games_block_update_finalized": {
            "regra": "Bloqueia qualquer UPDATE em jogos com status=finalizado.",
            "excecao": "Permitir UPDATE que altere exclusivamente o status de finalizado -> em_revisao, quando a ação for do Coordenador/Dirigente, com audit_log obrigatório (acao=game_reopen, actor_id, timestamp, old/new)."
          },
          "reabertura": {
            "operacao": "set status=em_revisao; registrar audit_log “game_reopen”.",
            "efeito": "Estatísticas deixam de alimentar dashboards/rankings até nova finalização (conforme RD85/RF29).",
            "edits_permitidos": "Enquanto em_revisao, o registro permite atualizações e correções (R23/R24), todas auditadas."
          },
          "nova_finalizacao": {
            "operacao": "set status=finalizado; registrar audit_log “game_finalize”; reativar trigger de bloqueio.",
            "efeito": "Dashboards/rankings passam a refletir o jogo novamente quando finalizado."
          },
          "exclusao_logica": {
            "operacao": "set deleted_at + deleted_reason (obrigatório); registrar audit_log “game_soft_delete”; permanece não editável; visível somente em histórico."
          }
        }
      },
      "approx_item_count": 1
    },
    {
      "id": "chunk-14",
      "titulo": "Organização por Camada de Configuração",
      "paths": [
        "/organizacao_regras_por_camada_de_configuracao"
      ],
      "conteudo": {
        "/organizacao_regras_por_camada_de_configuracao": {
          "apenas_no_db": {
            "R": ["R4", "R20", "R29", "R35"],
            "RDB": ["RDB1", "RDB2", "RDB3", "RDB4", "RDB5", "RDB6", "RDB7", "RDB8", "RDB9", "RDB10", "RDB11", "RDB12", "RDB13", "RDB14"]
          },
          "db_backend": {
            "R": ["R1", "R2", "R3", "R5", "R6", "R7", "R8", "R11", "R12", "R13", "R15", "R16", "R17", "R19", "R23", "R24", "R25", "R28", "R30", "R31", "R32", "R33", "R34", "R37", "R38", "R39"],
            "RF": ["RF2"],
            "RDB": []
          },
          "apenas_backend": {
            "R": ["R10", "R21", "R22", "R26", "R27", "R36", "R43"],
            "RF": ["RF5", "RF21", "RF31"],
            "RD": ["RD1", "RD2", "RD3", "RD5", "RD7", "RD8", "RD9", "RD10", "RD14", "RD15", "RD18", "RD20", "RD27", "RD30", "RD33", "RD34", "RD38", "RD40", "RD42", "RD49", "RD50", "RD51", "RD52", "RD53", "RD54", "RD58", "RD60", "RD61", "RD63", "RD64", "RD66", "RD67", "RD68", "RD69", "RD70", "RD71", "RD72", "RD74", "RD76", "RD79", "RD86", "RD87", "RD88", "RD90", "RD91"],
            "RP": ["RP1", "RP2", "RP4", "RP5", "RP6", "RP9", "RP13", "RP15", "RP19", "RP20"],
            "sintese": ["Regra-síntese de participação"]
          },
          "backend_frontend": {
            "R": ["R9", "R14", "R18", "R40", "R41", "R42"],
            "RF": ["RF1", "RF3", "RF4", "RF6", "RF7", "RF8", "RF9", "RF10", "RF11", "RF12", "RF13", "RF14", "RF15", "RF16", "RF17", "RF18", "RF19", "RF20", "RF22", "RF23", "RF24", "RF25", "RF26", "RF27", "RF28", "RF29", "RF30"],
            "RD": ["RD4", "RD6", "RD11", "RD12", "RD13", "RD16", "RD17", "RD19", "RD21", "RD22", "RD23", "RD24", "RD25", "RD26", "RD28", "RD29", "RD31", "RD32", "RD35", "RD36", "RD37", "RD39", "RD41", "RD43", "RD44", "RD45", "RD46", "RD47", "RD48", "RD55", "RD56", "RD57", "RD59", "RD62", "RD65", "RD73", "RD75", "RD77", "RD78", "RD80", "RD81", "RD82", "RD83", "RD84", "RD85", "RD89"],
            "RP": ["RP3", "RP7", "RP8", "RP10", "RP11", "RP12", "RP14", "RP16", "RP17", "RP18"],
            "visibilidade_perfil_atleta": ["Itens 1 a 10", "Regra-síntese (Atleta)"]
          },
          "apenas_front": {
            "observacao": "Nenhuma"
          }
        }
      },
      "approx_item_count": 1
    }
  ]
}

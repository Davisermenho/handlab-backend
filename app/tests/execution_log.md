# Execution Log — Ações realizadas no backend

Data: 2025-12-14

Objetivo:
- Registrar as mudanças feitas no repositório para preparar a Fase 3 (ORM, schemas, rotas e testes).

Ações (arquivos criados/alterados) e motivo:

- `sql/schema.sql` — criado
  - Contém os comandos SQL para criar as tabelas `usuarios`, `equipes`, `atletas`, `presencas`, `videos`.
  - Motivo: versionar o esquema SQL do MVP conforme as instruções.

- `config.py` — atualizado
  - Agora exporta `engine`, `SessionLocal` e `Base` (SQLAlchemy session factory e declarative base).
  - Motivo: permitir uso consistente do ORM e das sessões em `models.py` e rotas.

- `models.py` — criado
  - Implementa os modelos SQLAlchemy: `Usuario`, `Equipe`, `Atleta`, `Presenca`, `Video`.
  - Motivo: mapear o esquema SQL para ORM e possibilitar operações via SQLAlchemy.

- `schemas.py` — criado
  - Contém classes Pydantic (Create/Out) para as entidades; atualizado para Pydantic v2 (`model_config = {"from_attributes": True}`).
  - Motivo: validação de entrada/saída nas rotas FastAPI.

- `routes/` — criado (arquivos)
  - `routes/usuario.py`, `routes/equipe.py`, `routes/atleta.py`, `routes/presenca.py`, `routes/video.py`
  - Cada arquivo implementa CRUD (POST/GET/PUT/DELETE) usando dependência `get_db()` que provê `SessionLocal`.
  - Motivo: implementar endpoints iniciais do MVP.

- `main.py` — atualizado
  - Inclui os routers criados e mantém rota `/ping-banco` para checagem de conexão.
  - Motivo: registrar rotas no app FastAPI.

- `check_db.py` e `.vscode/testedb/check_db.py` — criados
  - Scripts para inspecionar o banco e garantir que as tabelas esperadas existem.
  - Motivo: verificação rápida de integridade do esquema no Neon/Postgres.

- `tests/api_test.py` — criado
  - Script de teste que realiza chamadas HTTP contra o servidor local para verificar fluxo CRUD de `Usuario`, `Equipe` e `Atleta`.
  - Motivo: validação automática das rotas durante desenvolvimento.

- `tests/test_log.md` e `tests/execution_log.md` — criados (este arquivo)
  - Documentam resultados dos testes e histórico de ações.

Comandos executados durante verificação (exemplos):

```bat
.venv\Scripts\activate
uvicorn main:app --reload
python tests\api_test.py
python .vscode\testedb\check_db.py
```

Observações e próximos passos recomendados:
- Adicionar `.env.example` ao repositório (sem credenciais reais).
- Migrar para testes `pytest` com asserts formais e fixtures (isolamento do DB — usar transação/rollback ou banco de teste).
- Considerar Alembic para versão de migrações do schema.

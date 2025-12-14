# Test Log — Integração API (FastAPI)

Data: 2025-12-14

Objetivo:
- Documentar os testes de integração que exercitam os endpoints CRUD para `Usuario`, `Equipe` e `Atleta`.

Ambiente:
- Servidor local: http://127.0.0.1:8000 (uvicorn main:app --reload)
- Venv: `.venv` (Python usado: `.venv\Scripts\python.exe`)
- Script de teste: `tests/api_test.py`

Nota importante:
- Todos os testes automatizados devem residir em `/app/tests` (mover ou manter scripts de teste nessa pasta).
- Não adicionar novos arquivos de teste fora de `/app/tests` para manter padrão de organização.

Resumo dos testes executados:

- Usuario CRUD
  - POST /usuarios/ — cria usuário
    - Payload exemplo: {"nome":"Teste","email":"teste@example.com","senha":"senha","papel":"atleta"}
    - Validação: resposta 200 com objeto contendo `id`, `nome`, `email`, `papel`, `data_cadastro`.
    - Exemplo de saída verificada: `{'id': 1, 'nome': 'Teste', 'email': 'teste@example.com', 'papel': 'atleta', 'data_cadastro': '2025-12-14T05:10:21.551637'}`

  - GET /usuarios/ — lista
    - Validação: lista contém o usuário criado.

  - GET /usuarios/{id} — detalha
    - Validação: retorna o objeto com `id` correto.

  - PUT /usuarios/{id} — atualiza
    - Payload de atualização exemplo: {"nome":"Teste2","email":"teste2@example.com","senha":"nova","papel":"atleta"}
    - Validação: resposta 200 com campos atualizados (ex.: `nome` e `email`).

  - DELETE /usuarios/{id}
    - Validação: resposta com `{"ok": True}` e recurso removido.

- Equipe & Atleta CRUD (fluxo integrado)
  - Criar treinador (usuário com `papel`="treinador").
  - POST /equipes/ — cria equipe vinculada ao treinador.
    - Exemplo: `{'id': 1, 'nome': 'Equipe A', 'categoria': 'juvenil', 'treinador_id': 2}`
  - POST /atletas/ — cria atleta vinculado à equipe.
    - Exemplo: `{'id': 1, 'nome': 'Atleta1', 'email': 'atleta1@example.com', 'nascimento': '2005-01-01', 'posicao': 'ala', 'equipe_id': 1}`
  - GET/PUT/DELETE aplicados para equipe e atleta; validações: status 200 e objetos coerentes.

Resultados (resumo):
- Todos os endpoints CRUD testados retornaram status 200 e payloads conforme esperado.
- Check de esquema no banco confirmou as tabelas esperadas (ver `check_db.py`).

Comandos para reproduzir os testes:

```bat
.venv\Scripts\activate
uvicorn main:app --reload
python tests\api_test.py
python .vscode\testedb\check_db.py
```

Observações:
- Os testes usam JSON simples e validam apenas contratos básicos (status e presença de campos). Para testes mais robustos, integrar `pytest` + fixtures e asserts detalhados.

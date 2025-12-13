# Hand Lab - Backend

Este é o backend do projeto **Hand Lab**, implementado com [FastAPI](https://fastapi.tiangolo.com/) e persistência em PostgreSQL (Neon.tech).

## Funcionalidades

- API REST para cadastro e autenticação de atletas e treinadores
- Gerenciamento de equipes
- Registro de presença em treinos/jogos
- Upload de vídeos (armazenamento em cloud)
- Autenticação com JWT e permissões básicas por perfil

## Como rodar localmente

1. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
   ```

2. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn python-dotenv psycopg2-binary sqlalchemy passlib[bcrypt] python-jose[cryptography]
   ```

3. **Configure o banco (Neon/Postgres) e o arquivo `.env` com as variáveis de conexão.**

4. **Rode o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa:**  
   http://localhost:8000/docs

---

*Mais detalhes de endpoints e modelos serão adicionados com a evolução do projeto.*
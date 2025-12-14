-- Tabela de atletas
CREATE TABLE atletas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    nascimento DATE,
    posicao VARCHAR(50),
    equipe_id INTEGER REFERENCES equipes(id)
);
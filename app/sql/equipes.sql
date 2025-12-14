-- Tabela de equipes
CREATE TABLE equipes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    treinador_id INTEGER REFERENCES usuarios(id)
);
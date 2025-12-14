-- Tabela de presenças
CREATE TABLE presencas (
    id SERIAL PRIMARY KEY,
    atleta_id INTEGER REFERENCES atletas(id),
    equipe_id INTEGER REFERENCES equipes(id),
    data DATE,
    tipo VARCHAR(20),      -- treino ou jogo
    presente BOOLEAN,
    obs VARCHAR(140)
);
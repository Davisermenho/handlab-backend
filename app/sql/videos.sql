-- Tabela de vídeos
CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    equipe_id INTEGER REFERENCES equipes(id),
    atleta_id INTEGER REFERENCES atletas(id),
    criado_em TIMESTAMP DEFAULT NOW()
);
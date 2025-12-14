from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.config import Base
import datetime


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    papel = Column(String(20), nullable=False)
    data_cadastro = Column(DateTime, default=datetime.datetime.utcnow)

    equipes = relationship("Equipe", back_populates="treinador")


class Equipe(Base):
    __tablename__ = "equipes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50))
    treinador_id = Column(Integer, ForeignKey('usuarios.id'))

    treinador = relationship("Usuario", back_populates="equipes")
    atletas = relationship("Atleta", back_populates="equipe")


class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    nascimento = Column(Date)
    posicao = Column(String(50))
    equipe_id = Column(Integer, ForeignKey('equipes.id'))

    equipe = relationship("Equipe", back_populates="atletas")


class Presenca(Base):
    __tablename__ = "presencas"

    id = Column(Integer, primary_key=True, index=True)
    atleta_id = Column(Integer, ForeignKey('atletas.id'))
    equipe_id = Column(Integer, ForeignKey('equipes.id'))
    data = Column(Date)
    tipo = Column(String(20))
    presente = Column(Boolean)
    obs = Column(String(140))


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, nullable=False)
    equipe_id = Column(Integer, ForeignKey('equipes.id'))
    atleta_id = Column(Integer, ForeignKey('atletas.id'))
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)
from sqlalchemy import Column, Integer, String, Date, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.config import Base
import datetime

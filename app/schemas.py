from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    papel: str


class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    papel: str
    data_cadastro: datetime
    model_config = {"from_attributes": True}


class EquipeCreate(BaseModel):
    nome: str
    categoria: Optional[str] = None
    treinador_id: Optional[int] = None


class EquipeOut(BaseModel):
    id: int
    nome: str
    categoria: Optional[str]
    treinador_id: Optional[int]
    model_config = {"from_attributes": True}


class AtletaCreate(BaseModel):
    nome: str
    email: EmailStr
    nascimento: Optional[date] = None
    posicao: Optional[str] = None
    equipe_id: Optional[int] = None


class AtletaOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    nascimento: Optional[date]
    posicao: Optional[str]
    equipe_id: Optional[int]
    model_config = {"from_attributes": True}


class PresencaCreate(BaseModel):
    atleta_id: int
    equipe_id: int
    data: date
    tipo: Optional[str] = None
    presente: Optional[bool] = None
    obs: Optional[str] = None


class PresencaOut(BaseModel):
    id: int
    atleta_id: int
    equipe_id: int
    data: date
    tipo: Optional[str]
    presente: Optional[bool]
    obs: Optional[str]
    model_config = {"from_attributes": True}


class VideoCreate(BaseModel):
    url: str
    equipe_id: int
    atleta_id: Optional[int] = None


class VideoOut(BaseModel):
    id: int
    url: str
    equipe_id: int
    atleta_id: Optional[int]
    criado_em: datetime
    model_config = {"from_attributes": True}
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    papel: str


class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    papel: str
    data_cadastro: datetime
    model_config = {"from_attributes": True}


class EquipeCreate(BaseModel):
    nome: str
    categoria: Optional[str] = None
    treinador_id: Optional[int] = None


class EquipeOut(BaseModel):
    id: int
    nome: str
    categoria: Optional[str]
    treinador_id: Optional[int]
    model_config = {"from_attributes": True}


class AtletaCreate(BaseModel):
    nome: str
    email: EmailStr
    nascimento: Optional[date] = None
    posicao: Optional[str] = None
    equipe_id: Optional[int] = None


class AtletaOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    nascimento: Optional[date]
    posicao: Optional[str]
    equipe_id: Optional[int]
    model_config = {"from_attributes": True}


class PresencaCreate(BaseModel):
    atleta_id: int
    equipe_id: int
    data: date
    tipo: Optional[str] = None
    presente: Optional[bool] = None
    obs: Optional[str] = None


class PresencaOut(BaseModel):
    id: int
    atleta_id: int
    equipe_id: int
    data: date
    tipo: Optional[str]
    presente: Optional[bool]
    obs: Optional[str]
    model_config = {"from_attributes": True}


class VideoCreate(BaseModel):
    url: str
    equipe_id: int
    atleta_id: Optional[int] = None


class VideoOut(BaseModel):
    id: int
    url: str
    equipe_id: int
    atleta_id: Optional[int]
    criado_em: datetime
    model_config = {"from_attributes": True}

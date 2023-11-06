from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Votos(Base):
    __tablename__ = 'votos'

    id_voto = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    lista = Column(String(255), nullable=False)
    partido = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Votos {self.eleccion} -> {self.lista} {self.partido} -> {self.timestamp}>"

class MensajeEncriptado(BaseModel):
    voto: dict
    token: str

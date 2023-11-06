from fastapi import APIRouter, HTTPException, Response
from layers.database.sqlalchemy.models import Votos, MensajeEncriptado
from votechain_core.stacks.votestamp import votestamp, sql_add
from datetime import datetime
import os


voteregister = APIRouter()

db_session = votestamp.db_session

# Ruta para recibir votos a través de una solicitud POST
@voteregister.post('/registrar_voto', response_model=dict)
def registrar_voto(message: MensajeEncriptado):
    try:
        
        if message.token != os.getenv("SECRET-TOKEN"):
            return Response(content='Token de autenticación inválido', status_code=400)
        
        fecha_actual = datetime.now().replace(microsecond=0)
        fecha_limite_inferior = datetime.strptime(os.getenv("FECHA_LIMITE_INFERIOR"), "%Y-%m-%d %H:%M:%S")
        fecha_limite_superior = datetime.strptime(os.getenv("FECHA_LIMITE_SUPERIOR"), "%Y-%m-%d %H:%M:%S")

        # Validar la hora de acceso aquí
        if fecha_actual < fecha_limite_inferior:
            return Response(content=f'El horario de votación todavía no ha comenzado. Comenzará el {str(fecha_limite_inferior)}', status_code=308)

        if fecha_actual > fecha_limite_superior:
            return Response(content=f'El horario de votación ya ha vencido. La fecha límite era {str(fecha_limite_superior)}', status_code=308)

        voto = Votos(
            timestamp=fecha_actual,
            lista=message.voto.get("lista"),
            partido=message.voto.get("partido")
        )
        sql_add(db_session, voto)
        return Response(content='Voto registrado con éxito', status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
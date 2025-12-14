from fastapi import FastAPI
from config.config import engine
from app.routes.usuario import router as usuario_router
from app.routes.equipe import router as equipe_router
from app.routes.atleta import router as atleta_router
from app.routes.presenca import router as presenca_router
from app.routes.video import router as video_router

app = FastAPI()

@app.get("/ping-banco")
def ping_banco():
    with engine.connect() as conn:
        conn.execute("SELECT 1")
    return {"ok": "Conexão com o banco funcionando!"}


app.include_router(usuario_router)
app.include_router(equipe_router)
app.include_router(atleta_router)
app.include_router(presenca_router)
app.include_router(video_router)


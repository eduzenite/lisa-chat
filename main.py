from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="My AI Project")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API de IA iniciada!"}

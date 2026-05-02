from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "AI Builder OS ativo",
        "message": "Backend a funcionar corretamente 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "system": "online"
    }

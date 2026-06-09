from fastapi import FastAPI
from api.paper_routes import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Research Synthesis Engine"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

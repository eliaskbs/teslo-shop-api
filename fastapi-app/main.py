from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from database import engine, Base
from routers import products, seed, files

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Teslo Shop API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(seed.router, prefix="/api/seed", tags=["seed"])
app.include_router(files.router, prefix="/api/files", tags=["files"])


@app.get("/")
def root():
    return {"message": "Teslo Shop API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True,
    )

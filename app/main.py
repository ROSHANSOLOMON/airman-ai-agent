from fastapi import FastAPI

from app.api.ingest import router as ingest_router
from app.api.eval import router as eval_router

from app.db.database import engine
from app.db import models


app = FastAPI(title="AIRMAN AI Agent")

# create tables
models.Base.metadata.create_all(bind=engine)

# include routers
app.include_router(ingest_router)
app.include_router(eval_router)


@app.get("/")
def health():
    return {"status": "running"}
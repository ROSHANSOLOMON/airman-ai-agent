from fastapi import FastAPI

app = FastAPI(title="AIRMAN AI Agent")

@app.get("/")
def health():
    return {"status": "running"}
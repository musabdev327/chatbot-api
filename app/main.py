from fastapi import FastAPI
import uvicorn

app = FastAPI()

from .router import chat, health

app.include_router(health.router)
app.include_router(chat.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

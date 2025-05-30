from typing import Optional
from fastapi import FastAPI

from views.account import router as account_router
from views.code import router as code_router
from views.file import router as file_router
from views.board import router as board_router

from config.settings import server_settings
from middlewares import cors_config, static_config


app = FastAPI(
    title="CRM Backend API",
    description="CRM Backend API Documentation",
    version="1.0.0",
)

cors_config.add(app)
static_config.add(app)

app.include_router(account_router)
app.include_router(code_router)
app.include_router(file_router)
app.include_router(board_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Backend API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

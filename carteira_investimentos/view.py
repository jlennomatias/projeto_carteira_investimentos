from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from carteira_investimentos.routers import carteira_routers, user_routers, operacao_routers


app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_routers.router)
app.include_router(carteira_routers.router)
app.include_router(operacao_routers.router)

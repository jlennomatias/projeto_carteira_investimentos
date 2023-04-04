from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


# Definindo as variaveis de configuração
SECRET_KEY = "chave-secreta" #Chave de assinatura do token, isso garante que o token não foi alterado
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# # Para verificar se a senha do usuário é válida
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# Para gerar o token JWT
def create_access_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

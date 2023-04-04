from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from carteira_investimentos.controllers.crud.user_controllers import UserService
from carteira_investimentos.controllers.security.auth import SECRET_KEY, ALGORITHM


# Criando uma instancia de Oauth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


# Para decodificar o token JWT
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    nome = payload.get("nome")
    if nome is None:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    user = UserService.get_username(nome)

    if user is None:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return user
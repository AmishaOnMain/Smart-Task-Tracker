from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt 

from app.config.settings import settings 


from fastapi import HTTPException, status

def create_access_token(user_id: int):
  expire = datetime.now(timezone.utc)+ timedelta(

    minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES
  )

  payload={

    "sub": str(user_id),

    "exp": expire
  }

  encoded_jwt=jwt.encode(

    payload,
    settings.SECRET_KEY,
    algorithm= settings.ALGORITHM
  )

  return encoded_jwt

def verify_access_token(token:str):

  try:

    payload=jwt.decode(

      token,
      settings.SECRET_KEY,
      algorithms= [settings.ALGORITHM]
    )

    return payload 
  except JWTError:

    return HTTPException(
    status_code=401,
    detail="Invalid token"
)
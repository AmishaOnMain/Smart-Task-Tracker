from pydantic import BaseModel


class GoogleLoginRequest(BaseModel):
    id_token: str

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

    user_id: int
    name: str
    email: str
    profile_picture: str | None
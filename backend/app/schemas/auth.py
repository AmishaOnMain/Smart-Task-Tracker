from pydantic import BaseModel, ConfigDict


class GoogleLoginRequest(BaseModel):
    id_token: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    profile_picture: str | None

    model_config = ConfigDict(from_attributes=True)


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

    user: UserResponse
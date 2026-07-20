from sqlalchemy.orm import Session

from app.auth.google import verify_google_token
from app.auth.jwt import create_access_token
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def google_login(db: Session, id_token: str):

        google_user = verify_google_token(id_token)

        user = UserRepository.get_by_google_id(
            db,
            google_user["google_id"],
        )

        if not user:
            user = UserRepository.create_user(
                db=db,
                google_id=google_user["google_id"],
                name=google_user["name"],
                email=google_user["email"],
                profile_picture=google_user.get("profile_picture"),
            )

        access_token = create_access_token(
            {"sub": str(user.id)}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "profile_picture": user.profile_picture,
        }
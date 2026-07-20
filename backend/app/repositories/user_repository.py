from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_google_id(db: Session, google_id: str):
        return (
            db.query(User)
            .filter(User.google_id == google_id)
            .first()
        )

    @staticmethod
    def get_by_email(db: Session, email: str):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        google_id: str,
        name: str,
        email: str,
        profile_picture: str | None,
    ):
        user = User(
            google_id=google_id,
            name=name,
            email=email,
            profile_picture=profile_picture,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
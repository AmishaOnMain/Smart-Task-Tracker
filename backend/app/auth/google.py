from google.auth.transport import requests
from google.oauth2 import id_token

from app.config.settings import settings

def verify_google_token(token: str):
    """
    Verify Google's ID token and return user information.
    """

    try:
        user_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            settings.GOOGLE_CLIENT_ID,
        )

        return user_info

    except ValueError:
        return None
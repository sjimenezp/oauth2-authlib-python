class Config:
    import os

    SECRET_KEY = os.getenv("FLASK_SECRET")
    TEST_WEB_APP_CLIENT_ID = os.getenv(
        "OAUTH2_CLIENT_ID"
    )  # Loaded automatically by the OAuth library
    TEST_WEB_APP_CLIENT_SECRET = os.getenv(
        "OAUTH2_CLIENT_SECRET"
    )  # Loaded automatically by the OAuth library
    OAUTH2_ISSUER = os.getenv("OAUTH2_ISSUER")

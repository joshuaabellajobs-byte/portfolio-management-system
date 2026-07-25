from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    # Project
    PROJECT_NAME = "Portfolio Management System"

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    # JWT Authentication
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "Qv8mX2pL9nRw4ZaHf7TyKs3NcJd6BgEeUp5Vx1Lm8AsQz4CrWt9Hy2FnPb7GkMdX"
    )

    ALGORITHM = os.getenv("ALGORITHM", "HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )

settings = Settings()
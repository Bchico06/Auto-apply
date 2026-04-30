import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./autoapply.db")
JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 60 * 24

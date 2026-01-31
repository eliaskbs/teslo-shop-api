from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "teslo_shop"
    db_username: str = "postgres"
    db_password: str = "postgres"
    host_api: str = "http://localhost:8000"
    port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

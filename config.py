from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    Token:str
    WeatherToken: str
    Units: str
    
    class Config:
        env_file='.env'
        
settings = Settings()
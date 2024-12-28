from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE_PATH = ".env"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, env_ignore_empty=True)

    BITGET_API_KEY: str = ""
    BITGET_API_SECRET: str = ""
    BITGET_API_PASSPHRASE: str = ""

    OKX_API_KEY: str = ""
    OKX_API_SECRET: str = ""
    OKX_API_PASSPHRASE: str = ""

    PROXY_STR: str = ""


settings = Settings()
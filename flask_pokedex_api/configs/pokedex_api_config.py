from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    POKEDEX_API_HOST: str
    POKEDEX_API_PORT: int
    # POKEDEX_API_SPEC_ROUTE: str


def get_api_config() -> ApiSettings:
    return ApiSettings()

from pydantic import BaseSettings


class PokeapiSettings(BaseSettings):
    POKEAPI_IP: str


def get_pokeapi_ip() -> PokeapiSettings:
    return PokeapiSettings()

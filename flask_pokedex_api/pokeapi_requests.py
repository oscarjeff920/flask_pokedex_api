import typing

import requests

from flask_pokedex_api.configs.pokeapi_config import get_pokeapi_ip
from flask_pokedex_api.pokedex_schema import PokedexBase


def get_pokedata(poke_name: str) -> typing.Dict:
    ip = get_pokeapi_ip().POKEAPI_IP

    try:
        response = requests.get("{}{}".format(ip, poke_name.lower()))
        if response.status_code == 404:
            return {"HTTP Error: 404. Pokemon Not Found": "Check Spelling"}
        response.raise_for_status()
    except requests.exceptions.HTTPError as httperr:
        raise httperr
    except requests.exceptions.ConnectionError as conerr:
        raise conerr
    except requests.exceptions.RequestException as reqerr:
        raise reqerr

    details = response.json()
    return PokedexBase(
        name=poke_name,
        description=english_description(details.get("flavor_text_entries", {})),
        habitat=details.get("habitat").get("name")
        if details.get("habitat") is not None
        else "Unknown",
        isLegendary=details.get("is_legendary", {}),
    ).dict()


def english_description(descriptions: typing.List) -> str:
    for entry in descriptions:
        if entry.get("language").get("name") == "en":
            return entry.get("flavor_text").replace("\n", " ").replace("\u000c", " ")
    else:
        return "*NOTFOUND*"

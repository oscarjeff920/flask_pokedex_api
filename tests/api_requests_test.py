import typing

from flask_pokedex_api.configs.pokedex_api_config import get_api_config
import requests


def api_requests_test() -> typing.Dict:
    BASE = (
        "http://"
        + get_api_config().POKEDEX_API_HOST
        + ":"
        + str(get_api_config().POKEDEX_API_PORT)
        + "/"
    )
    endpoint = "pokedex/pikachu"

    try:
        response = requests.get(BASE + endpoint)
    except requests.exceptions.HTTPError as httperr:
        raise httperr
    except requests.exceptions.ConnectionError as conerr:
        raise conerr
    except requests.exceptions.RequestException as reqerr:
        raise reqerr

    return response.json()


if __name__ == "__main__":
    print(api_requests_test())

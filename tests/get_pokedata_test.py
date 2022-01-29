from flask_pokedex_api.pokeapi_requests import get_pokedata


def pokedata_test() -> None:
    pokemon = get_pokedata(poke_name="mew")
    print(pokemon)


if __name__ == "__main__":
    pokedata_test()

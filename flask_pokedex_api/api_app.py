import typing

from flask import Flask
from flask_restful import Api, Resource

from flask_pokedex_api.pokeapi_requests import get_pokedata
from flask_pokedex_api.pokedex_schema import PokedexBase

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self) -> typing.Dict:
        return dict(about="An API to receive pokemon data from pokeapi.co")


class PokeRequest(Resource):
    def get(self, pokemon_name: str) -> PokedexBase:
        return get_pokedata(poke_name=pokemon_name)


api.add_resource(Home, "/")
api.add_resource(PokeRequest, "/pokedex/<string:pokemon_name>")

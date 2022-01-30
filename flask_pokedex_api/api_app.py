import typing

from flask import Flask
from flask_restful import Api, Resource

from flask_pokedex_api.pokeapi_requests import get_pokedata

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self) -> typing.Dict:
        return dict(about="An API to receive pokemon data from 'pokeapi.co'")


class PokeRequest(Resource):
    def get(self, poke_name: str) -> typing.Dict:
        return get_pokedata(poke_name=poke_name)


class PokedexHome(Resource):
    def get(self) -> str:
        return "enter a pokemon name into the url after 'pokedex/'"


api.add_resource(Home, "/")
api.add_resource(PokedexHome, "/pokedex", "/pokedex/")
api.add_resource(
    PokeRequest, "/pokedex/<string:poke_name>", "/pokedex/<string:poke_name>/"
)

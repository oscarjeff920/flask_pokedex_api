from flask import Flask
from flask_restful import Api

from flask_pokedex_api.configs.pokedex_api_config import get_api_config

app = Flask(__name__)
api = Api(Flask)

if __name__ == "__main__":
    api_settings = get_api_config()
    app.run(
        debug=True,
        host=api_settings.POKEDEX_API_HOST,
        port=api_settings.POKEDEX_API_PORT,
    )

from flask_pokedex_api.api_app import app
from flask_pokedex_api.configs.pokedex_api_config import get_api_config


if __name__ == "__main__":
    api_settings = get_api_config()

    app.run(
        debug=True,
        host=api_settings.POKEDEX_API_HOST,
        port=api_settings.POKEDEX_API_PORT,
    )

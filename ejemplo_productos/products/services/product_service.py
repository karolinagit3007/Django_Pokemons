import requests

from products.models import Pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemons():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["results"]
    return []

def get_pokemon(id):
    response = requests.get(f"{API_URL}{id}")
    if response.status_code == 200:
        return response.json()
    return {}

def load_pokemons():
    if not Pokemon.objects.exists():
        pokemons = get_pokemons()
        for pokemon in pokemons:
            pokemon_data = get_pokemon(pokemon["name"])
            Pokemon.objects.create(
                name=pokemon_data["name"],
                type=pokemon_data["types"][0]["type"]["name"],  # Tomamos el primer tipo
                image=pokemon_data["sprites"]["front_default"],
                abilities=", ".join([ability["ability"]["name"] for ability in pokemon_data["abilities"]]),
                height=pokemon_data["height"],
                weight=pokemon_data["weight"],
            )
        return f"{len(pokemons)} Pokémon cargados"
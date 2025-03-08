import requests
from products.models import Pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemons(url=API_URL):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"results": []}


def get_pokemon(name):
    response = requests.get(f"{API_URL}{name}")
    if response.status_code == 200:
        return response.json()
    return {}


def load_pokemons():
    if Pokemon.objects.count() >= 1025:  
        print("✅ Todos los Pokémon ya están en la base de datos.")
        return

    pokemons = get_pokemons()  # Obtiene la lista de Pokémon

    for pokemon in pokemons:
        pokemon_data = get_pokemon(pokemon["name"])
        if pokemon_data:
            Pokemon.objects.get_or_create(
                name=pokemon_data["name"].capitalize(),
                defaults={
                    "type": pokemon_data["types"][0]["type"]["name"].capitalize(),
                    "image": pokemon_data["sprites"]["front_default"],
                    "abilities": ", ".join([a["ability"]["name"].capitalize() for a in pokemon_data["abilities"]]),
                    "height": pokemon_data["height"] / 10,  # Convertimos dm a metros
                    "weight": pokemon_data["weight"] / 10,  # Convertimos hg a kg
                }
            )

    print(f"✅ Se han agregado {len(pokemons)} Pokémon correctamente.")

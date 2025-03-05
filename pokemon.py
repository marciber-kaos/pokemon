import requests

def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "Nombre": data["name"].capitalize(),
            "ID": data["id"],
            "Altura": data["height"],
            "Peso": data["weight"],
            "Tipos": [t["type"]["name"].capitalize() for t in data["types"]]
        }
        return pokemon_info
    else:
        return None

# Solicitar el nombre del Pokémon
pokemon_name = input("Ingrese el nombre del Pokémon: ")
pokemon_data = get_pokemon_data(pokemon_name)

if pokemon_data:
    print("\nInformación del Pokémon:")
    for key, value in pokemon_data.items():
        print(f"{key}: {value}")
else:
    print("No se encontró el Pokémon. Verifica el nombre e inténtalo de nuevo.")

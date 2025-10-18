import requests

base_url = 'https://pokeapi.co/api/v2/pokemon/'

def get_poke_info(name):
    url = base_url + name
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('error connecting')

pokemon_name = 'charizard'
pokemon_data = get_poke_info(pokemon_name)

if pokemon_data:
    print(f"Name: {pokemon_data['name']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
    print("Abilities:")
    for ability in pokemon_data['abilities']:
        print(f" - {ability['ability']['name']}")
    
import requests

def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    try:
        response = requests.get(url, timeout=5)
        print(f"Status Code: {response.status_code}")

        # Raise error if bad status
        response.raise_for_status()

        data = response.json()
        print(f"\n{name.title()} stats:")
        for stat in data["stats"]:
            stat_name = stat["stat"]["name"]
            base = stat["base_stat"]
            print(f"  {stat_name:15} {base}")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Connection error: {err}")

if __name__ == "__main__":
    get_pokemon("pikachu")
    print("\nTesting invalid call:")
    get_pokemon("pikachuu")  # triggers 404

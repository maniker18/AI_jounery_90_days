import requests
import json
pokiman_name = "Pikachu"
base_url = "https://pokeapi.co/api/v2/"

def pokemaon_check(name):
    url = f"{base_url}/pokemon/{pokiman_name}"
    respone = requests.get(url)
    if respone.status_code == 200:
        print(" pokeman found")
        data = respone.json()
        return data
    else:
        print("name doesnt match pokeman")

pokwmon_info =pokemaon_check(pokiman_name)
if pokwmon_info:
    print(pokwmon_info["name"])









    

# print(respone)
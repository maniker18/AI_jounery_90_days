import requests
import json
url = "https://jsonplaceholder.typicode.com/users/"
id =1
# f_url = f"{url}"
respone = requests.get(f"{url}{id}")
data = respone.json()

print(data)
with open("person.json","w") as f:
    json.dump(data,f,indent=2)
    print()







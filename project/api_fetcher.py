import requests
import json

class DataSyncAgent():


    def __init__(self, base_url):
        self.baserul = base_url
        self.lastd = None

    def user_id(self, id):
        try:
            url = f"{self.baserul}{id}"
            response = requests.get(url)
            sc = response.status_code
            if sc == 200:
                data = response.json()
                self.lastd = data
                return data
            else:
                print(f"warning {sc}")
                self.lastd = None          # <-- clear stale data
                return None
        except requests.exceptions.RequestException as e:
            print(e)
            self.lastd = None              # <-- clear stale data here too
            return None
   
    def json_method(self):
        
        with open("person.json","w") as f:
            json.dump(self.lastd,f,indent=2)
        


DataSyncAgent1 =DataSyncAgent("https://jsonplaceholder.typicode.com1/users/")

print(DataSyncAgent1.user_id(999)) 
DataSyncAgent1.json_method()   
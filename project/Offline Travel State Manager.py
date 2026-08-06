from pathlib import Path
import json
class travel_itinerary():
    directory = Path("offline_cache")

    def __init__(self,destination,departure_date,accommodation):
        self.destination= destination
        self.departure_date =departure_date
        self.accommodation = accommodation

    def save_json(self,filename):
       
        self.directory.mkdir(exist_ok=True)

        with open(self.directory/filename,"w") as f:
            data = {"destination" : self.destination,"departure_date" :
                    self.departure_date,"accommodation":self.accommodation}

            json.dump(data,f,indent = 2)

    @classmethod
    def load(cls,filename):
        try:
            with open (cls.directory/filename,"r") as f:
                data = json.load(f)
            return cls(data["destination"], data["departure_date"], data["accommodation"])
        except FileNotFoundError :
            print("Warning: file not found")
            return cls("Unknown", "Unknown", False)
        except json.JSONDecodeError:
            print("Warning: corrupted JSON")  
            return cls("Unknown", "Unknown", False)
 
# except AttributeError as e:
#                 print("missing filename ")

travel_itinerary1 = travel_itinerary("banglore","12-11-2016",True)
travel_itinerary1.save_json("bangalore.json")
travel_itinerary1.load("json_01")
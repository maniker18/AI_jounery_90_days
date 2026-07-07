import json

people_string = '''
{
    "people": [{ 
    "name": "John Smith",
    "age": 30,
    "city": "New York"
    },
{

    "name" :"smith",
    "age":20,
    "city" : "new jersey"

   }]
   }'''

data = json.loads(people_string)
print(type(data))

for person in data["people"]:
    del person["age" ]

for person in data["people"]:
    print(person)

str = json.dumps(data,indent = 2)
print(type(str))
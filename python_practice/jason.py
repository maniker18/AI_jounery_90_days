# import json

# string_1 = '''{
#     "people": {
#         "person1": {"name": "John", "age": 30, "city": "New York"},
#         "person2": {"name": "Jane", "age": 25, "city": "Los Angeles"},
#         "person3": {"name": "Mike", "age": 35, "city": "Chicago"}
#     }
# }'''

# peopl = json.loads(string_1)
# # print(peopl)

# for l in peopl["people"].values():
#     del (l["name"])

# # print(peopl)

# string_2 = json.dumps(peopl,indent=2)

# print(string_2)


import json

person = {
    "name": "Mani",
    "age": 24,
    "city": "Hyderabad",
    "skills": ["Python", "SQL", "Java"]
}

# TODO: convert `person` to a JSON string using json.dumps()
# print it and check the type with type()

data = json.dumps(person,indent=4,sort_keys=True)
# print(data)
# print(type(data))

json_string = '{"name": "Mani", "age": 24, "city": "Hyderabad"}'

# TODO: convert json_string back into a Python dict using json.loads()
# print it, check its type
# then try accessing a key like ["name"] to prove it's a real dict now

data1 = json.loads(json_string)
print(data1["name"])
print(type(data1))



# TODO:
# 1. Open a file called "person.json" in write mode using `with open(...) as f:`
# 2. Use json.dump(person, f, indent=4) to write it
# 3. Go check your folder — did person.json actually appear?

with open("person.json","w") as f:
    json.dump(person,f,indent=4)

with open("person.json","r") as fp:
    dat = json.load(fp)
print(dat["skills"])
print(type(dat))
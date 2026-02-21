import json

#python to json
data = {"name": "Aigerim", "age":17}

json_data = json.dumps(data)
print(json_data)

#json to python
json_string = '{"name": "Aigerim", "age":18}'

python_obj = json.loads(json_string)
print(python_obj["name"])

#write to json file
data = {"city": "Almaty", "country": "Kazakhstan"}

with open("data.json", "w") as file:
    json.dump(data, file)

#Read from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

print(data)

#Complex JSON (dict in list)
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Aruzhan", "grade": 85}
]

json_data = json.dumps(students, indent=4)
print(json_data)
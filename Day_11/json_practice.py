#Example 1: Python JSON to dict
import json 
person = '{"name": "Imtiaz",  "language": ["English", "Bengali"]}'
person_dict = json.loads(person)
print(person_dict)

print(person_dict['language'])

#Example 2: Python read JSON file
with open('Day_11/data.json', 'r') as f:
    data = json.load(f)
    print(data)

#Example 3: Convert dict to JSON
person_dict = {
    "name": "Imtiaz",
    'age': 25,
    'children': None,
}
person_json = json.dumps(person_dict)
print(person_json)

person_dict = {
    "name":"Khan",
    "age": 30,
    "married": True,
}


with open('Day_11/person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)
#Example 5: Python pretty print JSON
person_string = '{"name": "Imtiaz",  "language": ["English", "Bengali"]}'
#Getting dictionary
person_dict = json.loads(person_string)

#Pretty Printing JSON string back
print(json.dumps(person_dict, indent=4, sort_keys=True))
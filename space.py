import requests

response = requests.get('http://api.open-notify.org/astros.json')
people_in_space_json = response.json()

print('The people currently in space are:')
for people in people_in_space_json['people']:
    print(people['name'])
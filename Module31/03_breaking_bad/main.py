import requests
import json

my_req = requests.get('https://breakingbadapi.com/api/deaths')
data = json.loads(my_req.text)
max_death = 0
for i_elem in data:
    if i_elem['number_of_deaths'] > max_death:
        max_death = i_elem['number_of_deaths']
for j_elem in data:
    if j_elem['number_of_deaths'] == max_death:
        with open('User_info.json', 'w') as file:
            json.dump(j_elem, file, indent=4)
with open('User_info.json', 'r') as file:
    data = json.load(file)
print(data)

for i_info in data:
    if i_info == 'death_id':
        print('ID episode:', data[i_info])
    elif i_info == 'season':
        print('Season number:', data[i_info])
    elif i_info == 'episode':
        print('Episode number:', data[i_info])
    elif i_info == 'number_of_deaths':
        print('Total deaths:', data[i_info])
    elif i_info == 'death':
        print('List of dead:', data[i_info])




import requests
import json

episode_req = requests.get('https://www.breakingbadapi.com/api/episodes')
episode_data = json.loads(episode_req.text)
episode_id = 0
for i_episode in episode_data:
    if i_episode['season'] == '2' and i_episode['episode'] == '13':
        episode_id = i_episode['episode_id']


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

print('ID episode:', episode_id)

for i_info in data:
    if i_info == 'season':
        print('Season number:', data[i_info])
    elif i_info == 'episode':
        print('Episode number:', data[i_info])
    elif i_info == 'number_of_deaths':
        print('Total deaths:', data[i_info])
    elif i_info == 'death':
        print('List of dead:', data[i_info])

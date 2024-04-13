import requests
from pprint import pprint
url = "https://akabab.github.io/superhero-api/api"
response = requests.get(f'{url}/all.json')
# with open('answer.json', 'w') as file:
#     file.write(response.text)
all_hero_info = response.json()
heroes = {}
for hero_info in all_hero_info:
    name = hero_info['name']
    if name == 'Hulk':
        heroes[hero_info['name']] = hero_info['powerstats']['intelligence']
    elif name == 'Captain America':
        heroes[hero_info['name']] = hero_info['powerstats']['intelligence']
    elif name == 'Thanos':
        heroes[hero_info['name']] = hero_info['powerstats']['intelligence']

sorted_people = sorted(heroes.items(), key=lambda item: item[1])
print(sorted_people[-1][0])
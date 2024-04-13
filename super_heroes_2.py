import requests
from pprint import pprint
url = "https://akabab.github.io/superhero-api/api"
response = requests.get(f'{url}/all.json')
# with open('answer.json', 'w') as file:
#     file.write(response.text)
all_hero_info = response.json()
super_heroes = {}
heroes = [222, 112, 113]
for i in range(len(heroes)):
    for hero_info in all_hero_info:
        if hero_info['id'] == heroes[i]:
            super_heroes[hero_info['name']] = hero_info['powerstats']['intelligence']
sorted_people = sorted(super_heroes.items(), key=lambda item: item[1])
print(sorted_people[-1][0])

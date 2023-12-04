import requests
import json

def starscraping(url: str = 'https://swapi.dev/api/'):
    req = requests.get(f'{url}starships')
    data = json.loads(req.text)
    result = dict()

    for ship in data['results']:
        if ship['name'] == 'Millennium Falcon':
            result = {
                'ship_name': ship['name'],
                'max_atmosphering_speed': ship['max_atmosphering_speed'],
                'starship_class': ship['starship_class'],
                'pilots': []
            }

        for url in ship['pilots']:
            pilot_req = requests.get(url)
            pilot_data = json.loads(pilot_req.text)

            planet_req = requests.get(pilot_data['homeworld'])
            planet_data = json.loads(planet_req.text)

            pilot_info = {
                'name': pilot_data['name'],
                'height': pilot_data['height'],
                'mass': pilot_data['mass'],
                'homeworld': planet_data['name'],
                'homeworld_url': pilot_data['homeworld']
            }

            result['pilots'].append(pilot_info)

    with open('starship.json', 'w', encoding='UTF-8') as file:
        json.dump(result, file, indent=4)

    return result

text = starscraping()
print(text)



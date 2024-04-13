import requests
import time

url = 'https://geocode.maps.co/reverse'
token ='' # API geocode


def find_uk_city(coordinates:list) -> str:
    uk_cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    for i in range(len(coordinates)):
        latitude = coordinates[i][0]
        longitude = coordinates[i][1]
        param = {'lat': latitude,
                     'lon': longitude,
                     'api_key': token
                     }
        response = requests.get(url=url, params=param).json()
        time.sleep(1) # Задержка, чтобы в цикле сайт не думал что его DDOS
        if response['address']['city'] in uk_cities:
            return response['address']['city']
            
            

if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'
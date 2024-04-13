import requests
import json
from pprint import pprint

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = '' # https://yandex.ru/dev/dictionary/

def translate_word(word):
    param = {'key': token,
             'lang': 'ru-en',
             'text': word,
             'ui': 'ru'
             }
    response = requests.get(url=url, params=param).json()
    return response['def'][0]['tr'][0]['text']

pprint(translate_word('кот'))

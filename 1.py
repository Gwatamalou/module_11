import requests
from pprint import pprint

q = {'q': 'Moscow', 'appid': '1b417740c98e2c1ca400c10eb4312013', 'units': 'metric'}
URL = f'http://api.openweathermap.org/data/2.5/weather'

r = requests.get(URL, params=q)

pprint(r)
import json
import requests
import pandas as pd
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt


#===================================================================
#
cityes = ['Tokyo', 'Delhi', 'Shanghai', 'São Paulo', 'Mumbai', 'Beijing', 'Cairo', 'Dhaka', 'Mexico City', 'Osaka',
          'New York City', 'Karachi', 'Chongqing', 'Istanbul', 'Kolkata', 'Manila', 'Rio de Janeiro', 'Guangzhou',
          'Lahore', 'Shenzhen', 'Bangalore', 'Moscow', 'Tianjin', 'Jakarta', 'London', 'Lima', 'Bangkok', 'Chengdu',
          'Bogotá', 'Chennai', 'Paris', 'Tehran', 'Hyderabad', 'Wuhan', 'Hangzhou', 'Santiago', 'Alexandria',
          'Kuala Lumpur', 'Nairobi', 'Los Angeles', 'Abidjan', 'Addis Ababa', 'Kanpur', 'Hong Kong', 'Brasília',
          'Sydney', 'Melbourne', 'Philadelphia', 'San Francisco']

q = {'q': None, 'appid': '67ad722f344bbab57f17ee1dbe5101c9', 'units': 'metric'}
URL = f'http://api.openweathermap.org/data/2.5/weather'
# tem = []




with mp.Manager as manager:
    tem = manager.dict()
    for city in cityes:
        q['q'] = city
        try:
            response = requests.get(URL, q)
            response.raise_for_status()
            data = response.json()
            city_weather = {
                'City': city,
                'Temp': data['main']['temp'],
                'Humidity': data['main']['humidity'],
                'Description': data['weather'][0]['description']
            }
            tem.append(city_weather)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка: {e}")

df = pd.DataFrame(tem)
print(pd)

# with mp.Manager() as manager:
#     requestDict = manager.dict()
#     for request in requests:
#         p = mp.Process(target=self.process_request, args=(request, requestDict, lock,))
#         p.start()
#         p.join()
#     self.data.update(requestDict)
# #===================================================================
# x = []
# df = pd.DataFrame()
#
# with open('tem.json', 'r', encoding='utf-8') as file:
#     d = json.load(file)
#     for data in d:
#         # pprint(i)
#         city_weather = {
#             'City': data['name'],
#             'Temp': data['main']['temp'],
#             'Humidity': data['main']['humidity'],
#             'Description': data['weather'][0]['description']
#         }
#         x.append(city_weather)
#
# df = pd.concat([df, pd.DataFrame(x)], axis=1)
#
# ===========================================================================

x_city = np.array(df['City'])
y_temp = np.array(df['Temp'])

av_temp = np.mean(df['Temp'])
av_humidity = np.mean(df['Humidity'])

print(df)
print()
print(f'Средняя Температура: {av_temp:10.02f}')
print(f'Средняя влажность: {av_humidity:10.02f}')

plt.bar(x_city, y_temp)
plt.xticks(rotation=45)
plt.show()

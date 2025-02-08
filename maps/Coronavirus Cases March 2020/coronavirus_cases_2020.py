import pandas as pd
import geopandas as gpd
import requests


r = requests.get('https://news.google.com/covid19/map?hl=en-AU&gl=AU&ceid=AU%3Aen').text
data = pd.read_html(r)
data[0] = data[0][1:]

for data_cases in data:
    print(data_cases)
    
data_cases = data_cases[['Location', 'Deaths' ]]

world_data = gpd.read_file('World_Map.shp')

print(world_data['NAME'].tolist())

for items in data_cases['Location'].tolist():
    world_data_list = world_data['NAME'].tolist()
    if items in world_data_list:
        pass
    else:
        print(items + ' is not in the world_data list')
    
world_data.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
world_data.replace('Czech Republic', 'Czechia', inplace = True)


data_cases.rename(columns = {'Location': 'NAME'}, inplace = True)

combined = world_data.merge(data_cases, on = 'NAME')

combined.to_file("combined.shp")











































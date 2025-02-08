# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:00:40 2021

@author: Giacomo
"""


import pandas as pd
import requests
from matplotlib import pyplot as plt

r = requests.get('https://news.google.com/covid19/map?hl=en-AU&gl=AU&ceid=AU%3Aen').text
data = pd.read_html(r)
data = data[0]

plt.bar(data.Location[1:10], data.Deaths[1:10])
plt.show()
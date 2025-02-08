import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import folium
import geopandas

pd.set_option("display.max_rows", None, "display.max_columns", None)

# The URL we will read our data from
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_past_and_projected_GDP_(nominal)'
# read_html returns a list of tables from the URL
tables = pd.read_html(url)

# i = 0
# for table in tables:
#     print("TABELLA NUOVAAAAA NUMERO", i, table.head())
#     i += 1

# Merge the tables into one table
merge_index = 'Country (or dependent territory)'
table = tables[8].merge(tables[11], how="left", left_on=[merge_index], right_on=[merge_index])
table = table.merge(tables[14], how="left", left_on=[merge_index], right_on=[merge_index])

print(table.iloc[80])

# row = table.iloc[80]
# X = table.columns[1:].to_numpy().reshape(-1, 1)
# X = X.astype(int)
# Y = 1 + row.iloc[1:].pct_change()
# Y = Y.cumprod().fillna(1.0).to_numpy()
# Y = Y.reshape(-1, 1)

# regr = LinearRegression()
# regr.fit(X, Y)

# Y_pred = regr.predict(X)

# plt.scatter(X, Y)
# plt.plot(X, Y_pred, color='red')
# plt.show()


coef = []
countries = []

for index, row in table.iterrows():
    #print(row)
    X = table.columns[1:].to_numpy().reshape(-1, 1)
    X = X.astype(int)
    Y = 1 + row.iloc[1:].pct_change()
    Y = Y.cumprod().fillna(1.0).to_numpy()
    Y = Y.reshape(-1, 1)

    regr = LinearRegression()
    regr.fit(X, Y)

    coef.append(regr.coef_[0][0]*100)
    countries.append(row[merge_index])

data = pd.DataFrame(list(zip(countries, coef)), columns=['Country', 'Coef'])

print(data)


# Read the geopandas dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# Replace United States of America to United States to fit the naming in the table
world = world.replace('United States of America', 'United States')

# Merge the two DataFrames together
table = world.merge(data, how="left", left_on=['name'], right_on=['Country'])


# Clean data: remove rows with no data
table = table.dropna(subset=['Coef'])

# We have 10 colors available resulting into 9 cuts.
table['Cat'] = pd.qcut(table['Coef'], 9, labels=[0, 1, 2, 3, 4, 5, 6, 7, 8])

print(table)


# Create a map
my_map = folium.Map()

# Add the data
folium.Choropleth(
    geo_data=table,
    name='choropleth',
    data=table,
    columns=['Country', 'Cat'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Growth of GDP since 1990',
    threshold_scale=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
).add_to(my_map)
my_map.save('gdp_growth.html')

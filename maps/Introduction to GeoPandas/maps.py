import geopandas as gpd

districts = gpd.read_file("Introduction to GeoPandas\Shapefiles\districts.shp")

districts.plot()

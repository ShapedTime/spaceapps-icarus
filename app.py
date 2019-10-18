import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

shapefile = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
shapefilefire = 'DL_FIRE_M6_81021/fire_nrt_M6_81021.shp'

gdffire = gpd.read_file(shapefilefire)

gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()

ax = gdf.plot()
gdffire.plot(ax=ax)


plt.show()


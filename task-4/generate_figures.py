import galah
import geopandas as gpd
import shapely
import mapclassify, matplotlib
import folium
import kaleido
import plotly.express as px
import plotly
from math import log

def reslog(x):
    if x == 0:
        return 0
    else:
        return log(x, 10)

## Read in geojsons

grid = gpd.read_file('./spatial/act_grid_road_count_latlon.geojson')
act_border = gpd.read_file('./spatial/act_border_latlon.geojson')
bird_grid = gpd.read_file('./spatial/2023_Bird_sighting_grid.geojson')
bird_grid['log_occurrences'] = [reslog(x) for x in bird_grid.occurences]

grid_leaflet = grid.explore()
grid_leaflet.save("./output/grid.html")

#grid.near_road

## pull bird data

birds = gpd.read_file('./spatial/records-2024-05-10/records-2024-05-10.csv', include_fields=[ 'vernacularName', 'decimalLatitude', 'decimalLongitude', 'scientificName', 'eventDate'], rows = 10000, crs = 'EPSG:4326')
birds.set_crs(crs='EPSG:4326', inplace=True)
birds['geometry'] = [shapely.Point(xy) for xy in zip(birds.decimalLongitude, birds.decimalLatitude)]
# gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.lon, data.lat)

cbrbirds = gpd.clip(birds, act_border)

cbrbirds.explore().save('./output/webmap/birds.html')

## query galah
#print(galah.atlas_counts(filters=["year>=1980", "taxa=Banksia", "stateProvince=Australian Capital Territory"], group_by='year', expand=False))
#print(galah.atlas_counts(filters=["year>=1980", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='species', expand=False))

bird_counts = galah.atlas_counts(filters=["year=2023", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='vernacularName', expand=False)
bird_counts.sort_values(by='count', ascending=False, inplace=True)

## Make pie chart

bird_pie = px.pie(bird_counts.head(20), values='count', names='vernacularName',
    title='2023 Sighting Frequency by Species',
    hover_data=['vernacularName'], labels={'vernacularName':''}
    )
bird_pie.update_traces(textposition='inside', textinfo='percent+label')
bird_pie.write_image('output/img/pie.png')
plotly.offline.plot(bird_pie, filename='output/webmap/pie.html')

## Histogram of sites:

bird_histogram = px.histogram(bird_grid, x='occurences', color='near_road', log_y=True)
bird_histogram.write_image('output/img/histogram.png')
plotly.offline.plot(bird_histogram, filename='output/webmap/histogram.html')

## FAILED ## pie of sites

# Split the frame by near road versus remote.
# Ssum the toatal occurrences for each df.
#bird_pie = px.pie(bird_grid.occurences, values='count', names='vernacularName',

## FAILED ## Download dataset

#galah.atlas_species(taxa="Aves",filters="stateProvince=Australian Capital Territory")
#galah.atlas_occurrences(taxa="Eolophus roseicapilla",filters=["stateProvince=Australian Capital Territory","year>=2023"],fields=["institutionID","basic"])
# I keep getting JSON errors from the get_occurrences command
# changing the parameters doesn't help at all

#birds = galah.atlas_counts(filters=["year>=1980", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='species', expand=False)
#print(birds.sort_values('count', ascending=False).head(20))

#galah.atlas_counts(filters=["year>=2010", "taxa=Aves", "stateProvince=Australian Capital Territory"])

#birds = galah.atlas_occurrences(filters=["year>=2010", "taxa=Aves", "stateProvince=Australian Capital Territory"])

## Context
# Show the ACT map broken into a 1 sqkm grid with the roads painted over it
# and a 500m buffer around the roads.

## Most common species in my suburb:

# Grab my suburb's square
# send a request to ALA asking for the species within my suburb

# sort species by count
# list species

## Most biodiverse area of the ACT:

# get ocurrance records for the whole territory

# run through the grid cells.
# count the number of unique species for each cell.

# Make a map showing the number of species per cell


## Is the data skewed towards areas with roads?

# show a scatter plot with the biodiversity on the y-axis and the total length
# of roads on the x axis

# Alternatively, Show a histogram with the number of species on the x axis and
# the count of cells on the y-axis. Colour code the bars by remote or not.

## Chloropleth

# Create a leaflet map of the sighting density overlaying the road network.


m = folium.Map(location=(-35.5, 149), zoom_start=10, tiles="cartodb positron")
# m = folium.Map(location=(30, 10), zoom_start=3, tiles="Open Street Map")

#folium.GeoJson('./spatial/act_border_latlon.geojson').add_to(m)
#folium.GeoJson('./spatial/act_grid_road_count_latlon.geojson').add_to(m)

# Map title code from stack overflow user Do-Me
map_title = "Base 10 Log of Occurrences"
title_html = f'<h1 style="position:absolute;z-index:100000;left:40vw" >{map_title}</h1>'
m.get_root().html.add_child(folium.Element(title_html))

folium.Choropleth(
    geo_data='./spatial/2023_Bird_sighting_grid.geojson',
    data=bird_grid,
    columns=["id", "log_occurrences"],
    key_on="feature.properties.id",
    fill_color="YlOrRd",
    fill_opacity=0.5,
    line_opacity=0.1,
).add_to(m)

m.save("./output/webmap/chloropleth.html")
import galah
import geopandas as gpd
import shapely


# Figure out how to get common names
print(galah.atlas_counts(filters=["year>=1980", "taxa=Banksia", "stateProvince=Australian Capital Territory"], group_by='year', expand=False))
print(galah.atlas_counts(filters=["year>=1980", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='species', expand=False))

birds = galah.atlas_counts(filters=["year>=1980", "taxa=Aves", "stateProvince=Australian Capital Territory"], group_by='species', expand=False)
print(birds.sort_values('count', ascending=False).head(20))

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

## Dashboard

# Create a leaflet map of the species count overlayed with the road network.
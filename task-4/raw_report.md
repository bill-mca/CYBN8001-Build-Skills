---
Title: Skiils Work 4
Author: Bill McAlister
Date: 2024-05-10
colorlinks: blue
---
# Introduction
I've decided to investigate the Atlas of Living Australia's (ALA) occurence record data to see if it aligns with my annecdotal experience and if there is a noticeable sampling bias. This investigation will demonstrate my understanding of the importance of scientific interpretation of data. 

## Methods
As much as possible I'm aiming to abide by reproducible research guidelines in this project. All the code written for this assignment is [available on Github](https://github.com/bill-mca/CYBN8001-Build-Skills/tree/main/task-4). Running the code on a linux computer should regenerate all outputs including this report and the dashboard. The code uses the ALA's galah API to download data so that re-running the code should generate an updated report includng any freshly collected data. 

For this report, I have not undertaken any sophisticated spatial or temporal statistics. My method for assessing bias will be qualitative. I hope that it will be clear from a qualitative analysis whether or not bias exists however, it may be necessary to recomend more rigorous analysis if my qualitative methods do not make it obvious.

### Pre-processing
I did some pre-processing of spatial data in the [QGIS](qgis.org) desktop app. The resulting datasets were included as a zip file in the [Github repo](https://github.com/bill-mca/CYBN8001-Build-Skills/tree/main/task-4). The spatial data generated will be used to assess the question of whether or not the data is skewed by sampling bias. Here are the steps that I took with QGIS:

- I downloaded a geojson of the ACT border from the [ACT Spatial catalogue website](https://actmapi-actgov.opendata.arcgis.com/datasets/71f829d78ce34246ad8f71c684042c1d_0/explore). 
- I took a bounding box of the ACT and cut it into 1km^2 boxes.
- I discarded all boxes that were not completely included within the ACT border. This step protects against a bias where border cells will have lower than expected counts because the occurence records are restricted to the ACT.
- There were 2176 grid cells in total.
- I downloaded a geojson of the ACT road network from the [ACT Spatial catalogue website](https://actmapi-actgov.opendata.arcgis.com/datasets/9fb78ff6f8b74efe8720d05b333ebaba_0/explore?location=-35.511583%2C149.085154%2C9.91)
- I deleted all road lines that fall outside the ACT border (Jervis Bay etc.).
- I applied a 500m buffer to the road network dataset.
- Grid cells that did not at all overlap with the buffered road network were tagged as remote.
- There were 1286 remote grid cells.
- I transformed the grid cells, the ACT border and the road network from GDA2020 MGA zone 55 into WGS84. The datum shift used a null transformation. This step was taken to align with the geographic coordinates reported by the ALA dataset which i will assume are reported in WGS84.

![A map of the ACT broken into 1km grid cells showing roads overlayed.]('./output/img/grid_cell_map.png')

### Spatial precision
For the pupose of this analysis I have aimed for a spatial precision of about 250m. I discarded all records frpm the ALA that did not report spatial certainty or reported uncertainty greater than 200m. This coarse target, and the use of a 1km grid for analysis, made redundant any issues of spatial datums or coordinate measurement methods (GPS, reporting from map etc) as these errors are on the order of 10s of metres not hundreds of metres. The choice to use recent records helped to mitigate inprecision as more records have results reported with GPS coordinates rather than coordinates reverse geocoded from a place name. 

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

This grid will be the basis of my investigation of sampling bias. I will be investigation the 

# show a scatter plot with the biodiversity on the y-axis and the total length
# of roads on the x axis

# Alternatively, Show a histogram with the number of species on the x axis and
# the count of cells on the y-axis. Colour code the bars by remote or not.

## Dashboard

The ideal dashboard would allow users to explore the map and selct grid cells. Selected grid cells would be highlighted on the scatter graph. working backwards, the user could select points on the graph and see the corresponding grid cell highlighted on the map. This type of exploratory investigation of outliers is the real strength of interactive data dashboads. 

Interactively linking the graph with the map was out of scope for me but I've produced an interactive map that allows users to interrogate grid cells to see how many occurence records and how much road there is in each cell. This allows users who are familiar with the ACT to compare their personal experience with the data in an interactive dasboard.

[![A screenshot of the interactive map on the dashboard.](./dashboard_screenshot.png)](bill-mca.github.io/webmap/index.html')

# Aknowledgements

Thanks to Ant and Izak who encouraged me to stick to my self-proclaimed policy of not putting in too much effort on skills-work assignments. I'm affraid I ignored you and went over the top writing custom code and learning a few new libraries.



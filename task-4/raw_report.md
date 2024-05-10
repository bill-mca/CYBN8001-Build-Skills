---
Title: Skiils Work 4
Author: Bill McAlister
Date: 2024-05-10
colorlinks: blue
---
# Introduction
I've decided to investigate the Atlas of Living Australia's (ALA) occurence record data to see if it aligns with my annecdotal experience and if there is a noticeable sampling bias. This investigation will demonstrate my understanding of the importance of scientific interpretation of data. 

## Methods
As much as possible I'm aiming to abide by reproducible research guidelines in this project. All the code written for this assignment is [available on Github](https://github.com/bill-mca/CYBN8001-Build-Skills/tree/main/task-4). Running the code on a linux computer should regenerate all outputs including this report and the dashboard. I tried to use the ALA's galah API to download data so that re-running the code should generate an updated report includng any freshly collected data. However, it was too difficult. I kept getting JSON errors when I tried to download occurence records. Also, the volume of data is overwhelming. For 2023, there were almost 95000 bird sightings recorded in the ACT. Of these the ALA interface recomended screening about 1300 because of suspect data fields or because they recorded absences.

![ALA's download interface showing the records available for Canberra in 2023'.](./output/img/2023_ACT_bird_records.png)

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
- I transformed the grid cells, the ACT border and the road network from GDA2020 MGA zone 55 into WGS84. The datum shift used a null transformation. This step was taken to align with the geographic coordinates reported by the ALA dataset which I will assume are reported in WGS84.

![A map of the ACT broken into 1km grid cells with roads.](./output/img/grid_cell_map.png)

### Spatial precision
For the pupose of this analysis I have aimed for a spatial precision of about 250m. I discarded all records frpm the ALA that did not report spatial certainty or reported uncertainty greater than 200m. This coarse target, and the use of a 1km grid for analysis, made redundant any issues of spatial datums or coordinate measurement methods (GPS, reporting from map etc) as these errors are on the order of 10s of metres not hundreds of metres. The choice to use recent records helped to mitigate inprecision as more records have results reported with GPS coordinates rather than coordinates reverse geocoded from a place name. 

## Is the data skewed toward conspicuous species?

To get a feel for which species are being recorded, I produced a piechart showing the relative frequency of observation of the 20 most commonly recorded bird species in the ACT for 2023. The magpie was the most commonly observed bird. I believe that this is an indication of a bias in the dataset. The magpie is a very conspicuous species recognisable by most citizen scientists. 

![A pie chart of the relative frequency of observation for the ACT's 20 most common birds'.](./output/img/pie.png)

Magpies are indeed ubiquitous throughout suburban Canberra. However, magpies are quite large predatory birds. Ecological theory would predict that smaller birds occupying lower trophic levels would be more numerous. As an example, I would expect the Noisy Miner bird to be more numerous than the Magpie but it is recorded about half as often as Magpies. I believe that the data has a bias toward conspicuous species.

## Is the data skewed towards accessible areas?

To investigate The extent to which data is skewed towards accessible areas I applied a histogram and a map visualisation. Firstly, the histogram chart shows the relationship between bird sightings and roads 

## Dashboard

The ideal dashboard would allow users to explore the map and selct grid cells. Selected grid cells would be highlighted on the scatter graph. working backwards, the user could select points on the graph and see the corresponding grid cell highlighted on the map. This type of exploratory investigation of outliers is the real strength of interactive data dashboads. 

Interactively linking the graph with the map was out of scope for me but I've produced an interactive map that allows users to see the density of occurrence records layed over the canberra road network. The dashboard also includes the raw sighting data. This allows users who are familiar with the ACT to compare their personal experience with the data. Interogating the raw sighting data shows that there are many records of birds taken at popular natural recreation areas especially Jerrabombera Wetlands.

## Conclusion
The ALA's bird sighting dataset is of limited utility for ecological research. While the data does indicate which species occur in Canberra, There is very little data from remote areas of the ACT. As such, it is not possible to use this data to draw any conclusions about the biodiversity of most areas of the ACT. Another limitation identified was a bias toward conspicuous species. While this data might be useful to identify areas of suburban canberra where Magpies are less common, the data would not be reliable to indicate either the presence or absence of inconspicuous, small or difficult to identify species.

# Aknowledgements

Thanks to Ant and Izak who encouraged me to stick to my self-proclaimed policy of not putting in too much effort on skills-work assignments. I'm affraid I ignored you and went over the top writing custom code and learning a few new libraries.



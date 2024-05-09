

- I downloaded a geojson of the ACT border from the [ACT Spatial catalogue website](https://actmapi-actgov.opendata.arcgis.com/datasets/71f829d78ce34246ad8f71c684042c1d_0/explore). 
- I took a bounding box of the ACT and cut it into 1km^2 boxes.
- I discarded all boxes that were not completely included within the ACT border.
- There were 2176 grid cells in total.
- I downloaded a geojson of the ACT road network from the [ACT Spatial catalogue website](https://actmapi-actgov.opendata.arcgis.com/datasets/9fb78ff6f8b74efe8720d05b333ebaba_0/explore?location=-35.511583%2C149.085154%2C9.91)
- I deleted all road lines that fall outside the ACT border (Jervis Bay etc.).
- I applied a 500m buffer to the road network dataset.
- Grid cells that did not at all overlap with the buffered road network were tagged as remote.
- There were 1286 remote grid cells.
- I transformed the grid cells, the ACT border and the road network from GDA2020 MGA zone 55 into WGS84. The datum shift used a null transformation. This step was taken to align the geographic coordinates reported by the ALA dataset.

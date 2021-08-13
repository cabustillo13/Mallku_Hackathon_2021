# Mallku_Hackathon_2021
<p align="center">
 <img width="100px" src="https://github.com/cabustillo13/Mallku_Hackathon_2021/blob/main/Demo/logo_mallku.png" align="center" alt="NASA Space App Challenge" />
 <h2 align="center">Mallku Hackathon 2021 in Argentina</h2>
 <p align="center"><b>Determine the probability that a heat source occurs under certain conditions.</b></p>
</p>

# Requirements

You can run this code in Python 2.7 and Python 3.x

# Toolkit Files

### Toolkit 1

```
___ Mapa
 |___ AEstrella.py            -> Pathfinder Algorithm
 |___ AlgoritmoGenetico.py    -> Genetic Algorithm
 |___ TempleSimulado.py       -> Annealing Algorithm
``` 
**Input:** A list with the order of the sources of where the fires occur.  

It's an API. It contains a genetic algorithm that allows you to order the order in which the fire sources should be turned off. It uses a simulated annealing algorithm for fitness. Which evaluates the distance between points with a Pathfinder algorithm. 

**Output:** Return an ordered list with which each source of fire must be extinguished.

### Toolkit 2

```
___ Clasificacion
  |___ Main.py                -> KNN Algorithm and KMeans Algorithm
```
 
**Input:** A parameter is passed that contains the data of: humidity, distance to the nearest water source and wind speed. This parameters are inside a csv file.
 
It's an API. Historical humidity data, distance to the nearest water source and wind speed obtained from the SAOCOM satellite are read but you can use any source of information available in csv format. We use K-Nearest Neighbor(KNN) algorithm to classify the degree of fire (Extreme, high, medium and low) and KMeans algorithm to do a regression.
 
 **Output:** Determine degrees of fire (Extreme, high, medium and low).
 
 ### Toolkit 3

```
___ Prediccion
  |___ main.py                -> KNN Algorithm 
 ```
 
**Input:** A parameter is passed that contains the data of: Temperature, Humidity and Wind. This parameters are inside a csv file.
 
It's an API. Historical data from Chile is analyzed (because they were the data we found). For the dataset (csv file), a cleaning and pre-filtering of the data was carried out.
 
 **Output:** Determine the probability of a fire occurring. If it is 1, the fire occurs. If it is 0, it does not occur..
 
 # Demo
 
 **Below is the execution of two Python programs that consume our developed API. This helps us to show and validate our APIs.**
 
 - Toolkit 1
 
 ![Toolkit 1](https://github.com/cabustillo13/Mallku_Hackathon_2021/blob/main/Demo/Toolkit1.gif)

- Toolkit 2
 
 ![Toolkit 2](https://github.com/cabustillo13/Mallku_Hackathon_2021/blob/main/Demo/Toolkit2.gif)

- Toolkit 3
 
 ![Toolkit 3_0](https://github.com/cabustillo13/Mallku_Hackathon_2021/blob/main/Demo/toolkit3.JPG)

 # Data and Resources
 
### For Mapa Folder

- We used a map with the location of the Volunteer Fire Station of the Province of Cordoba. In order to recommend which fire station is closest to the source of the fire.

Link: https://www.bomberoscordoba.com.ar/regional/regional.php

- We use Google Maps data to define a fire source as a point on the map, in those places in very large areas of forest. From that coordinate we assign a number or label to each focus. With that input processed data, we proceed to apply our API.

### For Clasificacion Folder

- **Fire danger:** It is classified in: extreme, high, medium and low degree.

Link : https://www.argentina.gob.ar/ambiente/fuego/alertatemprana/indices

- **Soil moisture:** Map of soil moisture estimates at 50cm depth, periodically updated in the last 7 days (SAOCOM data).

Link: https://gn-idecor.mapascordoba.gob.ar/maps/87/view

- **Distance to Water Resources:** Map of the essential data of "Portal de Información Hídrica de Córdoba (PIHC)"

Link: https://gn-idecor.mapascordoba.gob.ar/maps/295/view

- **Wind speed:** 10m above gnd.

Link: https://www.meteoblue.com/es/tiempo/webmap/beta/general-levalle_argentina_3855098#coords=5/-34.01/-63.92&map=windAnimation~coldwarm~auto~10%20m%20above%20gnd~none

### For Prediccion Folder

This is a data base of temperatures, humidity and wind for Chile of 4 stations of the region of the lakes. We were looking to interpolate the data to determine fire hazards.

- **The data was taken from the SMN of Chile**

Link: https://climatologia.meteochile.gob.cl/application/historico/datosDescarga/400009

- **The information of the fires of CONAF**

Link: https://www.conaf.cl/incendios-forestales/incendios-forestales-en-chile/estadisticas-historicas/

***From the interpolation and these data, if we knew which exact days the fires occurred, we could make an estimate of which days these fires occur in order to predict future catastrophes.***

 ![Toolkit 3_1](https://github.com/cabustillo13/Mallku_Hackathon_2021/blob/main/Demo/graph_toolkit3.jpg)
 ![Toolkit 3_2](https://github.com/cabustillo13/Mallku_Hackathon_2021/blob/main/Demo/Tabla_Toolkit3.JPG)

### NOTE: You can also use files your own data for our APIs.

# License

This project has License (Apache-2.0 License).


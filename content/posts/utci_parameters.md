Date: 2018-10-21
Modified: 2018-10-21
Status: published
Authors: Christian Kongsgaard
Tags: python, livestock, comfort, utci
Title: UTCI Parameters
Summary: Ever wondered, which parameter in the UTCI calculation is the most important? 

The Universal Thermal Climate Index (UTCI) is a widely used outdoor comfort metric. It is currently released as a
6th order polynomial formula with four inputs: Mean Radiant Temperature, Air Temperature, Wind Speed and Relative 
Humidity. 

I often hear that different measures are needed for achieving outdoor comfort in different climates. These claims
often only backed up by experience and I therefore figured that a parameter study of UTCI would be in place to bring 
some clarity.

# Universal Thermal Climate Index Model
Before going into the parameter investigation let me just, for clarity, describe basis for the UTCI model.

“The UTCI is defined as the air temperature (Ta) of the reference condition causing the same model response as actual 
conditions.” (Błazejczyk et al. 2013)

This can be rewritten as:

![alt text]({filename}/images/utci_parameters/utci_formula.png)

T<sub>a</sub> is ambient air temperature.
T<sub>MRT</sub> is mean radiant temperature.
U<sub>wind</sub> is wind speed.
p<sub>vapour</sub> is water vapour pressure.

The reference condition is defined as an environment with a wind speed (U<sub>wind</sub>) of 0.5 m/s at 10m height 
(approximately 0.3 m/s at 1.1m height), a mean radiant temperature (T<sub>MRT</sub>) that equals the ambient air temperature (T<sub>a</sub>), 
a vapour pressure (p<sub>vapour</sub>), which corresponds to a relative humidity of 50%, but having a maximum value of 20hPa. 
It is furthermore assumed that persons have a metabolic rate of 2.3 MET corresponding to a walking speed of 1.1 m/s and 
wearing clothing with a thermal resistance modeled by the UTCI-clothing model (Havenith et al. 2012).

The model uses the UTCI-Fiala model (Fiala et al. 2012) as it’s thermoregulation model. It models an average person of 
73.4kg and with a surface body area of 1.85m². The body is represented by 12 spherical or cylindrical parts and 
contains a total of 187 tissue nodes. The model also includes a model to predict thermoregulatory reactions of the 
central nervous system, e.g. shivering or sweating. 
The model computes an UTCI temperature, which can be categorized in terms of thermal stress. The assessment scale can 
be seen in the table below.

| UTCI (°C)     | Physiological Stress      |
|:---------     |:------------------------- |
| Above +46     | Extreme heat stress       |
| +38 to +46    | Very strong heat stress   |
| +32 to +38    | Strong heat stress        |
| +26 to +32    | Moderate heat stress      |
| +18 to +26    | Thermal comfort zone      |
| +9 to +18     | No thermal stress         |
| 0 to +9       | Slight cold stress        |
| -13 to 0      | Moderate cold stress      |
| -27 to -13    | Strong cold stress        |
| -40 to -27    | Very strong cold stress   |
| Below -40     | Extreme cold stress       |

As the complexity of the UTCI is quite large so is the computational power and time needed to perform the analysis. 
Therefore (Bröde et al. 2012) proposed methods for approximating the UTCI. 
They came up with two methods: a look-up table of pre-calculated UTCI values and a 6th order regression function. 
They state that the computing speed (number of calculations per second) of the three methods are as following:

* Actual UTCI model: 1/s 
* Look-up table: 100/s
* Regression function: >100 000/s

With the higher number of computation per second comes with a cost of lower accuracy for the regression function. 
On the other hand, the 4th dimensional (Ta, TMRT, Uwind, pvapour) look-up table with 100 steps in each dimension, 
would require 200Mb of storage space. Because of the higher number of calculations per second the regression function 
is most commonly used. The regression function is only valid within the following bounds:

* **Ambient Air Temperature**: -50 to +50°C
* **Mean Radiant Temperature**: 50°C below air temperature and 70°C above air temperature
* **Wind Speeds at 10m height**: 0.5 to 17m/s
* **Vapour Pressure**: 0hPa to 45hPa

This limits UTCI in some extreme cases, but the model covers the most scenarios.   

# Parameter Variation

The parameter study is done by varying MRT, wind speed and relative humidity, plot them against different air 
temperatures and comparing them to a base case.
For all three charts, the air temperature was in the range of: -30°C to 40°C.
The base case is: 50% relative humidity, a wind speed at 10m of 3m/s and MRT is equal to air temperature.

Relative humidity, wind speed and MRT was computed for the ranges:

* **Relative Humidity**: 10% - 90%
* **Wind Speed**: 0.5m/s - 17m/s
* **Mean Radiant Temperature**: -50°C - 70°C + air temperature

If you wish to play with this yourself, then I have made it into a Jupyter Notebook. 
You can download it [here]({filename}/content/scripts/UTCI Parameter Variations.ipynb)

## Relative Humidity

![alt text]({filename}/images/utci_parameters/utci_relhum.png)


## Wind Speed

![alt text]({filename}/images/utci_parameters/utci_wind.png)

## Mean Radiant Temperature

![alt text]({filename}/images/utci_parameters/utci_mrt.png)


#### Bibliography

Błazejczyk, Krzysztof, Gerd Jendritzky, Peter Bröde, Dusan Fiala, George Havenith, Yoram Epstein, Agnieszka Psikuta, 
and Bernhard Kampmann. 
    2013. 
    “An Introduction to the Universal Thermal Climate Index (UTCI).” 
    Geographia Polonica 86 (1): 5–10. https://doi.org/10.7163/GPol.2013.1.

Bröde, Peter, Dusan Fiala, Krzysztof Blazejczyk, Ingvar Holmér, Gerd Jendritzky, Bernhard Kampmann, Birger Tinz, and George Havenith. 
    2012. 
    “Deriving the Operational Procedure for the Universal Thermal Climate Index (UTCI).” 
    International Journal of Biometeorology 56 (3): 481–94. https://doi.org/10.1007/s00484-011-0454-1.
   
Coccolo, Silvia, Jérôme Kämpf, Jean Louis Scartezzini, and David Pearlmutter. 
    2016. 
    “Outdoor Human Comfort and Thermal Stress: A Comprehensive Review on Models and Standards.” 
    Urban Climate 18. Elsevier Inc.: 33–57. https://doi.org/10.1016/j.uclim.2016.08.004.

Fiala, Dusan, George Havenith, Peter Bröde, Bernhard Kampmann, and Gerd Jendritzky. 
    2012. 
    “UTCI-Fiala Multi-Node Model of Human Heat Transfer and Temperature Regulation.” 
    International Journal of Biometeorology 56 (3): 429–41. https://doi.org/10.1007/s00484-011-0424-7.

Havenith, George, Dusan Fiala, Krzysztof Blazejczyk, Mark Richards, Peter Bröde, Ingvar Holmér, Hannu Rintamaki, Yael Benshabat, and Gerd Jendritzky. 
    2012. 
    “The UTCI-Clothing Model.” 
    International Journal of Biometeorology 56 (3): 461–70. https://doi.org/10.1007/s00484-011-0451-4.


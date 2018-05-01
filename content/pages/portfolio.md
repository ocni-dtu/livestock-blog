Date: 30-04-2018
Modified: 01-05-2018
Status: published
Authors: Christian Kongsgaard
Title: PORTFOLIO

Below selection of my previous work can be found:

 
 
## Master Thesis:
#### Hygrotermic Control of the Micro Climate Around Buildings
**ABSTRACT:** The urban heat island (UHI) is a well-documented phenomenon, that increases the
temperature within a city. In hotter climate that leads to uncomfortable outdoor spaces.
Research shows that vegetation and trees can help decrease the temperature (Shashua-
Bar et al. 2009). Current tools, for investigating the effect of vegetation on the microclimate
in the urban space, are not well suited in an integrated design process. The objective of
the thesis is to develop such a method, which evaluates the influence of vegetation on
thermal comfort in the microclimate and apply it to a case study in Abu Dhabi.

For that purpose, two models were developed: The Soil Model and The Atmosphere
Model. The Soil Model computes the evapotranspiration from the ground. It is implemented
as a wrapper around the Catchment Modelling Framework (Kraft et al. 2011). The
Atmosphere Model is a simple air volume model, that turns the evapotranspiration into
a change in air temperature and relative humidity. The two models are written in Python
and implemented in the parametric design tool Grasshopper. It has been demonstrated
how they can function in an analytic workflow with Ladybug Tools to compute outdoor
thermal comfort. The thermal comfort metric Universal Thermal Climate Index (UTCI)
was used to assess the thermal comfort.

A case study in Abu Dhabi, United Arab Emirates, was conducted. The case study was
20m times 22m site, with a wadi running through and five trees. The thermal comfort
was evaluated with the proposed method and compared to an assessment method that
neglects evapotranspiration. The results showed that an average reduction of 3.7°C
UTCI was present, when evapotranspiration was included. During the daytime of June
1st, the reduction would reach 15°C UTCI.

From this study it could be concluded that evapotranspiration has a substantial impact on
the thermal comfort in the microclimate and that it is possible include such an analysis in
an integrated design process.

Download: [Master Thesis]({filename}/data/Hygrotermic Control of the Microclimate Around Buildings.pdf)

Download: [Master Thesis Short Presentation]({filename}/data/master_thesis_slides.pdf)

 
 
## Bachelor Thesis: 
#### Ventileret facade på Union Canning - En analyse af fugt, skimmelsvamp, dagslys, energi og termisk indeklima

**ABSTRACT:** This bachelor thesis investigates moisture, mold, daylight, thermal comfort and energy in an internal insulated
wall and introduces a ventilated cavity to see if that will solve some of the, primarily, moisture and mold
issues an internal insulated wall has.

The investigations start by comparing 5 wall constructions with each other – 2 without a cavity and 3 with.
It shows that the construction where you have cavity with an air flow from the bottom of the wall, taking
in air from the indoor environment, to the top of the wall, with an outlet under the roof to the outside, has
the worst conditions for mold to grow in and with that also the lowest humidity in the construction. The
results also show that there only is a small difference between the three constructions with cavity in the
moisture and mold performance, but all three are superior to the constructions without cavity. Likewise are
the three superior to the other two, when it comes to thermal comfort and energy. Only the construction
without cavity and insulation has better daylight conditions than the rest, because the wall is thinner. To
check if the optimal construction is chosen the construction with the best moisture and mold performance
are varied by changing cavity and insulation thickness. No variation can be singled out as the best solution
based on the four performance criteria without further studies. The variation with 150mm cavity and 50mm
insulation seems at the moment as the most promising one.

During the work with this project a minor tool was developed to calculate and visualize driving rain on a
façade.

Download: [Bachelor Thesis (In Danish)]({filename}/data/Ventileret facade.pdf)

 
 
## Delphin 6 Automation 
**ABSTRACT:** Automation script for the hygrothermal simulation program Delphin 6 made under the EU research project, 
[RIBuild](http://ribuild.eu/).
The script make it possible to automate simulations and permutations of Delphin project files on a large scale.

Link to: [Delphin 6 Automation](https://github.com/ribuild/delphin_6_automation)
Title: LIVESTOCK
Date: 2018-04-30
Modified: 2018-09-02
Status: published
Slug: LIVESTOCK
Authors: Christian Kongsgaard

# LIVESTOCK
Livestock is a package for Grasshopper providing components for modelling water movement and hydrothermal effects 
around buildings to enable and evaluate sustainable solutions, where those effects are incorporated.

We have two focus areas: Surface Water Run-Off and Outdoor Thermal Comfort.
Livestock provides couplings to the hygrothermal modeling environment CMF as well as mesh capabilities used in Blender.
We are using CMF - [Catchment Modelling Framework](https://github.com/philippkraft/cmf) as our base for hydrological 
modelling. The hydrologic models can be used to investigate storm water management solutions at a high accuracy or 
be used as an input to an outdoor thermal comfort model.

Livestock aims at being a high performance package, by implementing the 
[Livestock Template Method (LTM)](https://ocni-dtu.github.io/how-is-it-working.html) for fast and scalable computations.
The LTM is a protocol and method to couple various CPython modules to Grasshopper. Livestock provides an easy way to 
read and write Python code back and forth between IronPython and CPython.

Livestock consists of a series of Grasshopper Python Script components and a 
underlying collection of Python scripts and a PyPI package

Livestock is the name of the plug-in for Grasshopper, that has been developed 
for the [master thesis](https://ocni-dtu.github.io/pages/portfolio.html) of Christian Kongsgaard. 
Livestock is currently being developed and maintained by Christian Kongsgaard and Kristoffer Negendahl. Livestock is 
under continuous development to provide validated analysis tools through the vast packages available on PyPI, Conda and 
elsewhere in the Open-Source world.

Livestock consists of a series of Grasshopper Python Script components and a underlying collection of Python scripts
 and a PyPI package.


# Examples
### Site Run-Off computed with Livestock
![alt text]({filename}/images/Livestock_CMF_Kinematic_wave_PZOO.gif)


### Getting Started with Livestock:
* [Background]({filename}/posts/background.md)
* [Install Livestock]({filename}/posts/install.md)
* [Tutorials]({filename}/pages/tutorials.md)



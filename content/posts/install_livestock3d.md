Date: 2018-04-30
Modified: 2018-06-26
Status: published
Authors: Christian Kongsgaard
Tags: python, livestock, install, grasshopper, first component, tutorial
Title: Install of Livestock Template Method
Summary: Guide to install the Livestock Package for the component tutorials.

If you already followed the instructions on the [Install]({filename}/posts/install.md) page. You can skip the top part of this page and go
directly to Download and Install Livestock3D in the bottom. Following these tutorials should not conflict with the
original installation of Livestock.


## Grasshopper Install
Livestock DOES NOT work without a valid installation of Grasshopper and Rhino.

## Anaconda Install
We recommend to download and install Anaconda as your Python package manager
[get it here](https://www.anaconda.com/download/)

Follow the instructions on their [page](https://docs.anaconda.com/anaconda/install/windows).

Remember to check the box with: "Add Anaconda to my PATH environment variable"

## Conda Environment
When Anaconda is install you are ready to create a conda environment. 
Open the command or Anaconda promt. Type in:

> conda create -n livestock_env python=3.6 numpy matplotlib

Conda will then install the environment called “livestock_env”, with Python 3.6 and NumPy. 
Afterwards the environment can be activated:

> activate livestock_env

## Download and Install Livestock3D

* Download the Livestock Grasshopper zip [here](https://github.com/livestock3d/livestock3d/archive/master.zip)
* Create a folder at %appdata%\McNeel\Rhinoceros\5.0\scripts called livestock3d
* Put the files from the folder "grasshopper" in there. 
* Create a folder called C:\livestock3d
* Put the files from the folder livestock3d there.
* Move the folder "Grasshopper Script" to a location of your choosing. 
* Put the files from "UserObjects" to the Grasshopper UserObjects folder.

## Create your first component!
[My First Component]({filename}/posts/first_component.md)
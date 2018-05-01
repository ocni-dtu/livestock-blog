Date: 2018-04-30
Modified: 2018-04-30
Status: published
Authors: Christian Kongsgaard
Tags: livestock, python, grasshopper
Title: Background for Livestock
Summary: Short introduction to the Livestock package and why it was created.

Each component is modelled as a placeholder with the Grasshopper Python Script for a Python class implementation of the component. 
This makes it possible to create and edit the components without having Grasshopper open, 
thus making it possible to use better Python editors than the build-in Grasshopper one – 
in this case PyCharm was used. Besides easing the workflow of this author, 
it also solves the problem of updating the components in the future. Some Grasshopper plug-ins such as 
Ladybug Tools (Sadeghipour Roudsari and Pak 2013), have written most of the source code directly in the 
Grasshopper Pythons Script components and every time an update is made or a bug is fixed the component 
has to be replaced with a newer version, which is troublesome. By having the Grasshopper component as a 
placeholder, this can be avoided. The only time a Livestock component should be replaced is when new 
inputs or outputs are added to the component, which is far less often, than when bug fixes are made.

As stated above Livestock also have a PyPI package – called livestock. At first this might sound a bit 
strange or as a duplicate of the Python scripts imported into Grasshopper – but it is not. 
The Grasshopper Python Script component runs IronPython, 
which is an implementation of Python for the .NET framework. IronPython comes as Python 2 and has long 
been undermaintained and developed. Standard Python or CPython is well maintained currently on version 
3.6. It goes without saying that CPython has undergone a lot development that IronPython has not 
and includes a whole bunch of new features. Furthermore, are the packages on PyPI mainly targeting 
CPython and many cannot be used in IronPython. This drastically decreases the usability the usability 
of the IronPython in the opinion of this author and very specific CMF cannot be ran from IronPython, 
therefore a CPython package and scripts are made. The CPython Livestock package – 
from now on mentioned as the Livestock package – is used when ever larger computations or CMF are needed.
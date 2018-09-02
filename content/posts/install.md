Date: 2018-04-30
Modified: 2018-09-02
Status: published
Authors: Christian Kongsgaard
Tags: python, livestock, install, grasshopper
Title: Install Livestock
Summary: Guide to install the Livestock Package.

Livestock is a plugin to [Grasshopper](http://www.grasshopper3d.com/) for [Rhino](https://www.rhino3d.com/). 
It is therefore an requirement that those two programs are installed for it to work. If they are install it 
should be pretty straight forward to install the rest.

### Grasshopper Dependencies

Livestock depends on ghPython, which is what makes it possible to create Python components in Grasshopper.
ghPython can be downloaded [here](http://www.food4rhino.com/app/ghpython)

**To Install**:
* In Grasshopper, choose File > Special Folders > Components folder. Save the gha file there.
* Right-click the file > Properties > make sure there is no "blocked" text
* Restart Rhino and Grasshopper

Livestock also explicitly depends on [Ladybug Tools](http://www.ladybug.tools/). 
They can be downloaded from [here](http://www.food4rhino.com/app/ladybug-tools).

### Download Livestock Grasshopper

Now you are ready to get Livestock installed!
All you need to do is to download this [zip](https://github.com/ocni-dtu/livestock_gh/archive/master.zip)

Download the latest [Livestock Release](https://github.com/livestock3d/livestock/releases)

* Create a folder at `%appdata%\McNeel\Rhinoceros\5.0\scripts` called `livestock`
* Put all the files from the folder "Python Rhino Script" in there.
* Create a folder at `%appdata%\Grasshopper\UserObjects` called `livestock`
* Put the files from the folder "Grasshopper User Objects" in there.
* Move the folder "Examples" to a location of your choosing. 
* On the C-drive create a folder called `livestock` as well. 

### Anaconda Install
Now when all th files for Grasshopper is in place it is time to complete the installation by installing CPython.
Livestock depend on Anaconda environments to run CPython. So it needs to be installed. If you already have Anaconda 
installed, you can just skip this part and go straight to setting up the Conda environment.  

Use this [link](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe) to download and install Miniconda.
Miniconda is the lightweight version of Anaconda. If you already installed Anaconda it is also fine. 
It will make no difference to the functionality of Livestock. 

Remember to check the box with: "Add Anaconda to my PATH environment variable, even if it prompts you with a warning. 
Second check box is optional"

### Conda Environment
When Anaconda is installed you are ready to create a conda environment specific to run Livestock. 
Open the command or Anaconda promt. (with adimin rights and you may need to turn off [sll verification](https://github.com/conda/conda/issues/6007#issuecomment-350348434))

Type in:
> conda create -n livestock_env python=3.6

Conda then will the install the environment called "livestock_env". Afterwards the environment can be activated:

> activate livestock_env

Your CPython 3.6 environment is now ready, however to make CPython talk to Grasshopper via the Livestock protocols we 
need to install the packages: [numpy](http://www.numpy.org/), 
[scipy](https://www.scipy.org/), [paramiko](http://www.paramiko.org/) and 
[shapely](https://github.com/Toblerity/Shapely) you may also install other packages such as 
[matplotlib](https://matplotlib.org/) or many other conda packages [Conda packages](https://anaconda.org/anaconda/repo) 
in this way:

> conda install numpy scipy shapely paramiko matplotlib

Your CPython 3.6 environment is almost ready, to take full advantage of the Livestock ecosystem we just need to use 
[pip](https://pypi.org/project/pip/) to install the Livestock CPython dependencies:

> pip install livestock

Just ignore any Cython related warnings.
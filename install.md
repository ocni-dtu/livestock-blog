# Install Livestock

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
They can be download from [here](http://www.food4rhino.com/app/ladybug-tools).

### Download Livestock Grasshopper

Now you are ready to get Livestock installed!
All you need to do is to download this [zip](https://github.com/ocni-dtu/livestock_gh/archive/master.zip)
In the zip there is a folder called grasshopper and in there is another folder called components. 
Take the files in components and drag them onto the Grasshopper Canvas. (The files will then be put in the right folder.)

Open explorer. Go to the location: *%appdata%\McNeel\Rhinoceros\5.0\scripts* and create a folder called livestock.
Put all the files from the subfolder in the zip called python into the livestock folder.

Go to the C-drive and create a folder called livestock as well.

### Anaconda Install
Now when all th files for Grasshopper is in place it is time to complete the installation by installing CPython.
Livestock depend on Anaconda environments to run CPython. So it needs to be installed. If you already have Anaconda 
installed, you can just skip this part and go straight to setting up the Conda environment.  

Use this [link](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe) to download and install Miniconda.
Miniconda is the lightweight version of Anaconda. If you already installed Anaconda it is also fine. 
It will make no difference to the functionality of Livestock. 

### Conda Environment
When Miniconda/Anaconda is install you are ready to create a conda environment. Open the command or Anaconda promt.
Type in:
> conda create -n livestock_env python=3.6 numpy scipy shapely paramiko

Conda then will the install the environment called "livestock_env". Afterwards the environment can be activated:

> activate livestock_env

And the CPython package for Livestock can be pip installed:

> pip install livestock

### Go Back
- [Main Page](/index.md)


Authors: Christian Kongsgaard
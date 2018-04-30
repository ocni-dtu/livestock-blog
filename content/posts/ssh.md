Date: 30-04-2018
Modified: 30-04-2018
Status: published
Authors: Christian Kongsgaard
Tags: livestock, tutorial, python, grasshopper, ssh
Title: SSH Graph Plotter Component
HeaderImage: /images/ssh_1.png
Summary: A tutorial on how to use the Livestock Template Method to create a Grasshopper component that will execute remotely over a SSH connection.

Welcome to the third tutorial! This tutorial will demonstrate how to create a SSH connection to a remote calculation machine.
The reason behind this, is that if you have very heavy computations, then you should be able to send them to a remote machine,
such as a high-end desktop, server or cloud service. Currently the Livestock SSH Method only support remote machines with 
Linux/Ubuntu as OS. If you do not have remote machine, then do not worry, you can still follow, this tutorial will work with
[Bash for Windows](https://docs.microsoft.com/en-us/windows/wsl/about). We will modify the second 
[tutorial]({filename}/posts/graph_plotter.md) so it does it processing on the remote machine instead of the local one.

## Installation
First you need to install Bash, follow this [guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
Configure your SSH connection:
```
sudo apt-get remove openssh-server
sudo apt-get install openssh-server
sudo nano /etc/ssh/sshd_config
```

Set the following:
- PermitRootLogin no
- Then add a line beneath it that says: AllowUsers USER (or whatever your username is for the linux subsystem)
- PasswordAuthentication yes
- UsePrivilegeSeparation no
- PubkeyAuthentication no
- RSAAuthentication no

```
sudo service ssh --full-restart
```

In some cases you have to modify Windows Firewall settings and add a new Rule for allowing incoming connections on Port 22.
Connect to your Linux subsystem from Windows using a ssh client like [PuTTY](https://www.putty.org/). 
Connect with PuTTY to make sure that the connection works.

We will use [Paramiko](http://www.paramiko.org/) to make the SSH connection. So let's go ahead and install it to our Conda
environment. Open the command promt or Anaconda promt:
```
activate livestock_env
conda install paramiko
```

## Grasshopper Script
Open "3 - SSH Graph Plotter.gh". In it you will find the Python Executor, the plotter component from before, the image viewer
and a SSH Connection component. 
![alt text](/images/ssh_1.png)
SSH Connection works similar to Python Executor it that it just collects and holds the information
concerning the SSH connection. You need to give it the IP, port, username and password for the SSH connection to work.
When you have done that, we can modify the plotter component.

We need to write a function, that can configure the files for the SSH connection: write_ssh_file():

```python
def write_ssh_files():
    # Clean SSH folder
    livestock3d.clean_ssh_folder()
 
    # SSH commands
    ssh_command = livestock3d.get_ssh()
 
    file_transfer = ['in_data.txt', 'plot_graph_template.py', 'data_file.txt']
 
    ssh_command['file_transfer'] = ','.join(file_transfer)
    ssh_command['file_run'] = 'plot_graph_template.py'
    ssh_command['file_return'] = 'plot.png'
    ssh_command['template'] = 'plot_graph'
 
    livestock3d.write_ssh_commands(ssh_command)
 
    return ssh_command
```
It first cleans up the ssh folder, to make sure there is not files from a previous run.
Then we collect the information from the SSH Connection component with get_ssh(). file_transfer is the files we want to
transfer to the remote machine. We want to transfer the plot_graph template and the data_file it needs. Besides that we
need to transfer in_data.txt, which is the configuration file for the ssh connection. We add that to the ssh_command variable.
ssh_command needs to know, which file should be run on the remote machine. We specify that in 'file_run'. The files we want
to return is given in 'file_return', this is typically the result files from the template, so in this case: 'plot.png'.
Lastly we set the template we use. Then write_ssh_commands is called. You can delete write_template(), we will not need that
as write_ssh_commands() writes the template for us.

clean_ssh_folder(), get_ssh() and write_ssh_commands() are located in the "ssh.py", which you should have gotten it 
with the initial download of Livestock3D. Make sure they are in the McNeel\Rhinoceros\5.0\scripts\livestock3d folder.
We also need to make a slight change to the execution part of the component:

````python
# Get CPython path from the other component
py = str(sc.sticky["PythonExe"])
 
# Make folder
folder = 'C:/livestock3d/ssh'
if not os.path.exists(folder):
    os.mkdir(folder)
 
# Specify paths 
txt_file = folder + '/data_file.txt'
template_file = folder + '/ssh_template.py'
result_file = folder + '/plot.png'
  
# Run functions
if run:
    #write_ssh_files()
    #write_file(txt_file, x)
    run_template(py, template_file)
```` 

- We change the folder to "C:\livestock3d\ssh"
- The template file should now be the ssh_template instead of the plot_graph.
- In the run statement we just need:
    - write_ssh_files()
    - write_file()
    - run_template()
   
The whole script in the component should look something like this:

```python
__author__ = "Christian Kongsgaard"
__license__ = "MIT"
 
#------------------------------------------------------------------------------#
# Imports
import os
import scriptcontext as sc
import subprocess
import livestock3d
 
#------------------------------------------------------------------------------#
# Functions
 
def write_file(file_path, x):
    file = open(file_path, 'w')
    
    for value in x:
        file.write(str(value) + '\n')
 
    file.close()
 
def write_ssh_files():
    # Clean SSH folder
    livestock3d.clean_ssh_folder()
 
    # SSH commands
    ssh_command = livestock3d.get_ssh()
 
    file_transfer = ['in_data.txt', 'plot_graph_template.py', 'data_file.txt']
 
    ssh_command['file_transfer'] = ','.join(file_transfer)
    ssh_command['file_run'] = 'plot_graph_template.py'
    ssh_command['file_return'] = 'plot.png'
    ssh_command['template'] = 'plot_graph'
 
    livestock3d.write_ssh_commands(ssh_command)
 
    return ssh_command
            
            
def run_template(py_exe, template_to_run):
    thread = subprocess.Popen([py_exe, template_to_run])
    thread.wait()
    thread.kill()
    
def load_file(file):
    file = open(file, 'r')
    lines = file.readlines()
    file.close()
    
    return lines
 
def print_lines(lines):
    for line in lines:
        print(line.strip())
        
        
#------------------------------------------------------------------------------#
# Execution
 
# Get CPython path from the other component
py = str(sc.sticky["PythonExe"])
 
# Make folder
folder = 'C:/livestock3d/ssh'
if not os.path.exists(folder):
    os.mkdir(folder)
 
# Specify paths 
txt_file = folder + '/data_file.txt'
template_file = folder + '/ssh_template.py'
result_file = folder + '/plot.png'
  
# Run functions
if run:
    #write_ssh_files()
    #write_file(txt_file, x)
    run_template(py, template_file)
```

## Template
Let us take a look at the SSH template in McNeel\Rhinoceros\5.0\scripts\livestock3d\templates.py

````python
def ssh_template(path):
    """
    Writes the ssh template.
 
    :param path: Path to write it to.
    """
 
    file_name = r'/ssh_template.py'
    file = open(path + file_name, 'w')
 
    file.write("# Imports\n")
    file.write("import sys\n")
    file.write("sys.path.insert(0, r'C:\livestock3d')\n")
    file.write("import ssh as ssh\n")
 
    file.write("# Run function\n")
    file.write("ssh.ssh_connection()\n")
 
    file.close()
 
    return True
````

It is similar to the two other templates, in that it imports a module (here ssh) and then calls a single 
function: ssh_connection(). ssh_connection() is the function that does all the SSH magic and it is there Paramiko comes into
play. You can go study it, if you want. It is located in "C:\livestock3d\ssh.py". Besides the SSH template, we also need
to modify the plot_graph template. When we are on the remote Ubuntu machine, the livestock3d folder is not located the same
place as on your on Windows one. Therefore we need to place a check to see if we are on Windows or Linux. We does this check
so you can still use the original plot_graph template on your Windows machine. We also need to add two lines after the template is finished.
The two lines creates an empty file called "out.txt". ssh_connection() will first start copying files back to the local machine
when it detects that "out.txt" is created. 

````python
def plot_graph(path):
    """
    Writes a template.
 
    :param path: Path to write it to.
    :type path: str
    :return: The file name
    """
 
    file_name = r'/plot_graph_template.py'
    file = open(path + file_name, 'w')
 
    file.write("# Imports\n")
    file.write("import sys\n")
    file.write("import platform\n")
    file.write("from pathlib import Path\n")
 
    file.write("system = platform.system()\n")
    file.write("if system == 'Windows':\n")
    file.write("    sys.path.insert(0, r'C:\livestock3d')\n")
    file.write("elif system == 'Linux':\n")
    file.write("    sys.path.insert(0, str(Path.home()) + '/livestock3d' )\n")
 
    file.write("import livestock3d as ls\n")
 
    file.write("# Run function\n")
    file.write("ls.plot_graph()\n")
 
    file.write("# Announce that template finished and create out file\n")
    file.write("print('Finished with template')\n")
    file.write("file = open('out.txt', 'w')\n")
    file.write("file.close()\n")
    file.close()
 
    return file_name
````

## On the Remote Machine

So far we have not installed Conda on the remote machine yet. You can do that by, in the terminal, typing in: 
````
wget -c http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
````

We also need a livestock_env environment. After the installation of Miniconda type in:
````
conda create -n livestock_env python=3.6 numpy matplotlib 
````

We also need to copy the files from "C:\livestock3d". If you are on Bash, you can do that by writing in the terminal:
````
cd ~/
cp -r /mnt/c/livestock3d ~/
````

Now the files are copied. Go into the livestock3d folder in Bash and check if all the files are there:
````
cd livestock3d
dir
````

It should return:
````
data  __init__.py  livestock3d.py  __pycache__  ssh  ssh.py
````

You should now be ready to run the component.

## Run Grasshopper
Remember to restart Rhino if you changed something in McNeel\Rhinoceros\5.0\scripts\livestock3d.
Make sure the Python Executor, SSH Connection is correctly sat up and then you can run the plotter component.
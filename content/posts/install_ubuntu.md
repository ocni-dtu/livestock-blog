Date: 2018-09-02
Modified: 2018-09-02
Status: draft
Authors: Christian Kongsgaard
Tags: ssh ubuntu livestock install
Title: Livestock Ubuntu
HeaderImage: /images/
Summary:

To enable high speed computation, Livestock have been made so it can run its computations on remote machines.
If you have a Ubuntu setup somewhere you can use that to direct your SSH connection at.
If not you need to install Bash for Windows. It is pretty easy just follow this [guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
Make sure to open Bash after the installation and update it. You can do that by:
> sudo apt-get update

> sudo apt-get upgrade

**Configure SSH**
When Bash is installed, you need to configure the SSH connection to it. Open Bash and do the following:

> sudo apt-get remove openssh-server

> sudo apt-get install openssh-server

> sudo nano /etc/ssh/sshd_config 

Set the following in sshd_config:

- PermitRootLogin no
- Then add a line beneath it that says: AllowUsers big (or whatever your username is for the linux subsystem)
- PasswordAuthentication yes
- UsePrivilegeSeparation no
- PubkeyAuthentication no
- RSAAuthentication no

> sudo service ssh --full-restart

Connect to your Linux subsystem from Windows using a ssh client like [PuTTY](https://putty.org/).

In some cases you have to modify Windows Firewall settings and add a new Rule for allowing incoming connections on Port 22.

**Install Miniconda**

To install Miniconda on your Ubuntu distribution, Bash or real, do the following:
Open Bash or your Ubuntu terminal.
> wget -c http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh 

> chmod +x Miniconda3-latest-Linux-x86_64.sh

> ./Miniconda3-latest-Linux-x86_64.sh

Follow the steps above to install the conda environment. The only thing that needs to be changed is the second command.
On Ubuntu Conda environments are activeted with "source activate", so do:
> source activate livestock_env
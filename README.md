# Git to YAML

This module is created with the intention of converting a git commit to yaml format. The metadata
from the git commit will be used to generate a yaml style item that can create a yaml file, or
append that entry to an already existing file. If we just checked in the `nsclient` module in puppet-core The end result should look something like this:

``` yaml
# puppetfile.yaml
modules:
  vscode:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/vscode
    ref: ab8a3d56d3c9ef957849206026de1dbaae050153
  nsclient:
    git: hurontfs@vs-ssh.visualstudio.com:v3/hurontfs/Puppet-Core/nsclient
    ref: as1e53gs8a74e35g4hyf53jki1ghk38gf7k531fg
```

This app adds an nsclient element in the `puppetfile.yaml` file with the new module
name, repo location (git) and commit hash (ref). Every update for that module from now 
on will update the ref to the most recent commit hash for that environment. The regular 
`Puppetfile` will then pick up this new entry and create a `mod <modulename>` statement dynamically
that will update the puppet-control repo to the most recent version. 

The ultimate goal is for this code to be used for puppet-control / puppet-core integrations. 
When a Puppet-Core module is updated, it will update the Puppetfile.yaml for the 
appropriate branch in Puppet-Control, 
and then kick of a puppet code deploy and puppet run for that environment. 
This will fully automate our puppet changes, and give full transparency of 
what is changing when just by looking at puppet-control.

## How to use

To use Run the full container this module the computer running it needs to have docker installed,
and to just run the source code python 3.0 or higher needs to be installed.

If you don't have docker it can be run in python mode by running the module folder and passing in commit information. an example

``` powershell
python3 C:\Users\rboley\Desktop\git\azure_devops\git_to_yaml\src\gityaml 'repo_name' '1235456789' 'C:\Users\rboley\Desktop\git\azure_devops\git_to_yaml\src\gityaml\test.yaml'
```

the first argument `repo_name` is the git repository name that needs to have the commit reference made. For example the check_ldapmodule.

Second is the commit reference that it should be pointing to next. this can be seen in the repo history, and is readily available in azure pipelines.

Third is the path to the yaml file that should be updated. this should be the full path.

## Development Setup

First your environment must have python and make.

### Windows

install pythom3, pip and make using chocolatey.

``` powershell
choco install python3 -y
choco install pip -y
choco install make -y
```

After installing those development tools, you can setup the project using:

``` powershell
make setup
```

That will create a virtual python environment and install all package dependencies in it. 
It should also activate the virtual environment in your terminal, 
so it should now have a (env) at the left, indicating you are in the virtual environment. 
Virtual environments let you install python packages in a contained environment so that you 
don't have packages of different versions on your machine interfering with your current 
development.

## Docker building and setup

This project has two docker images, a base and a dev image. The base image has the bare minimum required to run the app, and the test image has all the test dependencies installed as well. The dev image is based off the base image, so to get everything setup you need to build the base image, then the dev image and then can test the code.

### Base image setup

to build the base image change directory to \base folder and then run docker build.

``` powershell
cd base
docker build -t rboley/python-base .
```

That will create the base image named rboley/python-base. then to create the dev image.

### Dev image setup

To create the dev image it is pretty much the same, but it will be running from the project root since we need to have access to the src and scripts folders.

``` powershell
docker build -t gityaml-dev -f docker/dev/dockerfile .
```

That will build the dev image and name it gityaml-dev which doesn't have a repo in front of it since it is always just going to be a local image. The default state of this image is to run the tests, so next that is what we will do.

### Running the unit/integration tests in the dev image

To run the dev image:

``` powershell
docker run --rm gityaml-dev
```

This will run the dev image and execute the unit tests. You should see an output of all the tests that passed and failed.

To view the xml xunit test report mount the reports volume to somewhere on your local computer. For example:

``` powershell
docker run --rm -v C:\Users\rboley\Desktop\git\azure_devops\git_to_yaml\reports:/reports gityaml-dev
```

the `-v` means volume, which mounts the container drive to a place on your computer to be accessible, then the left hand side of the `:` is the local laptop location, and the right hand side is the container location. In the `dev\dockerfile` there is an explicit volume created called reports, and then in the cmd the nosetests.xml file is specified to be output in that reports directory. then by mapping it to your local computer it will show up there.


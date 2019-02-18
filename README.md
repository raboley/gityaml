# Git to YAML

This module is created with the intention of converting a git commit to yaml format. The ultimate goal is for this code to be used for puppet-control / puppet-core integrations. When a Puppet-Core module is updated, it will update the Puppetfile.yaml for the appropriate branch in Puppet-Control, and then kick of a puppet code deploy and puppet run for that environment. This will fully automate our puppet changes, and give full transparency of what is changing when just by looking at puppet-control.

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

That will create a virtual python environment and install all package dependencies in it. It should also activate the virtual environment in your terminal, so it should now have a (env) at the left, indicating you are in the virtual environment. Virtual environments let you install python packages in a contained environment so that you don't have packages of different versions on your machine interfering with your current development.

## Docker building and setup

This project has two docker images, a base and a dev image. The base image has the bare minimum required to run the app, and the test image has all the test dependencies installed as well. The dev image is based off the base image, so to get everything setup you need to build the base image, then the dev image and then can test the code.

### Base image setup

to build the base image change directory to \base folder and then run docker build.

``` powershell
cd base
docker build -t rboley/python-base .
```

That will create the base image namded rboley/python-base. then to create the dev image.

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
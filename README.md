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


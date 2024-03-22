#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/"

# put contents of your script here
echo "This script installs a Python distribution [3.11], an environment and the dependencies for ADA using conda. Please follow the instructions."
echo "Do you want to execute the installation script [yes/no]?"
read reply

if [ $reply == "yes" ]; then
    echo "Execute installation script."
    echo "Activate conda command"  
    echo "Source conda"
    source ~/anaconda3/etc/profile.d/conda.sh
    echo "Initialize conda"
    conda init
    # from https://stackoverflow.com/questions/70597896/check-if-conda-env-exists-and-create-if-not-in-bash
    if { conda env list | grep 'ada_env'; } >/dev/null 2>&1; then
      echo "Environment with the same name found and will be uninstalled. "
      yes "y" | conda remove --name ada_env --all
      echo "Environment sucessfully removed."

    else
      echo "Environment does not exist and will be installed."
    fi
    echo "Install ada environment"
    yes "y" | conda create --name ada_env Python=3.11
    echo "Activate ada environment"
    conda init
    conda activate ada_env
    echo "Install dependencies"
    yes "y" | pip3 install -r "$SCRIPT_DIR"requirements.txt
   echo "The installation script sucessfully finished. Press any key to exit"
   read junk
else
   echo "Installation aborted. Press any key to exit."
   read junk
fi

#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/"

if [ "$DISPLAY" != "" ]; then
   if [ "$1" != "--rex" -a "$2" != "--rex" ]; then
      konsole --nofork -e /bin/sh $0 --rex 2>/dev/null || xterm -e /bin/sh $0 --rex 2>/dev/null || /bin/sh $0 --rex 2>/dev/null
      exit
   fi
fi

# put contents of your script here
echo "This script installs a Python distribution [3.11], an environment and the dependencies for ADA using conda. Please follow the instructions."
echo "Do you want to execute the installation script [yes/no]?"
read reply

if [ $reply == "yes" ]; then
    echo "The installation script will be executed. Press any key to continue."
    read junk
    echo "Activate conda command"
    PATH_TO_CONDA=$( locate anaconda3/etc/profile.d/conda.sh )
    source $PATH_TO_CONDA
    conda init --all
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
    conda activate ada_env
    yes "y" | conda install -c conda-forge mamba
    echo "Install dependencies"
    yes "y" | mamba install -c conda-forge --file requirements.txt

fi

echo "The installation script sucessfully finished. Press any key to exit"
read junk

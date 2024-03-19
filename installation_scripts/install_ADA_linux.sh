#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/"

if [ "$DISPLAY" != "" ]; then
   if [ "$1" != "--rex" -a "$2" != "--rex" ]; then
      konsole --nofork -e /bin/sh $0 --rex 2>/dev/null || xterm -e /bin/sh $0 --rex 2>/dev/null || /bin/sh $0 --rex 2>/dev/null
      exit
   fi
fi

# put contents of your script here
echo This script installs a Python distribution [3.11], an environment and the dependencies for ADA using conda.
echo In order to follow the
echo Do you want to execute the installation script [y/n]?
read reply

if [ $reply == "y"]; do
    echo The installation script will be executed. Press y in every step.
    read junk
    source ~/anaconda3/etc/profile.d/conda.sh
    read junk
fi

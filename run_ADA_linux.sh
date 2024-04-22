#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/"

PATH_TO_CONDA=$( locate anaconda3/etc/profile.d/conda.sh )
source $PATH_TO_CONDA
conda init --all
conda activate ada_env
PATH_TO_ADA=$( locate adatool/src/main.py )
python $PATH_TO_ADA

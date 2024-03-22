#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh
conda init
conda activate ada_env
PATH_TO_ADA=$( mdfind -name adatool )
python "$PATH_TO_ADA"/src/main.py -style fusion

#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/"

source ~/anaconda3/etc/profile.d/conda.sh
conda activate ada_env
cd $SCRIPT_DIR
python src/main.py

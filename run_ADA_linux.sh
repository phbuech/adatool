#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/"
echo $SCRIPT_DIR

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dev2
cd $SCRIPT_DIR
python src/main.py

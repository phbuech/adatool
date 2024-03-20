import os
import numpy as np
import xarray as xr

import scipy as sp
import chardet
import pandas as pd


def write_TG_preamble(tmax,maxTier):
    line = "File type = \"ooTextFile\"\nObject class = \"TextGrid\"\n\nxmin = 0 \nxmax = "+str(tmax)+"\ntiers? <exists> \nsize = "+str(maxTier)+"\nitem []: \n"
    return line

def write_TG_segments(df,tmax,tier_index):
    line = "    item ["+str(tier_index+1)+"]:\n        class = \"IntervalTier\"\n        name = \""+df["tierName"][0]+"\"\n        xmin = 0\n        xmax = "+str(tmax)+"\n        intervals: size = "+str(len(df))+"\n"
    for i in range(len(df)):
        line += "        intervals ["+str(i+1)+"]:\n"
        line += "            xmin = "+str(df["tmin"][i])+"\n"
        line += "            xmax = "+str(df["tmax"][i])+"\n"
        if df["label"][i] == "nan":
            line += "            text = \"\"\n"
        else:
            line += "            text = \""+df["label"][i]+"\"\n"
    return line

def write_TG_points(df,tmax,tier_index):
    line = "    item ["+str(tier_index+1)+"]:\n        class = \"TextTier\"\n        name = \""+df["tierName"][0]+"\"\n        xmin = 0 \n        xmax = "+str(tmax)+"\n        points: size = "+str(len(df))+"\n"
    for i in range(len(df)):
        line += "        points ["+str(i+1)+"]:\n"
        line += "            number = "+str(df["tmin"][i])+"\n"
        line += "            mark = \""+df["label"][i]+"\"\n"
    return line

def export_annotation_to_TextGrid(directory,fname,annotation,landmark_tier_names):
    maxTier = len(annotation["tierName"].unique())
    tmax = annotation["tmax"].max()
    tiers = annotation["tierName"].unique()
    if os.path.isfile(directory+fname+".TextGrid"):
        os.remove(directory+fname+".TextGrid")
    tg = open(directory+fname+".TextGrid",mode="a",encoding="utf8")
    tg.write(write_TG_preamble(tmax,maxTier))
    for tier_idx in range(len(tiers)):
        if tiers[tier_idx] in landmark_tier_names:
            tmp_df = annotation[annotation["tierName"] == tiers[tier_idx]].reset_index(drop=True)
            tg.write(write_TG_points(tmp_df,tmax,tier_idx))
        else:
            tmp_df = annotation[annotation["tierName"] == tiers[tier_idx]].reset_index(drop=True)
            tg.write(write_TG_segments(tmp_df,tmax,tier_idx))
    tg.close()




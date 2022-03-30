#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
from psychopy import prefs
from psychopy import gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, STOPPED, FINISHED)
import numpy as np
from numpy.random import random, choice
from psychopy.hardware import keyboard
import pandas as pd
from collections import Counter
import random
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def copy_csv(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    df.to_csv('copy_of_' + filename)
copy_csv('AllBinned_IAPS_clean.csv')

df = pd.read_csv("copy_of_AllBinned_IAPS_clean.csv")
ds = df.sample(frac=1)

df1 =ds
selRows=[]
bin_list = []
for index, row in df1.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block1 = ds.loc[selRows]
block1["Block"] = 1
b1 = block1.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df2=ds
selRows=[]
bin_list = []
for index, row in df2.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block2 = ds.loc[selRows]
block2["Block"] = 2
b2 = block2.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df3=ds
from collections import Counter
selRows=[]
bin_list = []
for index, row in df3.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block3 = ds.loc[selRows]
block3["Block"] = 3
b3 = block3.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df4=ds
selRows=[]
bin_list = []
for index, row in df4.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block4 = ds.loc[selRows]
block4["Block"] = 4
b4 = block4.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df5=ds
selRows=[]
bin_list = []
for index, row in df5.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block5 = ds.loc[selRows]
block5["Block"] = 5
b5 = block5.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df6=ds
selRows=[]
bin_list = []
for index, row in df6.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block6 = ds.loc[selRows]
block6["Block"] = 6
b6 = block6.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df7=ds
selRows=[]
bin_list = []
for index, row in df7.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block7 = ds.loc[selRows]
block7["Block"] = 7
b7 = block7.sample(frac=1)

ds = ds[~ds['idx'].isin(selRows)]
df8=ds
selRows=[]
bin_list = []
for index, row in df8.iterrows(): 
    if ((row["Bin"])== 1):
        if Counter(bin_list)[1] < 5:
            selRows.append(index)
            bin_list.append(1)
    if ((row["Bin"])== 2):
        if Counter(bin_list)[2] < 5:
            selRows.append(index)
            bin_list.append(2)
    if ((row["Bin"])== 3):
        if Counter(bin_list)[3] < 5:
            selRows.append(index)
            bin_list.append(3)
    if ((row["Bin"])== 4):
        if Counter(bin_list)[4] < 5:
            selRows.append(index)
            bin_list.append(4)
    if ((row["Bin"])== 5):
        if Counter(bin_list)[5] < 5:
            selRows.append(index)
            bin_list.append(5)
    if ((row["Bin"])== 6):
        if Counter(bin_list)[6] < 5:
            selRows.append(index)
            bin_list.append(6)
block8 = ds.loc[selRows]
block8["Block"] = 8
b8 = block8.sample(frac=1)

blocksAll= pd.concat([b1,b2,b3,b4,b5,b6, b7, b8], axis=0)
blocksAll.to_csv("AllBlocks.csv")

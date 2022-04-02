import pandas as pd
import numpy as np

def build_x(r): 
    return r['image']

def build_y(r): return r['target']

def splitter(df):
    train = df.index[df['subset']=='T'].tolist()
    valid = df.index[df['subset']=='V'].tolist()
    return train,valid
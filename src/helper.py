import os
import pandas as pd

def count_na(data,col):
    return data[data[col].isna()].shape[0]
import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt

def get_data():
    start = dt.datetime(2021,1,1)
    end = dt.datetime(2021,6,1)
    data = web.DataReader("IBM",'yahoo', start, end).reset_index()
    return data
from .parameters.returnProbability import returnProbability;
from .tools.plotter import plotter;
from .tools.arraysorter import arraysorter;
import datetime as dt;
import numpy as np;
import pandas as pd;
import pandas_datareader.data as web;
import os;

def probCalc(start, dt):

    stocksSorted=[];
    df = pd.read_csv('options/top100.csv'); #can read in json, excel or more, look at pandas documentation
    numstocks = len(df['Symbol']);

    n=0;
    for x in range (0,numstocks):
        n=n+1;
        stocksSorted.append(returnProbability(df['Symbol'][x], dt));

    #sorting and plotting
    sortedArray = arraysorter(stocksSorted,n);
    for a in range(0, 10):
        plotter(sortedArray[a][0], dt, a);

def processtop100(start, dt):
    probCalc(start, dt);

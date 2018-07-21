
from .parameters.returnProbability import returnProbability;
from .tools.arraysorter import arraysorter;
from .tools.plotter import plotter;
import datetime as dt;
import numpy as np;
import pandas as pd;
import pandas_datareader.data as web;
import dateutil.parser;
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#purpose: 1) Validate results by printing data for individual stock

def probCalc(symblarray, dt):
     #symbol y/m/d
    stocksArray=[];
    n = 0;
    for symbol in symblarray:
        returnedtuple = returnProbability(symbol, dt);
        if(returnedtuple!=None):
            stocksArray.append(returnedtuple);
            n=n+1;


    arraySorted = arraysorter(stocksArray,n);

    for a in range(0, n):
        plotter(arraySorted[a][0], dt, a);





def processcustom(symblarray, dt):
    probCalc(symblarray, dt);

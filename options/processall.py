
from .tools.arraysorter import arraysorter;
from .parameters.returnProbability import returnProbability;
from .tools.plotter import plotter;
import datetime as dt;
import numpy as np;
import pandas as pd;
import pandas_datareader.data as web;


def probCalc(start, dt):
    stocksSorted=[];
    df = pd.read_csv('options/stocksymbols.csv'); #can read in json, excel or more, look at pandas documentation
    numstocks = len(df['Symbol']);
    n = 0;
    for x in range (0,numstocks):
        returnedtuple = returnProbability(df['Symbol'][x], dt);

        if returnedtuple is None:
            print("Null object detected");
        else:
            stocksSorted.append(returnedtuple);
            n=n+1;

    sortedArray = arraysorter(stocksSorted,10);

    for a in range(0, 10):
        plotter(sortedArray[a][0], dt, a);


def processall(start,dt):
    probCalc(start, dt);

    #ALBO-$32.55 x 2
    #ALLT-$5.26 x 15
    #DWCR-$28.67 x 2
    #BNTC-$2.75 x 29
    #BCAC-$10.04 x 7
    #CHEK-$3.73 x 21
    #CORT-$13.22 x 6
    #BREW-$19.55 x 4
    #GLDI-$8.31 x 9
    #USLV-$7.72 x 10 = 739.21 || 740.66

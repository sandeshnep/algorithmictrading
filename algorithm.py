#!/usr/bin/python3
import datetime as dt;
import numpy as np;
import pandas as pd;
import pandas_datareader.data as web;
import matplotlib.pyplot as plt;  #lets you make plots
from matplotlib import style;
import time;
start_time = time.time();
from datetime import datetime as date;
from options.processone import processone;
from options.processtop100 import processtop100;
from options.processall import processall;

def runalgorithm():

    option = 0;
    while(option<4):
        print('\n\nProgram starts here--------------------------\n\n');
        symdt = input('Enter startdate\n').split(' '); #symbol y/m/d
        startlist = symdt[0].split('/');

        start = date(int(startlist[0]),int(startlist[1]),int(startlist[2]));
        end = date.today();

        option = int(input('\n*Enter 1 to Input Symbols.\n*Enter 2 to process the Top-100 Stocks. \n*Enter 3 to process All the Stocks\n'));

        if(option==1):
            symdt = input('Enter symbol(s) saperated by whitespace:\n').split(' ');
            processone(symdt, start, end);
        else:
            if(option==2):
                processtop100(start, end);
            else:
                if(option==3):
                    processall(start, end);
                else:
                    return(0);


runalgorithm();

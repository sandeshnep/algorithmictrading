
import pandas_datareader.data as web;
import dateutil.parser;
import matplotlib.pyplot as plt;
import matplotlib.dates as mdates;
import pandas as pd;
import urllib.request;
from datetime import date;
import random;
#given a Symbol, start and end time, plots it.


def plotter(symbol, dt, styleno):

    formatstyles=['b-', 'g-', 'r-', 'c-', 'm-', 'y-', 'k-','b--', 'g--', 'r--', 'c--', 'm--', 'y--', 'k--'];


    url = 'https://api.iextrading.com/1.0/stock/'+ symbol + '/chart/' + dt;
    fp = urllib.request.urlopen(url);
    mybytes = fp.read();
    mystr = mybytes.decode("utf8");
    fp.close();
    pandasObj= pd.read_json(mystr);
    df = pd.DataFrame(data=pandasObj, columns=['close', 'date']);

    dfsize = len(df);


    #creating a two-dimensional array in python date, close_price
    closearray = df.get('close');

    #creating an array of properly formatted date from the string
    datearray=[];
    for item in range(0, dfsize):
        datearray.append(df['date'][item]);

    plt.plot_date(x=datearray, y=closearray, fmt=formatstyles[styleno], label=symbol);
    plt.title("Time Frame "  + str(dt));
    plt.ylabel("Close Price");
    plt.legend(loc='upper right');
    plt.grid(True);
    plt.show(block=False);

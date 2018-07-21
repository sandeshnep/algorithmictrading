#Author: Sandesh Paudel
#Function: Returns a list of closing prices based on the api response
import numpy as np;
import pandas as pd;
import urllib.request;
import pandas as pd;
import pandas_datareader.data as web;
import time;


def feedData(name, dt):
    try:
        url = 'https://api.iextrading.com/1.0/stock/'+ name + '/chart/' + dt;
        fp = urllib.request.urlopen(url);
        mybytes = fp.read();
        mystr = mybytes.decode("utf8");
        fp.close();
        pandasObj= pd.read_json(mystr);
        df = pd.DataFrame(data=pandasObj, columns=['close', 'date']);

    except urllib.error.HTTPError:
        print('HTTP Error');


    datasizeweb = len(df)+1;
    print(df.tail(10));
    close = list(df['close']);

    try:
        #getting the latest dynamic data--------------------------------------------
        url2 = 'https://api.iextrading.com/1.0/stock/'+ name + '/chart/dynamic';
        fp2 = urllib.request.urlopen(url2);
        mybytes2 = fp2.read();
        mystr2 = mybytes2.decode("utf8");
        fp2.close();
        pandasObj2= pd.read_json(mystr2);
        df2 = pd.DataFrame(data=pandasObj2, columns=['data']);
    except urllib.error.HTTPError:
        print('HTTP Error');

    #getting the latest closing price-------------------------------------------
    i=1;
    latestClose=0;
    df2size = len(df2);
    if(df2size>0):
        while((('close' in df2.loc[df2size-i][0]) is False) and ('marketClose' in df2.loc[df2size-i][0]) is False):
            print('inner loop');
            print(df2.loc[df2size-i][0]);
            i = i+1;
            if(i>df2size):
                break;


        if(i<=df2size): #if it doesnt go to negative index; that is, latest close exists
            if(('close' in df2.loc[df2size-i][0]) is True):
                latestClose = df2.loc[df2size-i][0]['close'];
            else:
                if(('marketClose' in df2.loc[df2size-i][0]) is True):
                    latestClose = df2.loc[df2size-i][0]['marketClose'];

            if(latestClose>0):
                print('[*]   '+ str(latestClose) + '    date    ' + str(df2.loc[df2size-i][0]['date']) + ' time    ' + str(df2.loc[df2size-i][0]['label']));
                close.append(latestClose);
        else:
            print('Latest Fetch Failed');

    return(close);

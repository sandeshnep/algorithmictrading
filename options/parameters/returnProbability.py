#Author: Sandesh Paudel
#Function: returns the probability of the stock's value going up the next day, using the probability calculation from consecutive ups and downs in the data;
import datetime as dt;
import numpy as np;
import pandas as pd;
import urllib.request;
import pandas as pd;
import pandas_datareader.data as web;
import time;
from .datafeed import feedData;

def returnProbability(name, dt):
    print('\n\nReturn Probability using the following parameters:\n');
    print('Name :' + name );

    #--------------------------------------------GETTING THE DATA FROM THE WEB
    close=feedData(name,dt);
    datasizeweb=len(close)+1;
    print('Size of data: ' + str(datasizeweb));


    #--------------------------------------------POPULATING THE LIST OF 1'S AND -1'S
    dataonelist=[];
    for n in range(1, datasizeweb):
        try:
            calc = (float(close[n]) - float(close[n-1]))/float((close[n-1]));
        except:
            break;

        if(calc>0):
            dataonelist.append(1);
        if(calc<0):
            dataonelist.append(-1);



    #-----------------------------------------FREQUENCYLISTS for POSITIVE and NEGATIVE
    listpos=[];
    listneg=[];

    dataonelistsize = len(dataonelist);

    for x in range(0, 20): #filling the list with 20 zero's. ASSUMPTION: there wont ever be 20 consecutives thats a good stock
        listpos.append(0);
        listneg.append(0);

    #--------------------------------------------POLULATING THE FREQUENCY LISTS WITH CORRECT FREQUENCIES OF OCCURENCES
    prev = 0;
    numconsecutive=0;

    for x in range(0, dataonelistsize):
        current = dataonelist[x];
        if(current==prev):
            if(current>0):
                numconsecutive = numconsecutive+1;
                for n in range(0, numconsecutive+1):
                    listpos[n] = listpos[n]+1;
            if(current <0):
                numconsecutive = numconsecutive+1;
                for n in range(0, numconsecutive+1):
                    listneg[n] = listneg[n]+1;
        else:
            if(current >0):
                listpos[0] = listpos[0] +1;
            else:
                if(current<0):
                    listneg[0] = listneg[0]+1;
            numconsecutive=0;

        prev = current;

    print("List Pos");
    print(listpos);
    print("List Neg");
    print(listneg);

    #-------------------------------------------CALCUATION OF LATEST DATA POINTS TO FIND LATESTCONSECUTIVE
    latestConsecutive = 0;
    if(dataonelistsize>2):
        index = dataonelistsize-1;
        latestConsecutive = dataonelist[index];
        change=0;
        while(change==0 and index>=0):
            current = dataonelist[index];
            prev = dataonelist[index-1]; #sth wrong here

            if(current==prev):
                latestConsecutive = current + latestConsecutive;
            else:
                change=1;
            index = index-1;

        print("\nLatest Consecutive :" + str(latestConsecutive) +'\n');




    #--------------------------------------PRINTS POSITIVE PROBABILITIES FROM LISTPOS, ADDS BEST NTH
    n=0;
    if(latestConsecutive>0):
        for n in range(1, dataonelistsize):

            highlight='';

            if(listpos[n]!=0):
                #print('positive inner loop');
                prob = listpos[n]/listpos[n-1];
                data=[name, prob, listpos[n], latestConsecutive];

                if(n==latestConsecutive):
                    highlight=">>>>>>";
                    print(highlight + "+Probability of " + str((n+1)) +"th consecutive positive. Probability: " + str(round(prob,2)));
                    return(data);
                else:
                    print(highlight + "+Probability of " + str((n+1)) +"th consecutive positive. Probability: " + str(round(prob,2)));

            else: #case: when the next positive never happened, 0
                highlight=">>>>>>";
                prob = 0;
                data=[name, prob, listpos[n], latestConsecutive];
                print(highlight + "+Probability of " + str((n+1)) +"th consecutive positive. Probability: " + str(round(prob,2)));
                return(data);


    #-------------------------------------PRINTS NEGATIVE PROBABILITIES FROM LISTPOS, ADDS BEST NTH
    print("\n\n");

    if(latestConsecutive<0):
        n=0;
        for n in range(1, dataonelistsize):

            highlight='';

            if(listneg[n]!=0):

                prob = 1-(listneg[n]/listneg[n-1]);
                data=[name, prob, (listneg[n-1]-listneg[n]), latestConsecutive];


                if(n==-1*latestConsecutive):
                    highlight=">>>>>>";
                    print(highlight + "-Probability of " + str((n+1)) + "th positive. Probability : " + str(round((prob),2)));
                    return(data);
                else:
                    print(highlight + "-Probability of " + str((n+1)) + "th positive. Probability : " + str(round((prob),2)));

            else:
                highlight=">>>>>>";
                prob = 1;
                data=[name, prob, listpos[n-1], latestConsecutive];
                print(highlight + "-Probability of " + str((n+1)) +"th consecutive positive. Probability: " + str(round(prob,2)));
                return(data);

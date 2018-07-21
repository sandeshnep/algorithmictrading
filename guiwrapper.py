#!/usr/bin/python3
from tkinter import *;
from options.processcustom import processcustom;
from options.processtop100 import processtop100;
from options.processall import processall;
from datetime import datetime as date;
from datetime import timedelta;

root= Tk();
root.geometry("400x180");


radiobtnframe = Frame(root);
radiobtnframe.pack(side=LEFT);

var = IntVar();
var.set(1);

#ENTRY HERE

R0 =  Radiobutton(radiobtnframe, text = "Enter Stocks", variable = var, value = 0);
R0.pack(anchor =W);

E1 = Entry(radiobtnframe);
E1.insert(END, "AAPL AMZN");
E1.pack(side=TOP);

R1 = Radiobutton(radiobtnframe, text = "Top100 Stocks", variable = var, value = 1);
R1.pack(anchor =W);

R2 = Radiobutton(radiobtnframe, text = "All the stocks", variable = var, value = 2);
R2.pack(anchor =W);




timeselect= Frame(root);
timeselect.pack(side=LEFT);
var2 = IntVar();
var2.set(2);


R1 = Radiobutton(timeselect, text = "1 month", variable = var2, value = 1);
R1.pack(anchor =W);
R8 = Radiobutton(timeselect, text = "3 months", variable = var2, value = 2);
R8.pack(anchor =W);

R2 = Radiobutton(timeselect, text = "6 months", variable = var2, value = 3);
R2.pack(anchor =W);
R3 = Radiobutton(timeselect, text = "1 year", variable = var2, value = 4);
R3.pack(anchor =W);
R4 = Radiobutton(timeselect, text = "2 years", variable = var2, value = 5);
R4.pack(anchor =W);
R5 = Radiobutton(timeselect, text = "5 years", variable = var2, value = 6);
R5.pack(anchor =W);




def runalgorithm():
    dt = timedelta(days=0);
    end = date.today();

    start = 0;

    if(var2.get()==1):
        dt ='1m';
    else:
        if(var2.get()==2):
            dt ='3m';
        else:
            if(var2.get()==3):
                dt='6m';
            else:
                if(var2.get()==4):
                    dt='1y';
                else:
                    if(var2.get()==5):
                        dt='2y';
                    else:
                        if(var2.get()==6):
                            dt='5y';



    if(var.get()==1):#top100 stocks
        processtop100(start, dt);
    else:
        if(var.get()==2):
            processall(start, dt);
        else:
            if(var.get()==0):
                symdt = E1.get().split(" ");
                processcustom(symdt, dt);






frame=Frame(root);
frame.pack(side=BOTTOM);

redbutton = Button(frame, text="Go",command = runalgorithm);
redbutton.pack(side=LEFT);
root.title("Stock Analysis");


root.mainloop();

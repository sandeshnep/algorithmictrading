from operator import itemgetter;

# sorts a given array with the probability and prints upto printsize, checks the 1st index
def arraysorter(array, printsize):
    print('\n\nSORTED LIST OF SYMBOLS FROM BEST TO WORST-------------------\n');
    #bestnthsize = len(bestnth);
    bestnthsize = len(array);

    arraySorted = sorted(array, key= itemgetter(1), reverse=True);#lambda prob : prob[1], reverse = True);

    for n in range(0,printsize):
         print(arraySorted[n]);

    return(arraySorted);

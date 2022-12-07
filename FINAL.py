import matplotlib.pyplot as mpl
import numpy as np
import os
from ALLFUNCTIONS import *
#imports my functions which I will use a lot below, has information on how to make graphs and other information
Bluejaysdata = open("BlueJaysdata.csv")
bluejayspitchersdata = open("bluejayspitchersdata.csv")
bluejayshitterssdata = open("bluejayshittersdata.csv")
#opens my 3 csv files which i use for my data collection and visualization

enter = True
#basis of a while loop. when a variable is equal to something, it will keep on running. Once the variable isn't true any more, it breaks out of the loop.
while enter:
    print("Hello and welcome to Michael's baseball tutorial! \nWould you like to learn about team, pitching or hitting stats?")
    typeofstat = input("Please enter T for team, P for pitching or H for hitting in uppercase: ")
    #simple introduction to my product and allows for the user to choose if he wants to learn about pitching, hitting or team stats, three main categories in baseball. I used T P and H and there is less chance of a typo, and the user can procede directly to the next section.
    if typeofstat == "T":
        enter = False
        #if the user types T for team stats, enter becomes false and we break out of the while loop. We then run these 2 functions back to back which will produce a graph.
        teamstat = teamfunction()
        teamgraph = teamgraphfunction()
    elif typeofstat == "P":
        enter = False
        #if the user types P for pitching stats, enter becomes false and we break out of the while loop. We then run these 2 functions back to back which will produce a graph.
        pitchingstat = pitchingfunction()
        pitchinggraph = pitchinggraphfunction()
        
    elif typeofstat == "H":
        enter = False
        #if the user types H for hitting stats, enter becomes false and we break out of the while loop. We then run these 2 functions back to back which will produce a graph.
        hittingstat = hittingfunction()
        hittinggraph = hittinggraphfunction()
    else:
        #if the user types something other than H, P or T, and made a typo, another prompt comes out to direct the user in the right direction. The while loop does not 'break' here.
        print("\nPlease enter T for team, P for pitching or H for hitting in uppercase. Thanks!")


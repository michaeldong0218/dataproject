import matplotlib.pyplot as mpl
import numpy as np
import os
#importing libraries which will help me show my graphs and visualize my data
Bluejaysdata = open("BlueJaysdata.csv")
bluejayspitchersdata = open("bluejayspitchersdata.csv")
bluejayshitterssdata = open("bluejayshittersdata.csv")
#opens my 3 csv files which i use for my data collection and visualization

def pitchingfunction():
    #this function runs when the user chooses 'P'. we have a while loop here. The purpose of this function is for the user to choose a pitching statistic in baseball to learn more about.
    stat = ""
    enter = True
    while enter: 
        print("\nHere are some common pitching stats: \nW,L,W-L%,ERA,G,GS,GF,SV,IP,H,R,ER,HR,BB,IBB,SO,HBP,BK,WP,BF,ERA+,FIP,WHIP,H9,HR9,BB9,SO9,SO/W" )
        a = ("W,L,W-L%,ERA,G,GS,GF,SV,IP,H,R,ER,HR,BB,IBB,SO,HBP,BK,WP,BF,ERA+,FIP,WHIP,H9,HR9,BB9,SO9,SO/W")
        #First write all the stats out, then write the stats again in a string. we then split the string so then the input can later be read and used in if/else statements.
        statslist = a.split(",")
        stat = input("What stat do you want to look for? Please type one of the previous: ")
        if stat not in a:
            print("Please type in one of the pitching stats! Thanks \n")
            #if the input is not entered correctly or theres a typo, a prompt shows up and allows the user to enter a stat again.
        else: 
            enter = False
            #breaks out of the loop and proceeds on towards the next function.
    return stat
#-----------------------------------------------------------------------------------------------------
def hittingfunction():
    #this function runs when the user chooses 'P'. we have a while loop here. The purpose of this function is for the user to choose a hitting statistic in baseball to learn more about.
    stat = ""
    enter = True
    while enter: 
        print("\nHere are some common hitting stats: \nG,PA,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB" )
        a = ("G,PA,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB")
        #First write all the stats out, then write the stats again in a string. we then split the string so then the input can later be read and used in if/else statements.

        statslist = a.split(",")
        stat = input("What stat do you want to look for? Please type one of the previous: ")
        if stat not in a:
            print("Please type in one of the hitting stats! Thanks \n")
            #if the input is not entered correctly or theres a typo, a prompt shows up and allows the user to enter a stat again.

        else: 
            enter = False
            #breaks out of the loop and proceeds on towards the next function.

    return stat
#-----------------------------------------------------------------------------------------------------
def teamfunction():
    #this function runs when the user chooses 'P'. we have a while loop here. The purpose of this function is for the user to choose a team statistic in baseball to learn more about.
    stat = ""
    enter = True
    while enter: 
        print("\nHere are some common team stats: \nW,L,T,W-L%,,GB,R,RA,Attendance")
        a = ("W,L,T,W-L%,,GB,R,RA,Attendance")
        #First write all the stats out, then write the stats again in a string. we then split the string so then the input can later be read and used in if/else statements.

        statslist = a.split(",")
        stat = input("What stat do you want to look for? Please type one of the previous: ")
        if stat not in a:
            print("Please type in one of the team stats! Thanks \n")
            #if the input is not entered correctly or theres a typo, a prompt shows up and allows the user to enter a stat again.

        else: 
            enter = False
            #breaks out of the loop and proceeds on towards the next function.

    return stat
#-----------------------------------------------------------------------------------------------------
def pitchinggraphfunction():
    #This function runs after pitchingfunction(). The purpose of this function is to take the stat from pitchingfunction() and to create a graph based on that stat.
    headerString = bluejayspitchersdata.readline()
    #reads the first line of the file and saves in our variable
    headerList = headerString.split(",")
    namelist = []
    #for every row in our csv, read the line and store the string in a list
    for line in bluejayspitchersdata.readlines():
        columns = line.split(",")
        #a list of each column in an individual row
        nameDictionary = {}
        #a dictionary to hold each column's data in a row
        #each row's data is one season
        for index in range(len(columns)):
            #for each index in our list of columns
            #index will be equal to 0, 1, 2, 3, ... len(columns)'
            #index our dictionary with our header
            #fill the value with our data from the column
            nameDictionary[headerList[index]] = columns[index]

        namelist.append(nameDictionary)

    mpl.style.use('ggplot')
    #from matplotlib, changes to a different style sheet with a different colour scheme
    np.random.seed(4)

    sizes = np.random.uniform(15, 80, len(namelist))
    colors = np.random.uniform(15, 80, len(namelist))

    x = []
    y = []
    stat = pitchingfunction()
    #where the previous function is called, with it being equal to stat. then runs a for loop where we can get the y and x values, from going down the name column and getting the players name and stat chosen.
    for name in namelist:
        y.append(float(name[stat]))
        x.append(name["Name"])
    fig, ax = mpl.subplots()
    ax.bar(x, y)
    ax.set_xlabel("Name")
    ax.set_ylabel(stat)
    ax.set_title(stat + ' per pitcher for the Toronto Blue Jays')
    mpl.xticks(fontsize = 10, ha = 'right', rotation = 25)
    #rotates the text for each x value so then the text doesn't go over each other.
    mpl.subplots_adjust(bottom=0.215)
    mpl.rc('axes')
    os.system('say These are the 2022 '+ stat  +' for each pitcher of the Toronto Blue Jays.')
    #a text to speech system which reads the text and says it out loud. While the graph is generating, The text to speech serves as an introduction to what the graph would show and its details.
    mpl.show()
    #shows the graph
#-----------------------------------------------------------------------------------------------------
def hittinggraphfunction():
    headerString = bluejayshitterssdata.readline()
    #reads the first line of the file and saves in our variable
    headerList = headerString.split(",")
    namelist = []
    #for every row in our csv, read the line and store the string in a list
    for line in bluejayshitterssdata.readlines():

        columns = line.split(",")
        #a list of each column in an individual row

        nameDictionary = {}
        #a dictionary to hold each column's data in a row
        #each row's data is one season
        for index in range(len(columns)):
            #for each index in our list of columns
            #index will be equal to 0, 1, 2, 3, ... len(columns)'
            #index our dictionary with our header
            #fill the value with our data from the column
            nameDictionary[headerList[index]] = columns[index]

        namelist.append(nameDictionary)

    mpl.style.use('Solarize_Light2')
    #from matplotlib, changes to a different style sheet with a different colour scheme
    np.random.seed(4)

    sizes = np.random.uniform(15, 80, len(namelist))
    colors = np.random.uniform(15, 80, len(namelist))

    x = []
    y = []
    stat = hittingfunction()
    #where the previous function is called, with it being equal to stat. then runs a for loop where we can get the y and x values, from going down the name column and getting the players name and stat chosen.
    for name in namelist:
        y.append(float(name[stat]))
        x.append(name["Name"])
    fig, ax = mpl.subplots()
    mpl.xticks(fontsize = 10, ha = 'right', rotation = 25)
    #rotates the text for each x value so then the text doesn't go over each other.
    mpl.subplots_adjust(bottom=0.215)
    mpl.rc('axes')
    ax.bar(x, y)
    ax.set_xlabel("Name")
    ax.set_ylabel(stat)
    ax.set_title(stat + ' per hitter for the Toronto Blue Jays')
    os.system('say These are the 2022 '+ stat  +' for each hitter of the Toronto Blue Jays.')
    #a text to speech system which reads the text and says it out loud. While the graph is generating, The text to speech serves as an introduction to what the graph would show and its details.
    mpl.show()
    #shows the graph
#-----------------------------------------------------------------------------------------------------

def teamgraphfunction():
    headerString = Bluejaysdata.readline()
    #reads the first line of the file and saves in our variable
    headerList = headerString.split(",")
    seasonList = []
    #for every row in our csv, read the line and store the string in a list
    for line in Bluejaysdata.readlines():

        columns = line.split(",")
        #a list of each column in an individual row

        seasonDictionary = {}
        #a dictionary to hold each column's data in a row
        #each row's data is one season
        for index in range(len(columns)):
            #for each index in our list of columns
            #index will be equal to 0, 1, 2, 3, ... len(columns)'
            #index our dictionary with our header
            #fill the value with our data from the column
            seasonDictionary[headerList[index]] = columns[index]

        seasonList.append(seasonDictionary)

    mpl.style.use('grayscale')
    #from matplotlib, changes to a different style sheet with a different colour scheme

    np.random.seed(4)

    sizes = np.random.uniform(15, 80, len(seasonList))
    colors = np.random.uniform(15, 80, len(seasonList))

    x = []
    y = []
    stat = teamfunction()
    #where the previous function is called, with it being equal to stat. then runs a for loop where we can get the y and x values, from going down the name column and getting the players name and stat chosen.

    for season in seasonList:
        y.append(float(season[stat]))
        x.append(season["season"][0:4])
    fig, ax = mpl.subplots()
    mpl.xticks(fontsize = 7, ha = 'right', rotation = 40)
    #rotates the text for each x value so then the text doesn't go over each other.
    mpl.subplots_adjust(bottom=0.215)
    mpl.rc('axes')
    ax.bar(x, y)
    ax.set_xlabel("Year")
    ax.set_ylabel(stat)
    ax.set_title(stat + ' by Year for the Toronto Blue Jays')
    os.system('say These are the total amount of '+ stat  +' in each year in the history of the Toronto blue jays.')
    #a text to speech system which reads the text and says it out loud. While the graph is generating, The text to speech serves as an introduction to what the graph would show and its details.

    mpl.show()   
    #shows the graph
 
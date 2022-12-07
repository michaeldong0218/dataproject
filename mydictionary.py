import os
baseballDict = {"Hit":"When a batter hits the ball and reaches on base without an error", 
          "Single":"A hit where the batter reaches first base ",
          "Double":"A hit where the batter reaches second base",
          "Triple":"A hit where the batter reaches third base",
          "Home Run":"A hit that where the ball is struck over the fence",
          "Runs":"When a player crosses home plate, a run is tallied. By the end of nine innings, the team with more runs win shte game.",
          "RBIs":"A run batted in is credited to a batter when the result of his plate appearance ends up in a run scored.",
          "Stolen Bases":"When a baserunners advances a base when the pitcher throws a pitch or during a pickoff.",
          "Walk":"When a pitcher throws four balls in a plate appearance, the batter is awarded first base.",
          "Hit-by-pitch": "When a batter gets hit by a pitch without swinging, the batter is awarded first base",
          "Batting Average":"A player's hits divided by their total at-bats, one of the most commonly used statistics in baseball",
          "On-Base Percentage": "On Base percentage is how often a batter reaches base. Similar to Batting average, on base percentage is calculated by hits + walks + hit by pitches over plate appearances",
          "Slugging Percentage": "Slugging Percentage is a batter's total number of bases divided by their number of at-bats",
          "On-Base Plus Slugging ": "As it sounds, On-Base Plus Slugging is when you add a player's On-Base Percentage and their Slugging Percentage ",
          "Strikeout":"When a pitcher throws 3 strikes to a batter, without a foul in the third strike ",
          "Strike":"A pitch that is thrown in the strike zone or a pitch that is swung at by the batter ",
          "Ball": "A pitch outside the strike zone that is not swung at by the batter",
          "At Bat":"An At-Bat occurs when a batter a batter gets a hit, reaches on an error or gets out.",
          "Plate Appearance": "A Plate Apperance refers to a batter turn at the plate. Each time a batter's turn at the plate ends, that counts as a plate apperance. The difference between a plate appearance and an at-bat is that plate appearances also count walks and hit-by-pitches, while an at-bat does not.",
          "Total Bases": "",
          "Error": "Fielders get charged with errors if they fail to convert a play that the average fielder should have made. Types of errors that can be made include throwing, fielding and tagging errors.",

           "Win": "A win is awarded to a pitcher when he is the pitcher while his team takes the lead for good. Starting pitchers must pitch a minimum of five innings to recieve a win, while relieving pitchers are awarded wins when they are pitching while their team takes the lead. Wins are paired with Losses to create a Win-Loss Record. ",
           "Loss": "A loss is awarded to a pitcher when that pitcher gives up a go-ahead run which is never taken back. Losses are paired with Wins to create a Win-Loss Record ",
           "Earned Runs":"An earned run is any run that is scored without the benefit of an error or passed ball. If a pitcher exits a game with runners on base, any earned runs scored by those runners will count against him.",
           "Earned-Run Average": "Earned Run Average, or ERA, is the number of earned runs allowed per nine innings. ERA is the most commonly used pitching statistic.",
           "WHIP": "WHIP stands for Walks plus Hits per Innings Pitched, which shows how well a pitcher is on keeping batters of the basepaths. To calculate WHIP, we add up a pitcher's walks and hits and divide it by their innings pitched.",
           "Saves": "A save is awarded to a relief pitcher who finishes a game for the winning team, under certain circumstances. The pitcher must finish the game while preserving a lead of 3 or under or pitch at least 3 innings. Teams usually have a closer who finishes close games for them.",
           "Appearance": "A pitcher is credited with an appearance when he enters a game and throws a pitch. Relief Pitchers tend to have more appearances than starting pitchers as they pitch for less innings, allowing them to recover quicker and pitch in more games. ",
           "Quality Start": "",
           "Innings Pitched":" Innings pitched measures the number of innings a pitcher pitches in a game. With there being three outs per inning, each out recorded represents one-third of an inning pitched.",
           "Hold": "A hold occurs when a reliever enters a game in a save situation and mantains the lead for the next pitcher while recording at least one out. One of two conditions must be met for a pitcher to record a hold: He enters with a lead of three runs or less and maintains that lead while recording at least one out. Or He enters the game with the tying run on-deck, at the plate or on the bases, and records an out. A pitcher can only be awarded one of a save, hold or win.",
           "Starting Pitcher":"A starting pitcher or starter is the pitcher that starts the game. Starting Pitchers are expected to pitch for a significant portion of a game, and usually rest four or more days before pitching again.",
           "Relief Pitchers":"A Relief pitcher or reliever is a pitcher that comes into the game after the starting pitcher. Relief pitchers are expected to go for shorter portions of a game, usually ranging from one to three innings. Relief pitchers are then divided into roles, such as closers, setup men, specialists, middle relievers and long relievers."
           }
#a dictionary for the statistics of baseball. 
print(baseballDict.keys())

for stat in baseballDict.keys():
    print(stat)

# myDict = {"cheese":"tasty milk solid", "milk":"water cheese", "yogurt":"sour milk"}

# word = input("Please enter a word: \n")
# while not word == "exit":
#     word = input("Please enter another word: \n")
#     if word in myDict.keys():
#         print(myDict[word])
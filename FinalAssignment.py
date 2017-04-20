#### CMPT 120
#### D200
#### Planets, Aliens and Explosions Game
#### game copyright - Gregory Levkine, Julian Katz
#### authors: Julian Katz, Gregory Levkine

# Imports that are necessary for the program
import random as r

# -------------------------
# |                       |
# |  Function Definition  |
# |                       |
# -------------------------

# Appens PythonPlanet to the value the user inputs
# if 0, nothing happens
def python_planet():                    # only in main loop, not turn loop
    posPythPlanet = input("Which position shall PythonShine be (0..7), 0 no effect: ")
    while(not posPythPlanet.isdigit()):
        print("What you typed is not a positive integer, please retype")
        print()
        posPythPlanet = input("Which position shall PythonShine be (0..7), 0 no effect: ")
    while(int(posPythPlanet) > 7 or int(posPythPlanet) < 0):
        print(" The value is not within the required range, retype")
        print()
        posPythPlanet = input("Which position shall PythonShine be (0..7), 0 no effect: ")
        while(not posPythPlanet.isdigit()):
            print("What you typed is not a positive integer, please retype")
            print()
            posPythPlanet = input("Which position shall PythonShine be (0..7), 0 no effect: ")
    x = int(posPythPlanet)
    if(x == 0):
        print()
        return 100
    else:
        planetList[x].append("<=== PythonPlanet ")
        return posPythPlanet

# Function that is called when the astronaut arrives to a planet
# Compares the civilization level of the astronaut versus the aliens on the planet
# And does a series of conditions based on whether or not the astronaut has a higher
# civilization value
# It also makes the astronaut collect the rocks when he is on the planet
def civi_checker(astro_civ, astroPosition, astroFuel):
    x = astro_civ
    y = astroPosition
    z = astroFuel
    a = 0
    c = 0                # output fuel
    k = planetList[y][1] # planet civilisation level
    b = planetList[y][2] # planet fuel level
    d = planetList[y][3] # planet rocks

    if(b==0):
        print("There is no fuel on this planet.")
        print()
        print("The astronaut now has " + str(z) + " fuel liters")
        print()
        c = z
    else:
        if planetList[y][1] == 0 or x > planetList[y][1]:
            a = r.randint(1,b)  # fuel
            print("There are aliens in this planet!! with civilization level " + str(k))
            print()
            print("Great! the astronaut is more civilized than the aliens!")
            print()
            print("The astronaut won " + str(a) + " fuel liters")
            c = z + a       
            z = b - a
            planetList[y][2] = z
            print("the planet " + str(y) + " now has " + str(z) + " fuel liters")
            print()
            print("The astronaut now has " + str(c) + " fuel liters")
            print()
        elif planetList[y][2] == x:
            a = r.randint(1,(.5*z))
            print("There are aliens in this planet!! with civilization level " + str(k))
            print()
            print("Oh well... the astronaut is equally civilized as the aliens")
            print(" but lost " + str(a) + " fuel liters")
            c = z - a
            print("the planet " + str(y) + " now has " + str(z) + " fuel liters")
            print()
            print("The astronaut now has " + str(c) + " fuel liters")
            print()
        else:
            a = r.randint(1,z)
            print("There are aliens in this planet!! with civilization level " + str(k))
            print()
            print("Oh well... the astronaut is less civilized than the aliens")
            print(" but lost " + str(a) + " fuel liters")
            c = z - a
            print()
            print("The astronaut now has " + str(c) + " fuel liters")
            print()
           
    if (c > 0):
        e = d//3                                                        # number of rocks collected
        print("Yey!!...  the astronaut collected " + str(e) + " rocks")
        f = d - e                                                       # rocks left on planet
        planetList[y][3] = f
        astroRockSpecimen.append(e)
        print("his rock collection is now " + str(astroRockSpecimen))
        print("the planet " + str(y) + " now has " + str(f) + " rocks")
        print()
    return c # make sure astroFuel = civi_checker() when calling function
             # have to make sure there is enough fuel to play

# Asks for the user to roll dice or to use their own input
# Conditions in place to make sure input is correct
def advance(num_of_planets, position, d_or_u):
    x = num_of_planets
    z = position
    y = d_or_u
   # x = number of planets in list
    if y == "d":
        pos = r.randint(1,6)
        print(" the die was...", pos)
        print(" the previous position was...", z)
        print(" and the next position was..", ((pos + z)% x))
        print()
        print()
        print()
    else:
        num = input(" Which planet should the astronaut go? ")
        print()
        print()
        while num.isdigit() == False or int(num) > x - 1:
           print("The list of available planets is between 0 and",x-1)
           num = input("We need an integer value in our range of planets. Please give a planet number")       
        else:
            pos = num                
    return pos # this is the number of the movement we input into astronaut mover

# Converts rock specimen list to a list
# of 1's and 0's based on whether
# the values are odd or even
def obtain_list_0s_1s(lint):
	lbin = []
	for i in range(len(lint)):  
		lbin.append(lint[i] %2) 
	return lbin

# Converts a list of ones and zeroes to
# a base 10 value
def convert_2_to_10(binary_as_list):
	val = 0
	for i in range(0,len(binary_as_list)):
		val = val + binary_as_list[i]*pow(2,(len(binary_as_list) -1- i))
	return val

# Appends the astronaut to the list initially
# Also appends the astronaut to the list after
# x amount of dice rolls
def move_astro(v,w,x,y,z):
    if(w == 0):
        pos = 0
    else:
        if d_or_u == "d":
            planetList[y].remove("<--- Astronaut")
            pos = (y + z) % (x)
            planetList[pos].append("<--- Astronaut")
            return pos
        elif d_or_u == "u":
            planetList[y].remove("<--- Astronaut")
            pos = z
            planetList[pos].append("<--- Astronaut")
            return pos
    # x = length of list of planets (need to recheck due to explosions)
    # y = # in list of planets astro starts at
    # z = either die roll or user input value
    # w = Number of turns in the game
    # v = dice or user input

# Function that reads the information in the list and then stores
# it in a list
def read_string_list_from_file(the_file): 
    fileRef = open(the_file,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()  
        
    #........
    #print ("\n JUST TO TRACE, the local list of strings is:\n")
    #for element in localList:
    #    print (element)
    #print ()
    #........
        
    return localList

# This is the initial board defined for the game
# It reads the information from planetsData1.txt
# and then appends it into a matrix
def defaultBoard():
    master = read_string_list_from_file("planetsData1.txt")
    planet_num = 0
    accum = 0
    num_lists = len(master)
    planets = []
    place = ""
    index = 1
    for i in range(num_lists):
        planets.append([planet_num])
        planet_num += 1
    for i in master:
        index = 1
        for j in master[accum]:
                if j.isdigit():
                    place = place + j
                    if index == len(master[accum]):
                        planets[accum].append(int(place))
                        place = ""
                else:
                    planets[accum].append(int(place))
                    place = ""
                index += 1                 
        accum += 1
    return planets

# This function prints the matrix of values for the game
# And the prints depend on whether the game has ended,
# or has not ended
def printBoard(planetList, turner, numTurnsInGame, astroPosition, pythPlaneter, astroFuel):
    planets = planetList
    maxTurns = numTurnsInGame
    

    if(turner == 0):
        print("Showing board... just created")
        print()
        print(" The board at this point contains...")
        print("\tPlanet#", "\tCivLevel", "\tFuel", "\t\tRocks")
    elif(turner > 0 and turner < maxTurns and not(turner == maxTurns or int(astroPosition) == int(pythPlaneter) or astroFuel == 0 )):
        print("Showing board... about to do turn num: " + str(turner))
        print()
        print(" The board at this point contains...")
        print("\tPlanet#", "\tCivLevel", "\tFuel", "\t\tRocks")
    elif(turner == maxTurns or int(astroPosition) == int(pythPlaneter) or astroFuel == 0 ):
        print()
        print(" RESULTS END OF GAME")
        print()
        print("The game number " + str(numOfGamesPlayed + 1) + " just took place")
        print("Showing board... end of game")
        print()
        print(" The board at this point contains...")
        print("\tPlanet#", "\tCivLevel", "\tFuel", "\t\tRocks")

    turner = turner + 1
    
    for i in range(len(planets)):
        for k in range(len(planets[i])):
            print("\t", planets[i][k], "\t", end="")
        print()
    print()

# Called within the mild_explosion function and asks
# for the proportion explosion and returns that value to
# be used in mild_explosion to affect how the explosions work
def proportion_expl(turner):
    proportion = input("Proportion explosions? (1..5) ")
    if proportion.isdigit() and 1 <= int(proportion) <= 5:
        proportion_actual = proportion
        return proportion_actual
    else:
        while not proportion.isdigit() or proportion.isdigit() and not 1 <= int(proportion) <= 5:
            proportion = input("Sorry, that is not an intger between 1 and 5. Please type an integer between 1 and 5 \n")
            if proportion.isdigit() and 1 <= int(proportion) <= 5:
                proportion_actual = proportion
                return proportion_actual

# Affects the board of the game by creating an explosion on a random
# planet which changes the number of rocks based
# on certain conditions
def mild_explosion(planetList, turner, numTurnsInGame, proporter):
    planets = planetList
    maxTurns = numTurnsInGame
    z = int(proporter)                          # proportion of explosion between 1 and 5 (1 being all the time)
    x = len(planetList)
    y = r.randint(1,z*(x-1))                      # random planet that has the explosion
    if 0 < y <= x-1:
        a = planetList[y][3]        # placeholder for calcs on rock changes
        print("Oooooh! A mild or amazing explosion is happening in planet # " + str(y))
        print(" the board will have more rock specimens!")
        print()
        print()
        while y > 1:
            y = y - 1
            a = a + planetList[y][3]
            planetList[y][3] = a
        printBoard(planets, turner, maxTurns, astroPosition, pythPlaneter, astroFuel)
    else:
        print("The explosion happened in a neighbouring galaxy")

# ===================================
#
#
#       MAIN LEVEL OF THE PROGRAM 
#
#
# ===================================

# These are the variables(global) pertaining to the different
# elements of the game and called into different functions
# based on the input by the user
numTurnsInGame = 0
numOfGamesPlayed = 0            # will be changed to the number of times the user said yes to play the game
numOfGamesWon = 0               # default to 0
astroPosition = 0
turnNumber = 0                  # Starts at 0 for the initial turn
planetList = []
astroRockSpecimen = []          # initially empty because astronaut has no rocks from planets yet
mExplosions = 0
proporter = 0
pythPlaneter = 10               # Outside the realm of possibility
maxTurnsInGame = 10             # Initialized to 10
astroCivLevel = 0
astroPosition = 0
astroFuel = 50                  # Initialized to 50

# [][][][][][][][][][][][]
#   Beginning of the game 
# [][][][][][][][][][][][]
print(" Welcome to the Planet, Aliens and Explosions CMPT 120 Game!")
print("==============================================================")
print()

# This is the part of the program that is not looped
# The board can take different values from the text file
boardDraw = input("Do you want to draw the board (for all games)? (y/n): ")
while(boardDraw != "y" or boardDraw != "n"):
    if(boardDraw == "y"):
        print()
        break
    elif(boardDraw == "n"):
        print()
        print("The board will only apply to this game...")
        break
    else:
        print("What you typed is not what is expected, please retype")
        boardDraw = input("Do you want to draw the board (for all games)? (y/n): ")


# This is where the main looping of the game occurs based on the game conditions

playChecker = input("Do you want to play? (y/n): ")
if(playChecker == 'y'):
    print()         
    while playChecker == 'y':                                   #turnNumber <= maxTurnsInGame and astroFuel > 0 and astroPosition != pythPlaneter:         
        boardIni = input("Type d for the default board: ")
        while(boardIni != 'd'):
            print("Sorry we don't understand your input.")
            boardIni = input("Type d for the default board: ")
        
        planetList = defaultBoard()
        printBoard(planetList, turnNumber, numTurnsInGame, astroPosition, pythPlaneter, astroFuel)
        pythPlaneter = python_planet()

        # Name can be anything
        # So conditional proofing is not required
        print("Data for astronaut/player ")
        print()
        astroName = input("Name? ")

        # Asks user for civ level
        # Takes any integer but does not take string input
        # and will crash
        # only breaks out of loop when a number between 0 and 3 is inputted
        astroCivLevel = int(input("Civilization level (0..3)? (MUST ENTER INTEGER) "))
        while(astroCivLevel < 0 or astroCivLevel > 3):
            if(astroCivLevel < 4 and astroCivLevel > 0):
                break
            else:
                print("What you typed is not what is expected, please retype")
                astroCivLevel = int(input("Civilization level (0..3)? (MUST ENTER INTEGER) "))

        # Check works if entry is integers only
        # Breaks if user enters anything other than Integer
        astroFuel = int(input("Initial fuel liters (10..50)? (MUST ENTER INTEGER IN MULTIPLES OF 10) "))
        while(astroFuel != 10 or astroFuel != 20 or astroFuel != 30 or astroFuel != 40 or astroFuel != 50):
            if(astroFuel == 10 or astroFuel == 20 or astroFuel == 30 or astroFuel == 40 or astroFuel == 50):
                break
            else:
                print("What you typed is not what is expected, please retype")
                astroFuel = int(input("Initial fuel liters (10..50)? (MUST ENTER INTEGER IN MULTIPLES OF 10) "))
        print()
        
        # Check works if entry is integers only
        # Breaks if user enters anything other than Integer
        numTurnsInGame = int(input("Maximum turns this game? (1..10) (MUST ENTER INTEGER) "))
        while(numTurnsInGame > 10 or numTurnsInGame < 1):
            if(numTurnsInGame <= 10 and numTurnsInGame >= 1):
                print()
                break
            else:
                print("What you typed is not what is expected, please retype")
                numTurnsInGame = int(input("Maximum turns this game? (1..10) (MUST ENTER INTEGER) "))

        # Asks the user if they want to do explosions
        # Only mild explosions is implemented but prompt for amazing is there
        # If they say yes to amazing, mild explosions will not be run
        # If they say no, they can choose whether or not they want mild explosions
        explosionsAllow = input("Allow that Amazing Explosions happen? (y/n)(TYPE n ITS NOT IMPLEMENTED): ")
        while(explosionsAllow != "y" or explosionsAllow != "n"):
            if(explosionsAllow == "y"):
                # prints empty line because it's not implemented and it's optional
                print()
                break
            elif(explosionsAllow == "n"):
                print()
                print("Since you do not want amazing explosions to happen")
                mildExplosions = str(input("would you allow that Mild Explosions happen? (y/n): "))
                if(mildExplosions == "y"):
                    print()
                    proporter = proportion_expl(turnNumber)
                    break
                elif(mildExplosions == "n"):
                    print()
                    break
                else:
                    print("What you typed is not what is expected, please retype")
                    mildExplosions = str(input("would you allow that Mild Explosions happen? (y/n): "))
            else:
                print("What you typed is not what is expected, please retype")
                explosionsAllow = input("Allow that Amazing Explosions happen? (y/n)(TYPE n ITS NOT IMPLEMENTED): ")

        # Main loop for the game
        # based on the astronaut not
        # reaching the winning condition
        # or if they have not yet reached the
        # conditions in which they lose
        astroPosition = 0
        turnNumber = turnNumber + 1
        planetList[astroPosition].append("<--- Astronaut")
        printBoard(planetList, turnNumber, numTurnsInGame, astroPosition, pythPlaneter, astroFuel)
        while turnNumber <= numTurnsInGame and astroFuel > 0 and int(astroPosition) != int(pythPlaneter):
            #turner = 0
            print("Showing astronaut ... about to do turn num: " + str(turnNumber))
            print()
            print("The astronaut " + astroName + " has civilization level " + str(astroCivLevel))
            print("is in position: " + str(astroPosition))
            print("currently has: " + str(astroFuel) + " fuel liters")
            print("and collected until and including this turn " + str(astroRockSpecimen) + " rock specimens")
            print("So... he is...very alive!!!")
            print("and also ready to keep moving!")
            print()

            # Calls mild explosions after if true
            if(mildExplosions == "y"):
                mild_explosion(planetList, turnNumber, numTurnsInGame, proporter)
                mExplosions = mExplosions + 1


            #turnNumber = turnNumber + 1

            
            # Rolls the dice then adjusts the astronaut's position
            # based on the number generated by the dice roll
            # start of the next turn
            d_or_u = input("Roll die, or user types next pos? (d/u): ")
            while d_or_u != "d" and d_or_u  != "u":
                d_or_u  = input("Sorry, we don't understand that input. Roll die, or user types next pos? (d/u): ")
                
            diceRoll = int(advance(len(planetList), astroPosition, d_or_u))

            turnNumber = turnNumber + 1
            # Adjusts the astronauts position based on the diceRoll function (could be die roll or user input)
            astroPosition = move_astro(d_or_u, turnNumber, len(planetList), astroPosition, diceRoll)

            # Adjusts the astronauts fuel based on the conditions
            # of visiting the planets in the final assignment notes
            # REFER TO PART 18 OF THE FINAL ASSIGNMENT NOTES
            astroFuel = civi_checker(astroCivLevel,astroPosition,astroFuel)
    
            # Prints the board based on the opposite of the winning game conditions
            # Adds a game played to a counter
            # for each time the user wants to play
            # Also knows that the game has concluded
            # Since all previous conditions will have been met
            # when this is run
            if(turnNumber != numTurnsInGame or astroFuel != 0 or int(astroPosition)!= int(pythPlaneter)): 
                printBoard(planetList, turnNumber, numTurnsInGame, astroPosition, pythPlaneter, astroFuel)
            
                
            # Will end the loop and the game based on the multiple conditions
            # for where the user can lose
            if(int(astroPosition) == int(pythPlaneter)):
                numOfGamesWon = numOfGamesWon + 1 
                print("The game ended because the astronaut reached Python Planet and won!!!")
                print()
            elif(astroFuel == 0):
                print("The game ended because the astronaut ran out of fuel")
                print()
            elif(turnNumber > numTurnsInGame):
                print("The game ended because the max number of turns were played")
                print()
        
        # Adds a game played to a counter
        # for each time the user wants to play
        # Also knows that the game has concluded
        # Since all previous conditions will have been met
        # when this is run
        numOfGamesPlayed = numOfGamesPlayed + 1

        # Prints the information about the astronaut now that the game is over
        print("The astronaut " + astroName + " has civilization level " + str(astroCivLevel))
        print("is in position: " + str(astroPosition))
        print("currently has: " + str(astroFuel) + " fuel liters")
        print("and collected until and including this turn " + str(astroRockSpecimen) + " rock specimens")
        print("So... he is...very alive!!!")
        print("and he cannot move anymore since the game ended!")
        if(mildExplosions == "y"):
            print(str(mExplosions) + " mild explosions took place, adding rocks to various planets")
        print()

        # ASK TO PLAY AGAIN?
        # If no, prints the result of all the games
        # If yes, go back to beginning of loop which starts
        # with asking for the default board
        playChecker = input("Do you want to play again? (y/n): ")
        while(playChecker != "y" or playChecker != "n"):
            if(playChecker == "y"):
                print()
                turnNumber = 0
                break
            elif(playChecker == "n"):
                print()
                print(" RESULTS END OF ALL GAMES...........")
                print()   
                print(" The user played " + str(numOfGamesPlayed) + " game in total")
                print(" of those, the astronaut won " + str(numOfGamesWon))
                print(" To conclude, the program will do a conversion from binary to decimal!")
                print(" taking as source the list of rock specimens in the last game board")
                print()

                # Latest rock specimens
                empty = []
                for p in range(len(planetList)):
                    empty.append(planetList[p][3])

                # converts the empty list to a list of 0's and 1's
                # then converts it to binary and prints all of that
                # The game then ends
                listerOfOneZeroes = obtain_list_0s_1s(empty)
                converterOneZeroList = convert_2_to_10(listerOfOneZeroes)
                print("  List with rock specimens: " + str(empty))
                print("  Corresponding Binary: " + str(listerOfOneZeroes))
                print("  which converted to decimal is: " + str(converterOneZeroList))      
                print()
                print()
                print("Bye....")
                break     
            else:
                print("What you typed is not what is expected, please retype")
                playChecker = input("Do you want to play? (y/n): ")
                print()
elif(playChecker == 'n'):
    print("Maybe you will want to play some other time?")
    print()
    print()
    print("Bye....")
else:
    print("THERE IS NO ELSE CASE HERE. HOW CAN YOU PLAY THE GAME IF YOU CAN'T EVEN INPUT THINGS PROPERLY")
    # didn't have time to implement conditional checker for this case

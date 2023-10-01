#CSE3110CSE3130-Project

'''
title: Search and Sort Superheros
author: kliment lo
date:2023/09/20
'''

### -- INPUTS
def menu():
    '''
    allows the user to select what they wanna do
    :return:
    '''

    choice = input("""
    
What would you like to do?
1. Search for Hero data
2. View past searches
3. Exit

> """)
    if choice.isnumeric():
        choice = int(choice)
    else:
        print("Invalid input! ")
        return
    if choice > 0 and choice < 4:
        return choice
    else:
        print("Invalid input! ")

def askHero(DHEROS, MHEROS):
    '''
    asks the user what hero data they want
    :param DHEROS: (list)
    :param MHEROS: (list)
    :return: (str)
    '''
    from datetime import datetime
    time = datetime.now()
    notFound = True
    while notFound:
        try:
            hero = input("""What is the superhero ID? 
> """)
            hero = hero.upper() # uppercases the letter just in case they didn't
            if hero[0] == "M" and len(hero) == 4: # if they want to search marvel hero, and inputted correctly lengthed id
                hero = hero[1:] #cut off the letter, only keeping numbers
                notFound, heroData = binarySearch(MHEROS, hero) # search for the the id in list that only has marvel characters
            elif hero[0] == "D" and len(hero) == 4:
                hero = hero[1:]
                notFound, heroData = binarySearch(DHEROS, hero)

            if notFound == False:  # if an id match was found
                return heroData, str(time)  # return the data to be outputted
            else:  # if not found
                print("Entry is invalid! ")
        except IndexError:
            print("Entry is invalid! ")


### -- PROCESSING
def sortFranchise(LIST):
    '''
    sorts the heros from either in dc or marvel
    :return: list -> sorted
    '''
    dHeros = []
    mHeros = []
    for i in range(len(LIST)):
        if LIST[i][0][0][0] == "D":
            dHeros.append(LIST[i])
        else:
            mHeros.append(LIST[i])

    return dHeros, mHeros

def getRawData(fileName):
    '''
    reads the files and returns the information
    :param fileName: str
    :return: array
    '''
    import csv
    tempLi = []
    if fileName == "searchHistory.csv":
        try:
            file = open(fileName, "x")  # try to create file
            file.close() # always close files once done extracting info
        except FileExistsError:
            pass # do nothing
    file = open(fileName) #opens desired file
    text = csv.reader(file) #currently: text = <_csv.reader object at 0x0000028383877C40>
    for line in text: # actually extracts the information in said file. (for every line in this text file, append that line.)
        tempLi.append(line) #appends it
    if fileName == "searchHistory.csv": # if its the search history
        return tempLi # return it
    else: #if its the characterData
        var = tempLi.pop(0) # pop the category thingy
        return tempLi, var #return them

# rawArr is a 2D arrays holding all the Superhero data
# headers is a variable that holds the List of all the column headers.


def quickSort(LIST, FIRST_INDEX, LAST_INDEX):
    '''
    assign the first value as the pivot and place it in its correct location
    :param LIST: list(int) -> unsorted
    :param FIRST_INDEX: (int)
    :param LAST_INDEX: (int)
    :return: none
    '''

    if FIRST_INDEX < LAST_INDEX: # test that the list is one or more
        PIVOT_VALUE = LIST[FIRST_INDEX]
        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False

        while not DONE: #iterative component
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE: #continues until finds value that is smaller than pivot and left index
                LEFT_INDEX += 1

            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE: # continues until
                RIGHT_INDEX -= 1

            if RIGHT_INDEX < LEFT_INDEX: # has the right index crossed over the left?
                DONE = True # exits while loop
            else:
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP

        TEMP = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX - 1)
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX)


def binarySearch(LIST, VALUE):  # Iterative
    '''
    Search for a value within a list
    :param LIST: array (the List of values coming in is going to either be only D or only M)
    :param VALUE: int (ex. 324)
    :return: (bool)
    '''

    start_index = 0
    end_index = len(LIST) - 1
    while start_index <= end_index: # when
        midpoint_index = (start_index + end_index) // 2 # gets the index thats in the exact middle of the list
        if LIST[midpoint_index][0][1:] == VALUE: # if number so happens to be in the middle of the list and matches the value wanted
            return False, LIST[midpoint_index] #tells the program the data was found, then returns the hero's data
        elif VALUE > LIST[midpoint_index][0][1:]: # however, if the value wanted is larger than the middle index number
            start_index = midpoint_index + 1 # make the new start index this current index
        else:
            end_index = midpoint_index # if it was actually smaller than the middle index, the end-index now becomes the middle index

    # if nothing matched
    return True, "none" # notFound = True, so it reruns and asks the question again

def trackHistory(data, history, time):
    '''
    tracks the search history of the user
    :param data: (list)
    :param history: (list)
    :param time: (str)
    :return: none
    '''
    data.append(time)
    historyList = []
    for i in range(len(history)): # for the length of old history path
        historyList.append(history[i]) # append all of it into the historyList
    historyList.append(data) # append the new history into that list of history
    FILE = open("searchHistory.csv", "w") # puts it into write mode
    for i in range(len(historyList)): # for the length of total history
        historyList[i] = ",".join(historyList[i]) + "\n" # join the commas, then add a line break
        FILE.write(historyList[i]) # write it into the file
    FILE.close() # once done, close the file


### -- OUTPUTS
def displayInfo(HEADER, DATA):
    '''
    displays the hero data nicely
    :param HEADER: is the categories of the thingy
    :param DATA: the hero data
    :return: none
    '''
    for i in range(len(DATA)):
        if DATA[i] == "":
            DATA[i] = "N/A"
    pause = input(f"""
{HEADER[0]}: {DATA[0]}
{HEADER[1]}: {DATA[1]}
{HEADER[2]}: {DATA[2]}
{HEADER[3]}: {DATA[3]}
{HEADER[4]}: {DATA[4]}
{HEADER[5]}: {DATA[5]}
{HEADER[6]}: {DATA[6]}
{HEADER[7]}: {DATA[7]}
{HEADER[8]}: {DATA[8]}
{HEADER[9]}: {DATA[9]}
{HEADER[10]}: {DATA[10]} 

Press enter to return to menu""")

def displayHistory(HEADER, HISTORY):
    '''
    displays past history nicely
    :param HISTORY: (array)
    :return: (none)
    '''
    if len(HISTORY) == 0:
        print("""
There is currently no past searches! """)
        return
    for i in range(len(HISTORY)):
        if len(HISTORY[i]) == 12:
            print(f"""
--------------------------------------------
Time of Search: {HISTORY[i][11]}
{HEADER[0]}: {HISTORY[i][0]}
{HEADER[1]}: {HISTORY[i][1]}
{HEADER[2]}: {HISTORY[i][2]}
{HEADER[3]}: {HISTORY[i][3]}
{HEADER[4]}: {HISTORY[i][4]}
{HEADER[5]}: {HISTORY[i][5]}
{HEADER[6]}: {HISTORY[i][6]}
{HEADER[7]}: {HISTORY[i][7]}
{HEADER[8]}: {HISTORY[i][8]}
{HEADER[9]}: {HISTORY[i][9]}
{HEADER[10]}: {HISTORY[i][10]} 
--------------------------------------------""")
        else: #The way the contents are saved into the search history file, dates such as "October, 1928" are split into two seperate sections as it cuts off the coma
            print(f"""
--------------------------------------------
Time of Search: {HISTORY[i][12]}
{HEADER[0]}: {HISTORY[i][0]}
{HEADER[1]}: {HISTORY[i][1]}
{HEADER[2]}: {HISTORY[i][2]}
{HEADER[3]}: {HISTORY[i][3]}
{HEADER[4]}: {HISTORY[i][4]}
{HEADER[5]}: {HISTORY[i][5]}
{HEADER[6]}: {HISTORY[i][6]}
{HEADER[7]}: {HISTORY[i][7]}
{HEADER[8]}: {HISTORY[i][8]},{HISTORY[i][9]} 
{HEADER[9]}: {HISTORY[i][10]}
{HEADER[10]}: {HISTORY[i][11]} 
--------------------------------------------""")
    clear = input("""
Press enter to return to menu. If you would like to clear your search history, type 'Clear All'
> """)
    clear = clear.upper()
    if clear == "CLEAR ALL":
        file = open("searchHistory.csv", "w") #opens the file that stores all search history, making it so when you write something it overrides everything in the file currently
        file.write("") # writes nothing
        file.close()
        print("""
History cleared successfully! """)
    else:
        pass

if __name__ == "__main__":
    rawArr, headers = getRawData('comicBookCharData_mixed.csv') # extracts the daa from the code
    dHeros, mHeros = sortFranchise(rawArr)
    insertionSort(dHeros)
    insertionSort(mHeros)
    while True:
        searchHistory = getRawData('searchHistory.csv') # needs to be in loop so it updates the search history file/data
        choice = menu()
        if choice == 1:
            heroData, time = askHero(dHeros, mHeros)
            displayInfo(headers, heroData)
            trackHistory(heroData, searchHistory, time)
        if choice == 2:
            displayHistory(headers,searchHistory)
        if choice == 3:
            exit()


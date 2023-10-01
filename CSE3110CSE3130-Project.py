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
    try:
        hero = input("""What is the superhero ID? 
> """)
        hero = hero.upper() # uppercases the letter just in case they didn't
        if hero[0] == "M" and len(hero) == 4: # if they want to search marvel hero, and inputted correctly lengthed id
            hero = hero[1:] #cut off the letter, only keeping numbers
            found, heroData = binarySearch(MHEROS, hero) # search for the the id in list that only has marvel characters
        elif hero[0] == "D" and len(hero) == 4:
            hero = hero[1:]
            found, heroData = binarySearch(DHEROS, hero)
        if found:
            return heroData, str(time)  # return the data to be outputted
        else:
            askHero(DHEROS, MHEROS)
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


def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    '''
    Heapifies all subtreesin the binary tree
    :param LIST: list(int)
    :param LEN_ARRAY: int
    :param ROOT_INDEX: int -> parent index
    :return:
    '''

    LARGEST_INDEX = ROOT_INDEX
    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # Test if left child is larger than the largest index value
    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    #Test if right child v alue is larger than the largest index value.
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # Change the ROOT/Parent if needed
    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        #Heapify the Root
        heapify(LIST,LEN_ARRAY, LARGEST_INDEX)

def heapSort(LIST):
    '''
    sorts the list
    :param LIST: list(int) - >unsorted
    :return: none
    '''

    LEN_ARRAY = len(LIST)

    #build the max heap
    for i in range(LEN_ARRAY, -1, -1): # from tail to head
        heapify(LIST, LEN_ARRAY, i)


    #Extract the highest element
    for i in range(LEN_ARRAY - 1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i] # swaps index zero with highest value in unsorted section

        heapify(LIST, i, 0)



def binarySearch (LIST, VALUE):
    '''
    Search for a value within a list -recursive
    :param LIST: list(int)
    :param VALUE: (int)
    :return: (bool)
    '''
    MIDPOINT_INDEX = len(LIST)//2
    if LIST[MIDPOINT_INDEX][0][1:] == VALUE: # base case
        return True, LIST[MIDPOINT_INDEX]
    else:
        # simplify the list and return the function ye
        if VALUE < LIST[MIDPOINT_INDEX][0][1:]:
            return binarySearch(LIST[:MIDPOINT_INDEX], VALUE)
        else:
            return binarySearch(LIST[MIDPOINT_INDEX+1:], VALUE)

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
    heapSort(dHeros)
    heapSort(mHeros)
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


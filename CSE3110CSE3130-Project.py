# CSE3110CSE3130-Project

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
    found = False
    try:
        hero = input("""What is the superhero ID? 
> """)
        hero = hero.upper()  # uppercases the letter just in case they didn't
        if hero[0] == "M" and len(hero) == 4:  # if they want to search marvel hero, and inputted correctly lengthed id
            hero = hero[1:]  # cut off the letter, only keeping numbers
            found, heroData = binarySearch(MHEROS,
                                           hero)  # search for the the id in list that only has marvel characters
        elif hero[0] == "D" and len(hero) == 4:
            hero = hero[1:]
            found, heroData = binarySearch(DHEROS, hero)
        if found:
            return heroData, str(time)  # return the data to be outputted
        else:
            print("Entry is invalid!!!!")
            askHero(DHEROS, MHEROS)
    except IndexError:
        print("Entry is invalid! ")
        askHero(DHEROS, MHEROS)


### -- PROCESSING
def sortFranchise(LIST, START_INDEX, DHEROS, MHEROS):
    '''
    sorts the heros from either in dc or marvel!
    :return: list -> sorted
    '''

    if LIST[START_INDEX][0][0] == "D":
        DHEROS.append(LIST[START_INDEX])
    else:
        MHEROS.append(LIST[START_INDEX])
    if START_INDEX == len(LIST) - 1:
        return DHEROS, MHEROS
    else:
        return sortFranchise(LIST, START_INDEX + 1, DHEROS, MHEROS)


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
            file.close()  # always close files once done extracting info
        except FileExistsError:
            pass  # do nothing
    file = open(fileName)  # opens desired file
    text = csv.reader(file)  # currently: text = <_csv.reader object at 0x0000028383877C40>
    for line in text:  # actually extracts the information in said file. (for every line in this text file, append that line.)
        tempLi.append(line)  # appends it
    if fileName == "searchHistory.csv":  # if its the search history
        return tempLi  # return it
    else:  # if its the characterData
        var = tempLi.pop(0)  # pop the category thingy
        return tempLi, var  # return them


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

    # Test if right child v alue is larger than the largest index value.
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # Change the ROOT/Parent if needed
    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        # Heapify the Root
        heapify(LIST, LEN_ARRAY, LARGEST_INDEX)


def heapSort(LIST):
    '''
    sorts the list
    :param LIST: list(int) - >unsorted
    :return: none
    '''

    LEN_ARRAY = len(LIST)

    # build the max heap
    for i in range(LEN_ARRAY, -1, -1):  # from tail to head
        heapify(LIST, LEN_ARRAY, i)

    # Extract the highest element
    for i in range(LEN_ARRAY - 1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i]  # swaps index zero with highest value in unsorted section

        heapify(LIST, i, 0)


def binarySearch(LIST, VALUE):
    '''
    Search for a value within a list -recursive
    :param LIST: list(int)
    :param VALUE: (int)
    :return: (bool)
    '''
    MIDPOINT_INDEX = len(LIST) // 2
    if LIST[MIDPOINT_INDEX][0][1:] == VALUE:  # base case
        return True, LIST[MIDPOINT_INDEX]
    else:
        # simplify the list and return the function ye
        if VALUE < LIST[MIDPOINT_INDEX][0][1:]:
            return binarySearch(LIST[:MIDPOINT_INDEX], VALUE)
        else:
            return binarySearch(LIST[MIDPOINT_INDEX + 1:], VALUE)


def trackHistory(historyList, data, history, INDEX1, INDEX2):
    '''
    tracks the search history of the user
    :param data: (list)
    :param history: (list)
    :param time: (str)
    :return: none
    '''

    if INDEX1 < len(history):
        historyList.append(history[INDEX1])  # append all of it into the historyList
        return trackHistory(historyList, data, history, INDEX1 + 1, INDEX2)
    elif INDEX1 == len(history): # if it is equal
        historyList.append(data)  # append the new history into that list of history
        return trackHistory(historyList, data, history, INDEX1 + 1, INDEX2)
    FILE = open("searchHistory.csv", "w")  # puts it into write mode
    if INDEX2 < len(historyList):  # for the length of total history
        historyList[INDEX2] = ",".join(historyList[INDEX2]) + "\n"  # join the commas, then add a line break
        FILE.write(historyList[INDEX2])
        return trackHistory(historyList, data, history, INDEX1, INDEX2 + 1)
    for i in range(len(historyList)):
        FILE.write(historyList[i])  # write it into the file

    FILE.close()  # once done, close the file


### -- OUTPUTS
def displayInfo(HEADER, DATA, INDEX):
    '''
    displays the hero data nicely
    :param HEADER: is the categories of the thingy
    :param DATA: the hero data
    :return: none
    '''
    if INDEX != len(DATA) - 1:
        if DATA[INDEX] == "":
            DATA[INDEX] = "N/A"
        return displayInfo(HEADER, DATA, INDEX + 1)
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


def displayHistory(HEADER, HISTORY, INDEX):
    '''
    displays past history nicely
    :param HISTORY: (array)
    :return: (none)
    '''
    if len(HISTORY) == 0:
        print("""
There is currently no past searches! """)
        return
    if INDEX != len(HISTORY):
        if len(HISTORY[INDEX]) == 12:
            print(f"""
--------------------------------------------
Time of Search: {HISTORY[INDEX][11]}
{HEADER[0]}: {HISTORY[INDEX][0]}
{HEADER[1]}: {HISTORY[INDEX][1]}
{HEADER[2]}: {HISTORY[INDEX][2]}
{HEADER[3]}: {HISTORY[INDEX][3]}
{HEADER[4]}: {HISTORY[INDEX][4]}
{HEADER[5]}: {HISTORY[INDEX][5]}
{HEADER[6]}: {HISTORY[INDEX][6]}
{HEADER[7]}: {HISTORY[INDEX][7]}
{HEADER[8]}: {HISTORY[INDEX][8]}
{HEADER[9]}: {HISTORY[INDEX][9]}
{HEADER[10]}: {HISTORY[INDEX][10]} 
--------------------------------------------""")
        else:  # The way the contents are saved into the search history file, dates such as "October, 1928" are split into two seperate sections as it cuts off the coma
            print(f"""
--------------------------------------------
Time of Search: {HISTORY[INDEX][12]}
{HEADER[0]}: {HISTORY[INDEX][0]}
{HEADER[1]}: {HISTORY[INDEX][1]}
{HEADER[2]}: {HISTORY[INDEX][2]}
{HEADER[3]}: {HISTORY[INDEX][3]}
{HEADER[4]}: {HISTORY[INDEX][4]}
{HEADER[5]}: {HISTORY[INDEX][5]}
{HEADER[6]}: {HISTORY[INDEX][6]}
{HEADER[7]}: {HISTORY[INDEX][7]}
{HEADER[8]}: {HISTORY[INDEX][8]},{HISTORY[INDEX][9]} 
{HEADER[9]}: {HISTORY[INDEX][10]}
{HEADER[10]}: {HISTORY[INDEX][11]} 
--------------------------------------------""")
        return displayHistory(HEADER, HISTORY, INDEX + 1)

    clear = input("""
Press enter to return to menu. If you would like to clear your search history, type 'Clear All'
> """)
    clear = clear.upper()
    if clear == "CLEAR ALL":
        file = open("searchHistory.csv",
                    "w")  # opens the file that stores all search history, making it so when you write something it overrides everything in the file currently
        file.write("")  # writes nothing
        file.close()
        print("""
History cleared successfully! """)
    else:
        pass


if __name__ == "__main__":
    rawArr, headers = getRawData('comicBookCharData_mixed.csv')  # extracts the daa from the code
    dHeros = []
    mHeros = []
    dHeros, mHeros = sortFranchise(rawArr, 0, dHeros, mHeros)
    heapSort(dHeros)
    heapSort(mHeros)
    searchHistory = getRawData('searchHistory.csv')  # needs to be in loop so it updates the search history file/data
    choice = menu()
    if choice == 1:
        heroData, time = askHero(dHeros, mHeros)
        displayInfo(headers, heroData, 0)
        historyList = []
        heroData.append(time)
        trackHistory(historyList, heroData, searchHistory, 0, 0)
    if choice == 2:
        displayHistory(headers, searchHistory, 0)
    if choice == 3:
        exit()
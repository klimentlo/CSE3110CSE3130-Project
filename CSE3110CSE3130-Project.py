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
    :return: (str)
    '''
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
                return heroData  # return the data to be outputted
            else:  # if not found
                print("Entry is invalid!! ")
        except IndexError:
            print("Entry is invalid! ")
    return


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
    import csv
    tempLi = []
    file = open(fileName)
    text = csv.reader(file)
    for line in text:
        tempLi.append(line)
    var = tempLi.pop(0)
    return tempLi, var

# rawArr is a 2D arrays holding all the Superhero data
# headers is a variable that holds the List of all the column headers.


def insertionSort(LIST):
    '''
    takes the lowest index of the unsorted section and placed it in the sorted section
    :param LIST: list(int)
    :return: (none)
    '''
    # [ 3, 5, 7, 4, 9]
    for i in range(1, len(LIST)):
        UNSORTED_VALUE = LIST[i] # 4
        HIGHEST_SORTED_INDEX = i - 1 # 7 (index 2)
        while HIGHEST_SORTED_INDEX >= 0 and UNSORTED_VALUE < LIST[HIGHEST_SORTED_INDEX]: #
            LIST[HIGHEST_SORTED_INDEX + 1 ] = LIST[HIGHEST_SORTED_INDEX] #
            HIGHEST_SORTED_INDEX = HIGHEST_SORTED_INDEX - 1 #
        LIST[HIGHEST_SORTED_INDEX + 1] = UNSORTED_VALUE


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
Press any key to return to menu
""")


if __name__ == "__main__":
    rawArr, headers = getRawData('comicBookCharData_mixed.csv') # extracts the daa from the code
    dHeros, mHeros = sortFranchise(rawArr)
    insertionSort(dHeros)
    insertionSort(mHeros)
    while True:
        choice = menu()
        if choice == 1:
            heroData = askHero(dHeros, mHeros)
            displayInfo(headers, heroData)

        if choice == 2:
            pass
        if choice == 3:
            exit()


#CSE3110CSE3130-Project

'''
title: Search and Sort Superheros
author: kliment lo
date:2023/09/20
'''






### -- INPUTS

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

def binarySearch (LIST, VALUE): #Iterative
    '''
    Search for a value within a list
    :param LIST: list(int)
    :param VALUE: (int)
    :return: (bool)
    '''

    start_index = 0
    end_index = len(LIST) - 1
    while start_index <= end_index:
        midpoint_index = (start_index + end_index) // 2
        if LIST[midpoint_index] == VALUE:
            return True
        elif VALUE > LIST[midpoint_index]:
            start_index = midpoint_index + 1
        else:
            end_index = midpoint_index
    return False

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



### -- OUTPUTS
if __name__ == "__main__":
    rawArr, headers = getRawData('comicBookCharData_mixed.csv') # extracts the daa from the code
    dHeros, mHeros = sortFranchise(rawArr)
    insertionSort(dHeros)
    insertionSort(mHeros)
    print(dHeros)
    print(mHeros)


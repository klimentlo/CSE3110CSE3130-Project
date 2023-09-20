#CSE3110CSE3130-Project

'''
title: Search and Sort Superheros
author: kliment lo
date:2023/09/20
'''






### -- INPUTS

### -- PROCESSING
def getRawData(fileName):
    import csv
    tempLi = []
    file = open(fileName)
    text = csv.reader(file)
    for line in text:
        print(f"This is line: {line}")
        tempLi.append(line)
    var = tempLi.pop(0)
    return tempLi, var



# rawArr is a 2D arrays holding all the Superhero data
# headers is a variable that holds the List of all the column headers.
### -- OUTPUTS

if __name__ == "__main__":
    rawArr, headers = getRawData('comicBookCharData_mixed.csv') # extracts the daa from the code
    print(rawArr[0])
    print(len(rawArr[0]))
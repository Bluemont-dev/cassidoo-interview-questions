# from recursive import *


def listSets(tray):
    # sort the list by value and then color
    tray = sorted(tray, key=lambda tray: (tray['value'],tray['color']))

    # print(f"Tray after sorting:")
    for i in range (len(tray)):
        print(tray[i])

    # get count of jokers, if any, in tray
    jokerCount = 0
    while tray[0]['value']==0 and len(tray) > 0:
        jokerCount+=1
        tray.pop(0)

    if jokerCount > 0:
        print(f"\nWe have {jokerCount} jokers.")
        print(f"\nTray after removal of jokers:")
        for i in range (len(tray)):
            print(tray[i])
 
    # remove duplicates from the tray; they are useless
    for i in reversed(range(len(tray)-1)):
        if tray[i] == tray[i+1]:
            tray.pop(i+1)

    # print(f"\nTray after de-duping:")
    # for i in range (len(tray)):
    #     print(tray[i])

    #  find all possible "groups" (3 or 4 tiles of the same value, different colors)
    tempGroup = []
    allGroups = ""
    for i in range(len(tray)):
        # if tempGroup is empty, start a new group by appending
        if len(tempGroup) == 0:
            tempGroup.append(tray[i])
            # print(f"First item in tempGroup: {tempGroup[0]}")
        # if not empty, check to see if i value matches value of first,or any, element in tempgroup;
        else:
            if tray[i]['value'] == tempGroup[0]['value']:
            # if so, append
                tempGroup.append(tray[i])
            # if not, tempGroup is complete; send it to a function for processing, empty it out and start a new one by appending
            else:
                # send tempgroup to function
                # print(f"Tempgroup: {tempGroup}")
                # print("Now sending this tempgroup for processing.")
                allGroups = processGroups(tempGroup, jokerCount, allGroups)
                tempGroup = []
                tempGroup.append(tray[i])
    # after completion of the loop, send tempGroup one more time for processing
    # print(f"Last tempgroup: {tempGroup}")
    # print("Now sending final tempgroup for processing.")
    allGroups = processGroups(tempGroup, jokerCount, allGroups)
    if allGroups == "":
        allGroups = "(None) \n"
    
    #  find all possible "runs" (three or more consecutive numbers all in the same color)
    tempRun = []
    allRuns = ""
    # sort the tray according to color first, then value
    tray = sorted(tray, key=lambda tray: (tray['color'],tray['value']))

    # print(f"\nTray after re-sorting by color:")
    # for i in range (len(tray)):
    #     print(tray[i])

    for i in range(len(tray)):
        # if tempRun is empty, start a new run by appending
        if len(tempRun) == 0:
            tempRun.append(tray[i])
            # print(f"First item in tempRun: {tempRun[0]}")
        # if not empty, check to see if i color matches color of first,or any, element in tempgroup;
        else:
            if tray[i]['color'] == tempRun[0]['color']:
            # if so, append
                tempRun.append(tray[i])
            # if not, tempRun is complete; send it to a function for processing, empty it out and start a new one by appending
            else:
                # send temprun to function
                # print(f"Temprun: {tempRun}")
                # print("Now sending this temprun for processing.")
                allRuns = processRuns(tempRun, jokerCount, allRuns)
                tempRun = []
                tempRun.append(tray[i])
    # after completion of the loop, send tempRun one more time for processing
    # print(f"Last temprun: {tempRun}")
    # print("Now sending final temprun for processing.")
    allRuns = processRuns(tempRun, jokerCount, allRuns)
    if allRuns == "":
        allRuns = "(None) \n"
    
    # turn these values into lists that are easier for testing
    allGroups = allGroups.split(' \n')
    for i in range(len(allGroups)):
        if allGroups[i] == '':
            allGroups.pop(i)
    allRuns = allRuns.split(' \n')
    for i in range(len(allRuns)):
        if allRuns[i] == '':
            allRuns.pop(i)
    # print("\nBest Groups:")
    # print(allGroups)
    # print("Best Runs:")
    # print(allRuns)
    return allGroups, allRuns

def processGroups(tempGroup, jokerCount, allGroups):
    # print("Entering the processGroups function.")
    # if we we have fewer than 3 items even with jokers, return allGroups without modification; nothing to add to it
    if len(tempGroup) + jokerCount < 3:
        return allGroups
    # else, if we have 4 items without jokers, write it
    elif len(tempGroup) == 4:
        allGroups += stringifyGroups(tempGroup)
    # else, if we have 4 items with jokers, add jokers to end and write it
    elif len(tempGroup) + jokerCount == 4:
        for i in range(4 - len(tempGroup)):
            tempGroup.append({"value":0, "color":"joker"})
        allGroups += stringifyGroups(tempGroup)
    # else, if we have 3 items without jokers, write it
    elif len(tempGroup) == 3:
        allGroups += stringifyGroups(tempGroup)
    # else, if we have 3 items with jokers, write it
    elif len(tempGroup) + jokerCount == 3:
        for i in range(3 - len(tempGroup)):
            tempGroup.append({"value":0, "color":"joker"})
        allGroups += stringifyGroups(tempGroup)
    # print(f"Just before returning one new line from processGroups, allGroups is:\n{allGroups}")
    return allGroups
    
def stringifyGroups(tempGroup):
    # print("Entering stringifyGroups function.")
    groupAsString = ""
    for item in tempGroup:
        # if not a joker
        if item['value'] > 0:
            groupAsString += f"[{item['value']} {item['color']}] "
        else:
            groupAsString += "[JOKER] "
    return groupAsString + "\n"
    
def processRuns(tempRun, jokerCount, allRuns):
    # print("Entering the processRuns function.")
    # if the array isn't long enough (even with jokers) to form a run, return without altering allRuns
    if len(tempRun) + jokerCount < 3:
        return allRuns
    # map the values to an array
    tempRunValues = []
    for i in range(len(tempRun)):
        tempRunValues.append(tempRun[i]['value'])
    # send this array to getBestRun for processing
    bestRunIntArray = getBestRun(tempRunValues,jokerCount)
    # convert the int array to a string, noting jokers where appropriate
    color = tempRun[0]['color']
    bestRunString = ""
    for i in range(len(bestRunIntArray)):
        if bestRunIntArray[i] in tempRunValues:
            bestRunString += f"[{bestRunIntArray[i]} {color}] "
        else:
            bestRunString += "[JOKER] "
    if bestRunString != "":
        bestRunString += "\n"
    # remember that allRun is a string containing the runs as tiles
    allRuns += bestRunString
    # print ("allRuns:")
    # print(allRuns)
    return allRuns

def getBestRun(array, jokerCount):
    maxRun = []
    if jokerCount == 0:
        maxRun = evaluateArrayNoJokers(array)
        return maxRun
    else:
        # loop through array, trying the joker at various locations
        for i in range(len(array)):
            tempArray = []
            newRun = []
            # for first element
            if i == 0:
                if array[i] > 1:
                    # insert a joker to the left
                    tempArray = array.copy()
                    tempArray.insert(i, array[i]-1)
                    newRun = getBestRun(tempArray, jokerCount-1)
                    maxRun = compareRuns(newRun, maxRun)
                # try inserting a joker to the right, if an element exists to the right and a gap exists
                if i != len(array)-1 and array[i+1] - array[i] > 1:
                    tempArray = array.copy()
                    tempArray.insert(i+1, array[i]+1)
                    newRun = getBestRun(tempArray, jokerCount-1)
                    maxRun = compareRuns(newRun, maxRun)       
            # for last element in list
            elif i == len(array)-1:
                # try inserting a joker to the left, if a gap exists
                if array[i] - array[i-1] > 1:
                    tempArray = array.copy()
                    tempArray.insert(i, array[i]-1)
                    newRun = getBestRun(tempArray, jokerCount-1)
                    maxRun = compareRuns(newRun, maxRun)
                # if integer is less than 13, make an insert to the right
                if array[i] < 13:
                    tempArray = array.copy()
                    tempArray.append(array[i] + 1)
                    newRun = getBestRun(tempArray, jokerCount-1)
                    maxRun = compareRuns(newRun, maxRun)
            # for all other elements, try inserts both left and right
            else:
                # insert left if gap exists
                if array[i] - array[i-1] > 1:
                    tempArray = array.copy()
                    tempArray.insert(i, array[i]-1)
                    newRun = getBestRun(tempArray, jokerCount-1)
                    maxRun = compareRuns(newRun, maxRun)
                # insert right if gap exists
                if array[i+1] - array[i] > 1:
                    tempArray = array.copy()
                    tempArray.insert(i+1, array[i]+1)
                    newRun = getBestRun(tempArray, jokerCount-1)
                    maxRun = compareRuns(newRun, maxRun)
    return maxRun

def compareRuns (newRun,maxRun):
    if len(newRun) > len(maxRun):
        return newRun
    elif len(newRun) == len(maxRun) and len(newRun) > 0 and newRun[0] > maxRun[0]:
        return newRun
    else:
        return maxRun

def evaluateArrayNoJokers(array):
    # create metaArray, or an array of arrays of consecutive integers
    subRun = []
    metaArray = []
    bestRun = []
    for i in range(len(array)):
        subRun.append(array[i])
        # if at end of array, or if last element in the subRun isn't one less than next element in array, close out that subrun and append to metaArray
        if (i == len(array) - 1) or (subRun[len(subRun) - 1] + 1 != array[i + 1]):
            # if subrun is at least 3 elements in length (long enough to be a run), add it to the metaArray
            if len(subRun)>2:
                metaArray.append(subRun)
            subRun = []
    if len(metaArray) > 0:
        metaArray.sort(key=doubleSort, reverse=True)
        bestRun = metaArray[0]
    return bestRun

def doubleSort(element):
    # if sorting by two conditions
    return len(element), element[len(element)-1]
    # if sorting by one conditions
    # return len(element)]

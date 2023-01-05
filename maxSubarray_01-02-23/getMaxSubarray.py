#evaluate the inputs and return the maxSubarray
def getMaxSubarray (mainList, n):
    #check for value of n too high or low
    if n > len(mainList) or n < 1:
        return "Invalid length for subarray"
    highestSum = 0
    maxSubarray = []
    tempSum = 0
    tempArray = []
    # loop through mainList, getting sums of subarrays
    for i in range(len(mainList)+1-n):
        tempSum = 0
        tempArray = []
        for j in range(n):
            tempSum += mainList[i+j]
            tempArray.append(mainList[i+j])
        if tempSum > highestSum:
            highestSum = tempSum
            maxSubarray = tempArray
    return maxSubarray
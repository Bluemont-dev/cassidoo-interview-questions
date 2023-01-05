# the challenge: Given an array of integers arr and an integer n, return a subarray of arr of length n where the sum is the largest. Make sure you maintain the order of the original array, and if n is greater than arr.length, you can choose what you want to return.

from getMaxSubarray import *

#prompt user for an series of integers, comma-separated
userEntry = input("Enter a series of integers, separated by commas: ")

#convert user entry to list of integers
userList = userEntry.split(',')
for i in range(len(userList)-1, -1, -1):
    try:
        userList[i] = int(userList[i])
    except ValueError:
        print(f"{userList[i]} is not an integer, so we will omit it from the series.")
        del userList[i]

#prompt user for the length of the desired subarray
subarrayLength = 0
while subarrayLength == 0:
    userLengthString = input(f"Enter the length of your desired subarray. Do not exceed {len(userList)}: ")
    try:
        subarrayLength = int(userLengthString)
    except ValueError:
        print(f"{userLengthString} is not an integer. Please try again.")
    if subarrayLength == 0:
        print("Subarray length must be greater than zero. Please try again.")
    elif subarrayLength > len(userList):
        print(f"Subarray length cannot exceed {len(userList)}, the length of your series. Please try again.")
        subarrayLength = 0

print(getMaxSubarray(userList, subarrayLength))
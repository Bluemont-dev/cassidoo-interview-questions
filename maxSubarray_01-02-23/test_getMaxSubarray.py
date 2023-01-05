from getMaxSubarray import *

def test_getMaxSubarray():
    # value of n greater than length of userList
    assert getMaxSubarray([1,2,3,4,5],6) == "Invalid length for subarray"

    # value of n less than 1
    assert getMaxSubarray([1,2,3,4,5],0) == "Invalid length for subarray"

    # n = length of userList
    assert getMaxSubarray([1,2,3,4,5],5) == [1,2,3,4,5]

    # highest values in beginning of list
    assert getMaxSubarray([5,4,3,2,1],2) == [5,4]

    # highest values in middle of list
    assert getMaxSubarray([1,2,5,4,3],2) == [5,4]

    # highest values at end of list
    assert getMaxSubarray([1,2,3,4,5],2) == [4,5]

    # all values the same
    assert getMaxSubarray([1,1,1,1,1],3) == [1,1,1]
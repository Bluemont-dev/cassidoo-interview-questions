from list_sets import *

def test_listSets():
    # unsorted, no groups or runs, no jokers, return two empty strings
    assert listSets([{'value': 8, 'color': 'yellow'}, {'value': 1, 'color': 'black'}, {'value': 3, 'color': 'red'}, {'value': 13, 'color': 'black'}, {'value': 4, 'color': 'yellow'}, {'value': 6, 'color': 'blue'}, {'value': 11, 'color': 'red'}, {'value': 7, 'color': 'red'}, {'value': 10, 'color': 'blue'}, {'value': 2, 'color': 'blue'}, {'value': 12, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 5, 'color': 'black'}, {'value': 2, 'color': 'red'}]) == (['(None)'], ['(None)'])

    # unsorted, no groups or runs, 1 joker, return two empty strings
    assert listSets([{'value': 8, 'color': 'yellow'}, {'value': 1, 'color': 'black'}, {'value': 3, 'color': 'red'}, {'value': 13, 'color': 'black'}, {'value': 4, 'color': 'yellow'}, {'value': 6, 'color': 'blue'}, {'value': 11, 'color': 'red'}, {'value': 7, 'color': 'red'}, {'value': 10, 'color': 'blue'}, {'value': 2, 'color': 'blue'}, {'value': 12, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 5, 'color': 'black'}, {'value': 0, 'color': 'joker'}]) == (['(None)'], ['(None)'])

    # unsorted, no groups or runs, 2 jokers; return one of every group thru 12 and a run in each color
    assert listSets([{'value': 8, 'color': 'yellow'}, {'value': 1, 'color': 'black'}, {'value': 3, 'color': 'red'}, {'value': 0, 'color': 'joker'}, {'value': 4, 'color': 'yellow'}, {'value': 6, 'color': 'blue'}, {'value': 11, 'color': 'red'}, {'value': 7, 'color': 'red'}, {'value': 10, 'color': 'blue'}, {'value': 2, 'color': 'blue'}, {'value': 12, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 5, 'color': 'black'}, {'value': 0, 'color': 'joker'}]) == (['[1 black] [JOKER] [JOKER]', '[2 blue] [JOKER] [JOKER]', '[3 red] [JOKER] [JOKER]', '[4 yellow] [JOKER] [JOKER]', '[5 black] [JOKER] [JOKER]', '[6 blue] [JOKER] [JOKER]', '[7 red] [JOKER] [JOKER]', '[8 yellow] [JOKER] [JOKER]', '[9 black] [JOKER] [JOKER]', '[10 blue] [JOKER] [JOKER]', '[11 red] [JOKER] [JOKER]', '[12 yellow] [JOKER] [JOKER]'], ['[9 black] [JOKER] [JOKER]', '[10 blue] [JOKER] [JOKER]', '[11 red] [JOKER] [JOKER]', '[JOKER] [12 yellow] [JOKER]'])

    # unsorted, 2 groups of equal length in different colors, no runs, no jokers; return both groups
    assert listSets([{'value': 8, 'color': 'yellow'}, {'value': 1, 'color': 'black'}, {'value': 3, 'color': 'red'}, {'value': 1, 'color': 'blue'}, {'value': 10, 'color': 'yellow'}, {'value': 6, 'color': 'blue'}, {'value': 11, 'color': 'red'}, {'value': 7, 'color': 'red'}, {'value': 10, 'color': 'blue'}, {'value': 2, 'color': 'blue'}, {'value': 12, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 10, 'color': 'black'}, {'value': 1, 'color': 'red'}]) == (['[1 black] [1 blue] [1 red]', '[10 black] [10 blue] [10 yellow]'], ['(None)'])

    # unsorted, no groups, 2 runs of equal length in same color, no jokers; return higher run
    assert listSets([{'value': 8, 'color': 'yellow'}, {'value': 1, 'color': 'black'}, {'value': 3, 'color': 'red'}, {'value': 2, 'color': 'black'}, {'value': 4, 'color': 'yellow'}, {'value': 6, 'color': 'blue'}, {'value': 11, 'color': 'black'}, {'value': 7, 'color': 'red'}, {'value': 10, 'color': 'blue'}, {'value': 3, 'color': 'black'}, {'value': 12, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 10, 'color': 'black'}, {'value': 1, 'color': 'red'}]) == (['(None)'], ['[9 black] [10 black] [11 black]'])

def test_processGroups():
    # no joker, 2 items to form group; return empty string
    assert processGroups([{'value': 2, 'color': 'blue'}, {'value': 2, 'color': 'red'}],0,'') == ''

    # 1 joker, 1 items to form group; return empty string
    assert processGroups([{'value': 2, 'color': 'blue'}],1,'') == ''

    # no joker, 2 items to form group; pass existing string, return unchanged string
    assert processGroups([{'value': 3, 'color': 'blue'}, {'value': 3, 'color': 'red'}],0,'[2 blue] [2 red] [2 yellow] \n') == '[2 blue] [2 red] [2 yellow] \n'

    # no joker, 3 items to form group; return the group
    assert processGroups([{'value': 2, 'color': 'blue'}, {'value': 2, 'color': 'red'}, {'value': 2, 'color': 'yellow'}],0,'') == '[2 blue] [2 red] [2 yellow] \n'

    # no joker, 3 items to form group; passing existing string; return new string with the group added
    assert processGroups([{'value': 2, 'color': 'blue'}, {'value': 2, 'color': 'red'}, {'value': 2, 'color': 'yellow'}],0,'[1 black] [1 blue] [1 red] \n') == '[1 black] [1 blue] [1 red] \n[2 blue] [2 red] [2 yellow] \n'


def test_processRuns():
    # no joker, 2 items to form run; return empty string
    assert processRuns([{'value': 2, 'color': 'blue'}, {'value': 3, 'color': 'blue'}],0,'') == ''

    # no joker, 2 items to form run; pass existing string, return unchanged string
    assert processRuns([{'value': 2, 'color': 'blue'}, {'value': 3, 'color': 'blue'}],0,'[10 black] [11 black] [12 black] \n') == '[10 black] [11 black] [12 black] \n'

    # no joker, 3 items to form run; return the run
    assert processRuns([{'value': 2, 'color': 'blue'}, {'value': 3, 'color': 'blue'}, {'value': 4, 'color': 'blue'}],0,'') == '[2 blue] [3 blue] [4 blue] \n'

    # no joker, 3 items to form run; passing existing string; return new string with the run added
    assert processRuns([{'value': 2, 'color': 'blue'}, {'value': 3, 'color': 'blue'}, {'value': 4, 'color': 'blue'}],0,'[10 black] [11 black] [12 black] \n') == '[10 black] [11 black] [12 black] \n[2 blue] [3 blue] [4 blue] \n'

    # 1 joker, 1 items to form run; return empty string
    assert processRuns([{'value': 2, 'color': 'blue'}, {'value': 7, 'color': 'blue'}],1,'') == ''

def test_getBestRun():
    # no jokers, run less than 3, return empty array
    assert getBestRun([1,2,4,6,12,13],0) == []

    # no jokers, run of 3, return that run
    assert getBestRun([1,2,4,5,6,12,13],0) == [4,5,6]

    # no jokers, 2 different runs of 3, return the higher run
    assert getBestRun([1,2,4,5,6,11,12,13],0) == [11,12,13]

    # no jokers, runs of 3 and 4, return the longer run despite earlier location in the array
    assert getBestRun([1,2,3,4,6,11,12,13],0) == [1,2,3,4]

    # 1 joker, run of 2, return run of 3
    assert getBestRun([1,2,5,13],1) == [1,2,3]

    # 1 joker, longest run is to left, insert left
    assert getBestRun([12,13],1) == [11,12,13]

    # 1 joker, longest run is to right, insert right
    assert getBestRun([11,12],1) == [11,12,13]

    # 1 joker, bridge a gap of 1
    assert getBestRun([1,2,3,4,5,7,8,9,10,11,12,13],1) == [1,2,3,4,5,6,7,8,9,10,11,12,13]

    # 2 jokers, bridge a gap of 2
    assert getBestRun([9,12],2) == [9,10,11,12]

    # 2 jokers, go on either side of sequence
    assert getBestRun([1,5,12],2) == [11,12,13]

    # 2 jokers, use both to the left
    assert getBestRun([3,4,12,13],2) == [10,11,12,13]

    # 2 jokers, use both to the right
    assert getBestRun([1,11],2) == [11,12,13]

def test_compareRuns():
    # different lengths, new run is longer, return new run
    assert compareRuns([1,2,3,4],[11,12,13]) == [1,2,3,4]

    # different lengths, max run is longer, return max run
    assert compareRuns([11,12,13],[1,2,3,4]) == [1,2,3,4]

    # equal lengths, new run has higher index, return new run
    assert compareRuns([11,12,13],[10,11,12]) == [11,12,13]

    # equal lengths, max run has higher index, return max run
    assert compareRuns([10,11,12],[11,12,13]) == [11,12,13]

def test_evaluateArrayNoJokers():
    # no runs of length greater than 2, return empty array
    assert evaluateArrayNoJokers([1,6,13]) == []
    # one run is length 3, none longer; return the 3
    assert evaluateArrayNoJokers([1,6,7,8,13]) == [6,7,8]
    # two runs of unequal length, both length greater than 2; return the longer run
    assert evaluateArrayNoJokers([1,2,3,4,6,7,8,13]) == [1,2,3,4]
    # two runs of equal length, both length greater than 2; return the one with higher index
    assert evaluateArrayNoJokers([1,2,3,4,6,7,8,9,13]) == [6,7,8,9]
    # three runs of equal length, all have length greater than 2; return the highest index
    assert evaluateArrayNoJokers([1,2,3,5,6,7,9,10,11,13]) == [9,10,11]
    # one array, full length, return that aray
    assert evaluateArrayNoJokers([1,2,3,4,5,6,7,8,9,10,11,12,13]) == [1,2,3,4,5,6,7,8,9,10,11,12,13]

def test_stringifyGroups():
    # group of 3, no jokers
    assert stringifyGroups([{'value': 5, 'color': 'black'}, {'value': 5, 'color': 'blue'}, {'value': 5, 'color': 'red'}]) == '[5 black] [5 blue] [5 red] \n'

    # group of 4, no jokers
    assert stringifyGroups([{'value': 5, 'color': 'black'}, {'value': 5, 'color': 'blue'}, {'value': 5, 'color': 'red'}, {'value': 5, 'color': 'yellow'}]) == '[5 black] [5 blue] [5 red] [5 yellow] \n'

    # group of 3, 1 joker
    assert stringifyGroups([{'value': 5, 'color': 'black'}, {'value': 0, 'color': 'joker'}, {'value': 5, 'color': 'yellow'}]) == '[5 black] [JOKER] [5 yellow] \n'

    # group of 4, 1 joker
    assert stringifyGroups([{'value': 0, 'color': 'joker'}, {'value': 5, 'color': 'blue'}, {'value': 5, 'color': 'red'}, {'value': 5, 'color': 'yellow'}]) == '[JOKER] [5 blue] [5 red] [5 yellow] \n'


# trays that should return no groups and no runs:
# [{'value': 1, 'color': 'black'}, {'value': 2, 'color': 'blue'}, {'value': 3, 'color': 'red'}, {'value': 4, 'color': 'yellow'}, {'value': 5, 'color': 'black'}, {'value': 6, 'color': 'blue'}, {'value': 7, 'color': 'red'}, {'value': 8, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 10, 'color': 'blue'}, {'value': 11, 'color': 'red'}, {'value': 12, 'color': 'yellow'}, {'value': 13, 'color': 'black'}, {'value': 1, 'color': 'blue'}]

# [{'value': 1, 'color': 'black'}, {'value': 2, 'color': 'blue'}, {'value': 3, 'color': 'red'}, {'value': 4, 'color': 'yellow'}, {'value': 5, 'color': 'black'}, {'value': 6, 'color': 'blue'}, {'value': 7, 'color': 'red'}, {'value': 8, 'color': 'yellow'}, {'value': 9, 'color': 'black'}, {'value': 10, 'color': 'blue'}, {'value': 11, 'color': 'red'}, {'value': 12, 'color': 'yellow'}, {'value': 13, 'color': 'black'}, {'value': 0, 'color': 'joker'}]
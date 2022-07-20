from random import sample

def createTray():
    #  set up the source array of tiles from which to create a tray
    #  values 1-13, colors are red, blue, black and yellow; 2 full sets of each color for 104 tiles, plus 2 jokers = 106
    allTiles = []
    colors = ["black","blue","red","yellow"]

    for i in range(1,14):
        for color in colors:
            for j in range (2):
                allTiles.append({"value":i, "color":color})

    # add the 2 jokers
    for i in range (2):
        allTiles.append({"value":0, "color":"joker"})

    # random select 14 tiles for the tray, without replacement, just like physically drawing tiles from a collection.
    tray = sample(allTiles, k=14)
    return tray
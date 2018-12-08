import re
coordinateInput = open("inputDay6.txt","r")
reg = re.compile("(\d+), (\d+)")
coordinates = []
for coordinate in coordinateInput:
    match = reg.match(coordinate)
    coordinates.append(list(map(lambda x:int(x),match.groups())))
maxX = max(coordinates,key=lambda x:x[0])[0]
maxY = max(coordinates,key=lambda x:x[1])[1]
minX = min(coordinates,key=lambda x:x[0])[0]
minY = min(coordinates,key=lambda x:x[1])[1]
grid = []

def findClosestCoordinate(x,y):
    distances = [abs(x[0])+abs(x[1]) for x in coordinates]
    closest = min(distances)
    if(distances.count(closest) == 1):
        return distances.index(closest)
    else:
        return -1

def existsOnEdge(value):
    if(value in grid[0] or value in grid[-1]):
        return True
    for y in range(len(grid[0])):
        if(value == grid[0][y] or value == grid[-1][y]):
            return True
    return False

for x in range(minX,maxX+1):
    gridRow = []
    for y in range(minY,maxY+1):
        gridRow.append(findClosestCoordinate(x,y))
    grid.append(gridRow)

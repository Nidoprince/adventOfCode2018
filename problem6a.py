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
    distances = [abs(z[0]-x)+abs(z[1]-y) for z in coordinates]
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

for x in range(minX-3,maxX+2):
    gridRow = []
    for y in range(minY-3,maxY+2):
        gridRow.append(findClosestCoordinate(x,y))
    grid.append(gridRow)

counter = {}
for row in grid:
    for cell in row:
        if(cell in counter):
            counter[cell] += 1
        else:
            counter[cell] = 1

mostArea = sorted(counter.items(),reverse = True,key=lambda x:x[1])
for area in mostArea:
    if(area[0] != -1 and not existsOnEdge(area[0])):
        print(area[1])
        break
print(mostArea)

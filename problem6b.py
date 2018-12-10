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

def totalDistance(x,y):
    distances = [abs(z[0]-x)+abs(z[1]-y) for z in coordinates]
    return sum(distances)

outDistance = 10000//len(coordinates)
howManyUnderTenK = 0
for x in range(minX-outDistance,maxX+outDistance):
    for y in range(minY-outDistance,maxY+outDistance):
        if(totalDistance(x,y) < 10000):
            howManyUnderTenK+=1
print(howManyUnderTenK)

import re
claims = open("inputDay3.txt","r")
grid = [[0 for x in range(1000)] for y in range(1000)]
reg = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
for claim in claims:
    search = reg.match(claim)
    chunks = list(map(lambda x: int(x),search.groups()))
    for i in range(chunks[1],chunks[1]+chunks[3]):
        for j in range(chunks[2],chunks[2]+chunks[4]):
            grid[i][j]+=1
count = 0
for x in range(1000):
    for y in range(1000):
        if(grid[x][y] >= 2):
            count+=1
print(count)

import re
claims = open("inputDay3.txt","r")
grid = [[0 for x in range(1000)] for y in range(1000)]
reg = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
remainingClaims = set()
for claim in claims:
    search = reg.match(claim)
    chunks = list(map(lambda x: int(x),search.groups()))
    remainingClaims.add(chunks[0])
    for i in range(chunks[1],chunks[1]+chunks[3]):
        for j in range(chunks[2],chunks[2]+chunks[4]):
            if(grid[i][j] == 0):
                grid[i][j] = chunks[0]
            else:
                remainingClaims.discard(grid[i][j])
                remainingClaims.discard(chunks[0])
                grid[i][j] = -1
print(remainingClaims)

import re
requirementInput = open("inputDay7.txt","r")
reg = re.compile("Step (\w) must be finished before step (\w) can begin.")
stepAfterWhat = {}
for req in requirementInput:
    parts = reg.match(req)
    aThenB = parts.groups()
    if(aThenB[1] in stepAfterWhat):
        stepAfterWhat[aThenB[1]].append(aThenB[0])
    else:
        stepAfterWhat[aThenB[1]] = [aThenB[0]]
    if(aThenB[0] not in stepAfterWhat):
        stepAfterWhat[aThenB[0]] = []
output = ""
while(len(stepAfterWhat) > 0):
    possibilities = ""
    for step in stepAfterWhat:
        if(len(stepAfterWhat[step]) == 0):
            possibilities += step
        elif(all(map(lambda x: x in output,stepAfterWhat[step]))):
            possibilities += step
    alphabetic = sorted(possibilities)
    print(alphabetic)
    output += alphabetic[0]
    del stepAfterWhat[alphabetic[0]]

print(output)

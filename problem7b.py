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
workers = [[False,0],[False,0],[False,0],[False,0],[False,0]]
finishedLength = len(stepAfterWhat)
seconds = 0
while(len(output) < finishedLength):
    for worker in workers:
        if(worker[0]):
            if(worker[1]>0):
                worker[1]-=1
            else:
                output+=worker[0]
                worker[0] = False
    possibilities = ""
    for step in stepAfterWhat:
        if(len(stepAfterWhat[step]) == 0):
            possibilities += step
        elif(all(map(lambda x: x in output,stepAfterWhat[step]))):
            possibilities += step
    alphabetic = sorted(possibilities)
    for worker in workers:
        if(not worker[0]):
            if(len(alphabetic)>0):
                worker[0] = alphabetic[0]
                worker[1] = 60 + ord(worker[0])-ord("A")
                alphabetic = alphabetic[1:]
                del stepAfterWhat[worker[0]]
    seconds+=1
print(seconds-1)

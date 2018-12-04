import re
guardSchedules = open("inputDay4.txt","r")
reg = re.compile('^\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)$')
schedules = []
for schedule in guardSchedules:
    search = reg.match(schedule)
    schedules.append(search.groups())
schedules.sort(key=lambda x:x[0]+x[1]+x[2]+x[3]+x[4])
currentGuard = 0
startTime = 0
guardMinutesSlept = {}
reg = re.compile('Guard #(\d+) begins shift')
for event in schedules:
    if(event[5][0] == "G"):
        guard = reg.match(event[5])
        currentGuard = int(guard.group(1))
        if(currentGuard not in guardMinutesSlept):
            guardMinutesSlept[currentGuard] = []
    elif(event[5][0] == "f"):
        startTime = int(event[4])
    elif(event[5][0] == "w"):
        for t in range(startTime,int(event[4])):
            guardMinutesSlept[currentGuard].append(t)
sleepiestGuard = sorted(guardMinutesSlept,reverse=True,key=lambda x:len(guardMinutesSlept[x]))[0]
sleepySchedule = guardMinutesSlept[sleepiestGuard]
sleepiestMinute = max(set(sleepySchedule),key=sleepySchedule.count)
print(sleepiestGuard,sleepiestMinute,sleepiestGuard*sleepiestMinute)

letters = open("inputDay2.txt","r")
numOf2s = 0
numOf3s = 0
def countainsTwosOrThrees(text):
    letterCounter = {}
    letterList = list(text)
    for letter in letterList:
        if letter in letterCounter:
            letterCounter[letter] += 1
        else:
            letterCounter[letter] = 1
    out = 0
    if 2 in letterCounter.values():
        out += 1
    if 3 in letterCounter.values():
        out += 2
    return out

for line in letters:
    value = countainsTwosOrThrees(line)
    if(value == 1):
        numOf2s += 1
    elif(value == 2):
        numOf3s += 1
    elif(value == 3):
        numOf2s += 1
        numOf3s += 1
print(numOf2s*numOf3s)

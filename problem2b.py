letters = open("inputDay2.txt","r")
letterList = [i for i in letters.readlines()]
count = 0
for letter in letterList:
    for letter2 in letterList:
        same = ""
        for i in range(len(letter)):
            if(letter[i] == letter2[i]):
                same += letter[i]
        if(len(same)+1 == len(letter)):
            print(same)
print(len(letterList))

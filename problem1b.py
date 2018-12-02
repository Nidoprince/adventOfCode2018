def findRepeat():
    total = 0
    frequencies = {}
    while(True):
        numbers = open("inputDay1.txt","r")
        for line in numbers:
            total += int(line)
            if(total in frequencies):
                return(total)
            else:
                frequencies[total] = 1
print(findRepeat())

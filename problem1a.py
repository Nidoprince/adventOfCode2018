numbers = open("inputDay1.txt","r")
total = 0
for line in numbers:
    total += int(line)
print(total)

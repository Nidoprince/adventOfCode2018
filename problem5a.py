polymer = open("inputDay5.txt","r")
polymer = [x for x in polymer][0]
def react(a,b):
    return a!=b and a.upper() == b.upper()

reactedPolymer = ""

for element in polymer:
    if(len(reactedPolymer) == 0):
        reactedPolymer += element
    else:
        if(react(element,reactedPolymer[-1])):
            reactedPolymer = reactedPolymer[:-1]
        else:
            reactedPolymer+=element

print(len(reactedPolymer))

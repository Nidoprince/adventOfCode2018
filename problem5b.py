oGpolymer = open("inputDay5.txt","r")
oGpolymer = [x for x in oGpolymer][0]

def react(a,b):
    return a!=b and a.upper() == b.upper()

def findPostReactionLength(polymer):
    reactedPolymer = ""
    for element in polymer:
        if(len(reactedPolymer) == 0):
            reactedPolymer += element
        else:
            if(react(element,reactedPolymer[-1])):
                reactedPolymer = reactedPolymer[:-1]
            else:
                reactedPolymer+=element
    return len(reactedPolymer)

removals = ["aA","bB","cC","dD","eE","fF","gG","hH","iI","jJ","kK","lL","mM","nN","oO","pP","qQ","rR","sS","tT","uU","vV","wW","xX","yY","zZ"]
polymerLengths = [findPostReactionLength(list(filter(lambda c:c not in x,oGpolymer))) for x in removals]
print(sorted(polymerLengths)[0])

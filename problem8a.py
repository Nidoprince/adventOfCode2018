inputData = open("inputDay8.txt","r")
dataPoints = list(map(lambda x: int(x),[x for x in inputData][0].split(" ")))

class treeNode:
    def __init__ (self,branches,data):
        self.numBranches = branches
        self.branches = []
        self.numDataEntries = data
        self.dataEntries = []

    def needsBranches(self):
        return self.numBranches != 0

    def needsData(self):
        return self.numDataEntries != 0

    def addBranch(self,branch):
        self.branches.append(branch)
        self.numBranches -= 1

    def addData(self,data):
        self.dataEntries.append(data)
        self.numDataEntries -= 1

    def done(self):
        return self.numBranches == 0 and self.numDataEntries == 0

    def count(self):
        count = sum(self.dataEntries)
        if(len(self.branches)==0):
            return count
        else:
            return count + sum(list(map(lambda x:x.count(),self.branches)))

stack = []
state = "getNum1"
for number in dataPoints:
    if(state == "getNum1"):
        branchNum = number
        state = "getNum2"
    else:
        if(state == "getNum2"):
            tempNode = treeNode(branchNum,number)
        elif(state == "getData"):
            tempNode.addData(number)
        while(tempNode.done() and len(stack)>0):
            stack[-1].addBranch(tempNode)
            tempNode = stack[-1]
            stack = stack[:-1]
        if(tempNode.needsBranches()):
            stack.append(tempNode)
            state = "getNum1"
        elif(tempNode.needsData()):
            state = "getData"
print(tempNode.count())

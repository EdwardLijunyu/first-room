class CQueue:

    def __init__(self):
        self.accepetStack=[]
        self.outputStack=[]

    def appendTail(self, value: int) -> None:
        self.accepetStack.append(value)

    def deleteHead(self) -> int:
        if self.outputStack==[]:
            while self.accepetStack:
                self.outputStack.append(self.accepetStack.pop())
        if self.outputStack!=[]:
            return self.outputStack.pop()
        else:
            return -1


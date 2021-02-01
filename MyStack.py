

class MyStack():
    def __init__(self):
        self.lst = []

    def top(self):
        if len(self.lst) > 0:
            return(self.lst[len(self.lst) - 1])
        else:
            return(None)

    def empty(self):
        if len(self.lst) == 0:
            return(True)
        else:
            return(False)

    def pop(self):
        if self.empty():
            return "Error, stack is empty!"
        else:
            last = self.lst[-1]
            del(self.lst[-1])
            return(last)

    def push(self, x):
        self.lst.append(x)





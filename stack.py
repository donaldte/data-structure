# Implementation of stack using the principe of LIFO(Last in First out)

class Stack:
    def __init__(self):
        self.list = []

    # function to add the value inside the stack
    def push(self, element):
        self.list.append(element)

    # Function to remove the last added inside the stack
    def pop(self):
        if len(self.list):
            self.list.pop()
        else:
            return None

    # Function which shows the last element without remove
    def peek(self):
        if len(self.list):
            return self.list[len(self.list) - 1]
        else:
            return None

    # Function which return the list
    def __str__(self):
        return str(self.list)


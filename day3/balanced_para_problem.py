class Stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return True if len(self.stack)==0 else False
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return None if self.is_empty() else self.stack.pop()
def check_parenthesis(expr):
    opening="([{"
    closing=")]}"
    stack=Stack()
    for char in expr:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if opening.index(stack.pop())!=closing.index(char):
                return False
    return stack.is_empty()
str=input("Input a string of parenthesis:")
print("valid" if check_parenthesis(str) else "invalid")
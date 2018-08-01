from stack import Stack
from queue import Queue

def isBalanced(input_string):
    if len(input_string) % 2 != 0:
        return False
    elif input_string == '':
        return True
    s = Stack()
    start = list('{[(')
    balanced = True
    i = 0
    while i < len(input_string) and balanced:
        expr = input_string[i]
        if expr == "(" or expr == '[' or expr == '{':
            s.push(expr)
            if s.isEmpty():
                balanced = False 
            elif expr == :
                s.pop()

        i += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    seq = input("Enter the sequence: ")
    print(isBalanced(seq))
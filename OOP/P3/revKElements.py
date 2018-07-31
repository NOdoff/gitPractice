from stack import Stack
from queue import Queue



def revKElements(input_string, k):
    s = Stack()
    q = Queue()
    l_string = input_string.split(',')
    n_string = l_string[:k]
    
    for value in n_string:
        q.enqueue(value)
 

    while not q.isEmpty():
        s.push(q.dequeue())


    while not s.isEmpty():
        q.enqueue(s.pop())

    print( ', '.join(list(q) + l_string[k:]))

if __name__ == '__main__':
    string = input("Enter the list of numbers: ")
    k = int(input("Enter k: "))
    
    revKElements(string, k)

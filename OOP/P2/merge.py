from singly_list import SinglyList, Node
from print_list import print_list

def merge(train1, train2):
    node1 = train1
    node2 = train2
    if not isinstance(train1, Node) or not isinstance(train2, Node) :
        print("This is not Node!")
        return
    while node1.next != None:
        node1 = node1.next
    node1.next = node2

    return node1



if __name__ == '__main__':
    s_list1 = SinglyList()
    a = Node(-1)
    s_list1.add_head(a)

    node = s_list1.head
    b = Node(5)
    c = Node(8)
    d = Node(7)
    a.next = b
    b.next = c
    c.next = d

    s_list2 = SinglyList()
    x = Node(10)
    s_list2.add_head(x)
    node = s_list2.head
    for i in range(10):
        node.next = Node(i)
        node = node.next
    merge(s_list1.head, s_list2.head)
    print_list(s_list1.head)

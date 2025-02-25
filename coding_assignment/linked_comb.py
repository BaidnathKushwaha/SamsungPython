class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self, num):
        self.head = None
        print(f'List-{num} is created')

    def create_node(self, data):
        node = Node(data)
        return node

    def add_node_at_front(self, data):
        if self.head is None:
            self.head = self.create_node(data)
        new_node = self.create_node(data)
        new_node.link = self.head
        self.head = new_node

def create_list(num):
    list = LinkedList(num)
    print(f'Creating List-{num}')
    while True:
        data = input('Enter data of the new node: ')
        list.add_node_at_front(data)
        choice = input('Enter 1 to add node, any other number to stop: ')
        if choice != '1':
            break
    return list

def check_if_converges(list1, list2):
    if list1.head is None or list2.head is None:
        print('Lists do not converge')
        return -1

    # Get the lengths of both lists
    len1 = get_length(list1.head)
    len2 = get_length(list2.head)

    # Find the difference in lengths
    diff = abs(len1 - len2)

    # Set pointers to the beginning of both lists
    temp1 = list1.head
    temp2 = list2.head

    # Move the pointer of the longer list ahead by 'diff' steps
    if len1 > len2:
        for _ in range(diff):
            temp1 = temp1.link
    elif len2 > len1:
        for _ in range(diff):
            temp2 = temp2.link

    # Traverse both lists together and check for convergence
    position = 0
    while temp1 is not None and temp2 is not None:
        if temp1 == temp2:
            return position  # Lists converge at this position
        temp1 = temp1.link
        temp2 = temp2.link
        position += 1

    return -1  # No convergence

def get_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.link
    return count

# Test the code
list1 = create_list(1)
list2 = create_list(2)
position = check_if_converges(list1, list2)
if position == -1:
    print('The lists do not converge')
else:
    print(f'The lists converge at position {position}')
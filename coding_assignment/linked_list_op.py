class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
        print(f'Node with data {data} created')

class LinkedList:  
    def __init__(self):
        self.root = None
        print('An empty linked list is created')

    def length(self):
        current = self.root
        count = 0
        while current:  
            count += 1
            current = current.next
        return count

    def add_node(self):
        data = int(input('Enter data of the new node: '))
        node = Node(data)
        pos = int(input("Enter position to Add:"))
        
        if pos < 0 or pos > self.length(): 
            print("Invalid position!")
            return
        if self.root is None and pos == 0:
            self.root = node
            return
        if pos == 0:
            node.next = self.root
            self.root = node
            return
        
        current = self.root
        index = 0
        while current and index < pos - 1:
            current = current.next
            index += 1
        if current:
            node.next = current.next
            current.next = node
            print(f"Node with data {data} added at position {pos}")
        
    def delete_node(self):
        pos = int(input('Enter pos of the node to be deleted: '))
        
        if pos < 0 or pos >= self.length():  
            print("Invalid position!")
            return
        
        if self.root is None:
            print("Empty linked list")
            return
        
        if pos == 0:
            print(f'Node with data {self.root.data} deleted')
            self.root = self.root.next
            return
        
        current = self.root
        index = 0
        while current and index < pos - 1:
            current = current.next
            index += 1
        
        if current and current.next:
            current.next = current.next.next
            print(f"Node deleted at position {pos}")
    
    def display(self):
        def _reverse_display(node):
            if node is None: 
                return
            _reverse_display(node.next) 
            print(node.data, end=" -> ")
        if self.root is None:
            print("The list is empty.")
        else:
            _reverse_display(self.root)
            print("None")

class Menu:
    def __init__(self):
        pass
    def get_menu(self,events):
        menu={
            1:events.add_node,
            2:events.delete_node,
            3:events.display
        }
        return menu
    def invalid(self):
        print("invalid input")
    def run_menu(self,list):
        while(True):
            choice=int(input("1.Add , 2.Delete , 3.Display , -1. To Exit"))
            if choice==-1:
                break
            menu=self.get_menu(list)
            menu.get(choice,self.invalid)()
        print("End of the Program")
list=LinkedList()
menu=Menu()
menu.run_menu(list)
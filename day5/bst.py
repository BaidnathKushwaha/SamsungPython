import sys

class Node:
    def __init__(self, data = 0):
        self.left = None
        self.data = data
        self.right = None
        print(f'Node with data {data} created')

class Bst:
    def __init__(self):
        self.root = None
        print('An empty Bst is created')

    def add_node(self):
        data = int(input('Enter data of the new node: '))
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if data < temp2.data:
            temp2.left = node
        else:
            temp2.right = node
    

    def delete_node(self):
        pass 

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

    def preorder(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")

    def search_node(self):
        if self.root==None:
            print("Tree is empty")
            return
        data=int(input("Enter the value to be searched:"))
        temp=self.root
        level=1
        while temp!=None:
            if data==temp.data:
                print(f'{data} is found at level {level}')
            elif data< temp.data:
                temp=temp.left
            else :
                temp=temp.right
            level+=1
        print(f'{data} is not found')


class Menu:
    def get_menu(self, bst):
        menu = {
            1 : bst.add_node,
            2 : bst.delete_node,
            3 : bst.inorder,
            4 : bst.preorder,
            5 : bst.postorder,
            6 : bst.search_node,
            7 : self.end_of_program
        }
        return menu
    
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        bst = Bst()
        while True:
            choice = int(input('1:Add 2:Delete 3:InOrder 4:PreOrder 5:PostOrder 6:Search 7:Exit.  Your choice: '))
            menu = self.get_menu(bst)
            menu.get(choice, self.invalid_choice)()

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()
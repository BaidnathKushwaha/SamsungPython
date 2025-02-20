# delete front and insert front using stack

import sys
class Stack:
    def __init__(self,size=5):
        self.stack=[]
        self.size=size
    def insert_front(self):
        if len(self.stack)>=self.size:
            print("stack is full")
        else:
            item=int(input("Enter the item is to be inserted:"))
            self.stack.insert(0,item)
    def delete_front(self):
        if len(self.stack)<0:
            print("stack is empty")
        else:
            print(self.stack.pop(0))
    def display(self):
        if len(self.stack)<0:
            print("stack is empty")
        else:
            print("stack is : ",self.stack , end=" ")
class Menu:
    def __init__(self):
        pass
    def get_menu(self,events):
        menu={
            1:events.insert_front,
            2:events.delete_front,
            3:events.display,
            4:self.end_of_program
        }
        return menu
    def end_of_program(self):
        sys.exit("Exit")
    def invalid_choice(self):
        print("Invalid choice")
    def run_menu(self,events):
        while(True):
            choice=int(input("1.Insert , 2.Delete , 3.Display , -1. To Exit"))
            if choice==-1:
                break
            menu=self.get_menu(events)
            menu.get(choice,self.invalid_choice)()
        print("End of the Program")
stack=Stack()
menu=Menu()
menu.run_menu(stack)
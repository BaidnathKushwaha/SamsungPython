# normal Queue

import sys
class Queue:
    def __init__(self,size=5):
        self.queue=[]
        self.size=size
    def push(self):
        if len(self.queue)>=self.size:
            print("stack is full")
        else:
            item=int(input("Enter the item is to be inserted:"))
            self.queue.append(item)
    def pull(self):
        if len(self.queue)<0:
            print("stack is empty")
        else:
            print(self.queue.pop(0))
    def display(self):
        if len(self.queue)<0:
            print("stack is empty")
        else:
            print("stack is : ",self.queue , end=" ")
class Menu:
    def __init__(self):
        pass
    def get_menu(self,events):
        menu={
            1:events.push,
            2:events.pull,
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
queue=Queue()
menu=Menu()
menu.run_menu(queue)
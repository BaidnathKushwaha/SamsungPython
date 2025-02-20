def monday():
    print("Today is Technical Fest")
def tuesday():
    print("Today is nothing")
def wednesday():
    print("Today is dept day")
def friday():
    print("Today is Ethenic day")
def other_day():
    print("Invalid choice")
menu={
    1:monday,
    2:tuesday,
    3:wednesday,
    4:friday
}
while(True):
    choice=int(input("1.Monday , 2.Tuesday , 3.Wednesday , 4. Friday , -1. To Exit"))
    if choice==-1:
        break
    menu.get(choice,other_day)()
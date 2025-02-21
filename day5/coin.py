def change(a):
    coins=[10,5,2,1]
    coins_count={}
    for coin in coins:
        coins_count[coin]=a//coin
        a%=coin
    print(coins_count)
amount=int(input("Enter the amount: "))
change(amount)
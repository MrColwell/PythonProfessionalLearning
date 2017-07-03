def main():
    money=eval(input("Enter change amount: "))
    money=money * 100
    money=int(round(money))
    print(money)
    print("Number of toonies:",money//200)
    money=money%200
    print("Number of loonies:",money//100)
    money=money%100
    print("Number of quarters:",money//25)
    money=money%25
    print("Number of dimes:",money//10)
    money=money%10
    print("Number of nickels:",int(money/5))

main()

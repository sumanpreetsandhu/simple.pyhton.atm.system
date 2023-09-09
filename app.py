bal=0
def deposit():
    amt = int(input("Enter amount to deposit: "))
    global bal
    bal = bal+amt
    print("Amount Deposited success")

def withdraw():
    amt = int(input("Enter amount to Withdraw: "))
    global bal
    bal = bal - amt
    print("Amount withdraw success")

def balance():
    global bal
    print("Your Account Balance is: ", bal)    

#-----------------------------------------------
y="y"
while y=="y" or y=="Y": 
    password = input("Enter password: ")
    if(password=="123"):
       print("1 for Deposit: ")
       print("2 for Withdraw: ")
       print("3 for Balance: ")
       choice = int(input())
       if choice==1:
           deposit()
       elif choice==2:
           withdraw()
       elif choice==3:
           balance()
       else:
           print("Enter a Valid Choice")
    else:
        print("Wrong Password")

    print("Press Y to continue / N for Exit")
    y=input()


    

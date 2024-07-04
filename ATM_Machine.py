#JDO BANK ATM MACHINE
print("WELCOME TO JDO BANK KENYA\n PLEASE INSERT YOUR CARD")

#Variables
pin = 5023
chances = 3
Bal = 1000
Min_bal = 0
choice = 0

#Pin initialization
while chances != 0:

    user_pin = int(input(f"Please enter your 4-digit pin : \n"))
    if user_pin == pin :
        print("Pin Correct")
    if user_pin != pin :
        chances -=1
        print("Incorrect Pin!! Try again\n")
        print(f"You have {chances} chances left")

#Transaction Menu
    else:
        user_choice = int(input("1 : balance,\n2 : deposit,\n3 : withdraw,\n4 : exit\n"))

#Confirming balance
        if user_choice == 1:
            print(f"Your A/C balance is KSH. {Bal}")

#Initializing deposit
        if user_choice == 2:
            deposit_user = float(input("Enter the amount to be deposited :KSH. "))
            total_balance = deposit_user + Bal
            print(f"Your have deposited KSH. {deposit_user}")
            print(f"Your total balance is KSH. {total_balance}")
        
#Initializing withdrawal 
        if user_choice == 3:
            
            withdraw_user = float(input("Enter the amount to be withdrawn :KSH. "))
            print(f"Your withdrawal of KSH. {withdraw_user} was diclined")
            if Bal - withdraw_user < Min_bal:
                print(f"Insufficient funds. Your balance cannot be less than your Min_bal KSH. {Min_bal}")
            else:
             print(f"You have withdrawn KSH. {withdraw_user}")
             total_balance = Bal - withdraw_user
             print(f"Your total balance is KSH. {total_balance}")

#Exit transaction
        user_exit = input("Would you like to exit? Yes/No \n")
        if user_exit == "Yes":
            print("Thank you for using JDO bank !!")
            break
        else:
            continue

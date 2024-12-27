import time
class ATM:
    def __init__(self,pin=1234,balance=500):
        self.pin=pin
        self.balance=balance
        self.Transaction_History=[]

    def verify_pin(self):
        for _ in range (3):
            print("Insert Your Card")
            time.sleep(5)
            entered_pin=int(input("Enter Your Pin:"))
            if entered_pin==self.pin:
                return True
            print("Incorrect pin Try Again")
        print("TOO Many attempts")
        return False
    
    def check_balance(self):
        print(f"Your Currrent Balance is {self.balance:.2f}")
        self.Transaction_History.append("Balance Checked.")

    def deposit(self):
        amount=float(input("Enter amount to Deposit : "))
        if amount > 0:
            self.balance+=amount
            print(f"{amount:.2f} deposited successfully")
            self.Transaction_History.append(f"Deposited amount {amount:.2f}.")
        else:
            print("Invalid amount")
    
    def withdraw(self):
        amount=float(input("Enter amount to withdraw : "))
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print("Withdrawn successful")
            self.Transaction_History.append(f"Amount{amount:.2f} withdrawn")
        else:
            print("Insufficient Balance")

    def change_pin(self):
        new_pin=int(input("Enter Your New ATM Pin : "))
        confirm_pin=int(input("Confirm Your Pin : "))
        if new_pin==confirm_pin and 1000<=new_pin<=9999:
            print("PIN changed successfully")
            self.pin=new_pin
            self.Transaction_History.append("Changed Pin")
        else:
            print("Invalid Pin or Pins do not match")
        
    def view_transactionhistory(self):
        print("\nTransaction History : ")
        if not self.Transaction_History:
            print("NO transaction yet")
        else:
            for i,transaction in enumerate(self.Transaction_History,1):
                print(f"{i}.{transaction}")
        
    def start(self):
        if not self.verify_pin():
            return
        while True:
            print("\n == ATM Menu == ")
            print("1.Check Balance")
            print("2.Deposit Cash")
            print("3.Withdraw Amount")
            print("4.Change Pin")
            print("5.View Transaction History")
            print("6.Exit")
            choice=input("Choose an option : ")

            if choice=="1":
                self.check_balance()
            elif choice=="2":
                self.deposit()
            elif choice=="3":
                self.withdraw()
            elif choice=="4":
                self.change_pin()
            elif choice=="5":
                self.view_transactionhistory()
            elif choice=="6":
                print("Thank You for Visiting Us")
                break
            else:
                print("Invalid Choice")


atm=ATM()
atm.start()
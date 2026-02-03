#atm menu driven program
#Menu: Deposit, Withdraw, Check Balance, Exit. Keep running until q.
class hdfcbank:
    def __init__(self,deposit_money,withdraw_money,checkbal_money,exit_q):
            self.exit_q = exit_q
            self.deposit_money = deposit_money
            self.withdraw_money = withdraw_money
            self.checkbal_money = checkbal_money 
               
    def bank_info(self):
        while True:
                user_input=input("ENTER YOUR CHOICE OR q TO QUIT:")
                if user_input == "q":
                       return (f"THANKS FOR VISITING US!!{self.exit_q}")
                elif user_input == "deposit":
                       return (f"YOUR DEPOSIT AMOUNT IS:{self.deposit_money}")
                elif user_input == "withdraw":
                       return (f"YOUR WITHDRAW AMOUNT IS:{self.withdraw_money}")
                elif user_input == "check balance":
                       return (f"YOUR BALANCE AMOUNT IS:{self.checkbal_money}")
                else:
                        return ("INVALID INPUT")
        
hdfc = hdfcbank(1000,500,1500,"QUIT")
print(hdfc.bank_info())
                
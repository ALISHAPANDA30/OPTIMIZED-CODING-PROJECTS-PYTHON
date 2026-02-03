#atm menu driven program
#Menu: Deposit, Withdraw, Check Balance, Exit. Keep running until q.
class hdfcbank:
    def _init_ (self,deposit_money,withdraw_money,checkbal_money,exit_q):
            self.exit_q = exit_q
            self.deposit_money = deposit_money
            self.withdraw_money = withdraw_money
            self.checkbal_money = checkbal_money 
               
    def bank_info(self):
        user_input=input("ENTER YOUR CHOICE OR q TO QUIT:")
        if user_input == q:
                return (f"THANKS FOR VISITING US!!{self.exit_q})
                break
        elif user_input == deposit
                
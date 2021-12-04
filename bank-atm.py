class ATM(object):
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin
    
    def balanceEnquiry(self):
        print('Your balance is 10,00,000 rupees.')   
    
    def cashWithdrawal(self, amount):
        newAmt = 1000000 - amount
        print('you have withdrawn Rs. ' + str(amount) + '. Your reamaining balance is Rs. '+ str(newAmt))

def main():
    print('*Bank ATM*')
    Card = input('Enter your card number:- ')
    PIN = input('Enter your pin number:- ')
    newUser = ATM(Card, PIN)
    
    print('What would you like to do?')
    print('Enter "1" for Balance Enquiry and "2" for Cash Withdrawl')
    activity = int(input('Enter your activity:- '))
    
    if (activity == 1):
        newUser.balanceEnquiry()
    elif (activity == 2):
        amt = int(input('Enter your amount:- '))
        newUser.cashWithdrawal(amt)
    else:
        print('Enter a valid number')

if (__name__ == "__main__"):
    main()
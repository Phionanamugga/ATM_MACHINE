import time

# Users account details with PIN and balance
users = {
    '1234': { 'balance': 300000, 'transactions': [] },
    '5678': { 'balance':100000, 'transactions': [] },
    '3456': { 'balance': 400000, 'transactions': [] }
}   
       
 # Initialize block users
blocked_users = set()

# Function for authentication of users
def authenticate():
    attempts=3
    while attempts > 0:
        pin = input('Enter your 4-digit PIN: ')
        if pin in blocked_users:
            print('Your account has been blocked. Please contact customer service')
            return None
        if pin in users:
            print('Authentication successful')
            return pin
        else:
            attempts = 2
            print('Invalid PIN. 1 attempt left')

    print('Too many failed attempts. Your account has been blocked')
    blocked_users.add(pin)
    return None


# Function for login
def login():
    print('Welcome to the ATM')
    print('******************')
    print('Enter your 4-digit PIN')
    pin = input('>>> ')
    if pin in users:
        if pin in blocked_users:
            print('Your account has been blocked. Please contact customer service')
            return False
        print('Login successful')
        return pin
    else:
        print('Invalid PIN')        
        
       
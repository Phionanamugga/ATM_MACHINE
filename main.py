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
        
# function to display the menu
def menu():
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Complaint')
    print('4. Check balance')
    print('5. Change PIN')
    print('6. Exit')
    return input('Select an option: ')

# check balance function
def check_balance(user_pin):
    print(f'Your account balance is: {users[user_pin]["balance"]}')
    return True

# function deposit money
def deposit(user_pin):
    amount = int(input('Enter amount to deposit: '))
    if amount > 0:
        users[user_pin]['balance'] += amount
        users[user_pin]['transactions'].append(f'You deposited {amount}')
        print(f'Your new balance is: {users[user_pin]["balance"]}')
    else:
        print('Invalid amount')

# function to withdraw money
def withdraw(user_pin):
    amount = int(input('Enter amount to withdraw: '))
    if amount > 0:
        if amount <= users[user_pin]['balance']:
            users[user_pin]['balance'] -= amount
            users[user_pin]['transactions'].append(f'You withdrew {amount}')
            print(f'Your new balance is: {users[user_pin]["balance"]}')
        else:
            print('Insufficient funds')
    else:
        print('Invalid amount')      
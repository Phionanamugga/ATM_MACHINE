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
         
       
from flask import Flask, request, jsonify, render_template
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
#import os
#import requests
#import json
#import random
#import string
#import datetime
#import jwt
#from functools import wraps
#from werkzeug.security import generate_password_hash, check_password_hash

import time

app = Flask(__name__)

# Users account details with PIN and balance
'''users = {
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



# Login endpoint
@app.route('/login', methods=['POST'])
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


# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)'''

# Users account details with PIN and balance
users = {
    '1234': {'balance': 300000, 'transactions': []},
    '5678': {'balance': 100000, 'transactions': []},
    '3456': {'balance': 400000, 'transactions': []}
}

# Initialize blocked users
blocked_users = set()

# Global variable to track logged-in user (simplified session)
current_user = None

# Root route to render the HTML template
@app.route('/')
def home():
    return render_template('index.html')

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    global current_user
    data = request.get_json()
    pin = data.get('pin')
    
    if pin in users:
        if pin in blocked_users:
            return jsonify({'message': 'Your account has been blocked. Please contact customer service'}), 403
        current_user = pin
        return jsonify({'message': 'Login successful', 'pin': pin}), 200
    else:
        return jsonify({'message': 'Invalid PIN'}), 401

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    global current_user
    current_user = None
    return jsonify({'message': 'Logged out successfully'}), 200

# Check balance endpoint
@app.route('/balance', methods=['GET'])
def check_balance():
    if not current_user:
        return jsonify({'message': 'Please log in first'}), 401
    balance = users[current_user]['balance']
    return jsonify({'message': f'Your account balance is: {balance}', 'balance': balance}), 200

# Deposit endpoint
@app.route('/deposit', methods=['POST'])
def deposit():
    if not current_user:
        return jsonify({'message': 'Please log in first'}), 401
    data = request.get_json()
    amount = data.get('amount', 0)
    
    if amount > 0:
        users[current_user]['balance'] += amount
        users[current_user]['transactions'].append(f'You deposited {amount}')
        return jsonify({'message': f'Your new balance is: {users[current_user]["balance"]}'}), 200
    else:
        return jsonify({'message': 'Invalid amount'}), 400

# Withdraw endpoint
@app.route('/withdraw', methods=['POST'])
def withdraw():
    if not current_user:
        return jsonify({'message': 'Please log in first'}), 401
    data = request.get_json()
    amount = data.get('amount', 0)
    
    if amount > 0:
        if amount <= users[current_user]['balance']:
            users[current_user]['balance'] -= amount
            users[current_user]['transactions'].append(f'You withdrew {amount}')
            return jsonify({'message': f'Your new balance is: {users[current_user]["balance"]}'}), 200
        else:
            return jsonify({'message': 'Insufficient funds'}), 400
    else:
        return jsonify({'message': 'Invalid amount'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
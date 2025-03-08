import pytest
from main import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    # Reset state after each test
    app.current_user = None

def test_login_success(client):
    response = client.post('/login', json={'pin': '1234'})
    assert response.status_code == 200
    assert response.json['message'] == 'Login successful'
    assert app.current_user == '1234'

def test_login_invalid_pin(client):
    response = client.post('/login', json={'pin': '9999'})
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid PIN'
    assert app.current_user is None

def test_login_blocked_user(client):
    app.blocked_users.add('1234')
    response = client.post('/login', json={'pin': '1234'})
    assert response.status_code == 403
    assert response.json['message'] == 'Your account has been blocked. Please contact customer service'
    app.blocked_users.clear()  # Clean up

def test_balance_logged_in(client):
    client.post('/login', json={'pin': '5678'})
    response = client.get('/balance')
    assert response.status_code == 200
    assert response.json['message'] == 'Your account balance is: 100000'
    assert 'balance' in response.json

def test_balance_not_logged_in(client):
    response = client.get('/balance')
    assert response.status_code == 401
    assert response.json['message'] == 'Please log in first'

def test_deposit_success(client):
    client.post('/login', json={'pin': '3456'})
    response = client.post('/deposit', json={'amount': 5000})
    assert response.status_code == 200
    assert response.json['message'] == 'Your new balance is: 405000'
    assert app.users['3456']['balance'] == 405000
    assert 'You deposited 5000' in app.users['3456']['transactions']

def test_deposit_invalid_amount(client):
    client.post('/login', json={'pin': '1234'})
    response = client.post('/deposit', json={'amount': -100})
    assert response.status_code == 400
    assert response.json['message'] == 'Invalid amount'

def test_deposit_not_logged_in(client):
    response = client.post('/deposit', json={'amount': 1000})
    assert response.status_code == 401
    assert response.json['message'] == 'Please log in first'

def test_withdraw_success(client):
    client.post('/login', json={'pin': '1234'})
    response = client.post('/withdraw', json={'amount': 10000})
    assert response.status_code == 200
    assert response.json['message'] == 'Your new balance is: 290000'
    assert app.users['1234']['balance'] == 290000
    assert 'You withdrew 10000' in app.users['1234']['transactions']

def test_withdraw_insufficient_funds(client):
    client.post('/login', json={'pin': '5678'})
    response = client.post('/withdraw', json={'amount': 200000})
    assert response.status_code == 400
    assert response.json['message'] == 'Insufficient funds'

def test_withdraw_invalid_amount(client):
    client.post('/login', json={'pin': '3456'})
    response = client.post('/withdraw', json={'amount': 0})
    assert response.status_code == 400
    assert response.json['message'] == 'Invalid amount'

def test_withdraw_not_logged_in(client):
    response = client.post('/withdraw', json={'amount': 1000})
    assert response.status_code == 401
    assert response.json['message'] == 'Please log in first'

def test_logout_success(client):
    client.post('/login', json={'pin': '1234'})
    response = client.post('/logout')
    assert response.status_code == 200
    assert response.json['message'] == 'Logged out successfully'
    assert app.current_user is None

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the ATM' in response.data  # Check HTML content
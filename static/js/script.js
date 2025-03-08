function login() {
    const pin = document.getElementById('pin').value;
    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pin: pin })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('login-message').textContent = data.message;
        if (data.message === 'Login successful') {
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('menu-section').style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
}

function logout() {
    fetch('/logout', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        document.getElementById('menu-message').textContent = data.message;
        document.getElementById('menu-section').style.display = 'none';
        document.getElementById('login-section').style.display = 'block';
        resetForms();
    });
}

function showBalance() {
    fetch('/balance')
    .then(response => response.json())
    .then(data => {
        resetForms();
        document.getElementById('balance-section').style.display = 'block';
        document.getElementById('balance').textContent = data.message;
        document.getElementById('menu-message').textContent = '';
    })
    .catch(() => document.getElementById('menu-message').textContent = 'Please log in first');
}

function showDeposit() {
    resetForms();
    document.getElementById('deposit-section').style.display = 'block';
}

function deposit() {
    const amount = parseInt(document.getElementById('deposit-amount').value);
    fetch('/deposit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount: amount })
    })
    .then(response => response.json())
    .then(data => document.getElementById('menu-message').textContent = data.message);
}

function showWithdraw() {
    resetForms();
    document.getElementById('withdraw-section').style.display = 'block';
}

function withdraw() {
    const amount = parseInt(document.getElementById('withdraw-amount').value);
    fetch('/withdraw', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount: amount })
    })
    .then(response => response.json())
    .then(data => document.getElementById('menu-message').textContent = data.message);
}

function resetForms() {
    document.getElementById('balance-section').style.display = 'none';
    document.getElementById('deposit-section').style.display = 'none';
    document.getElementById('withdraw-section').style.display = 'none';
    document.getElementById('menu-message').textContent = '';
}
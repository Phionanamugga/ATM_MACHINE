# ATM Web Application
A modern, web-based ATM system built with Flask, HTML5, CSS3, and JavaScript (ES6+). This application allows users to log in with a PIN, check their balance, deposit funds, withdraw money, and log out—all through a sleek, responsive interface. The backend runs on a lightweight Flask server, serving both a RESTful API and a rendered HTML template, making it a full-stack solution for banking simulation.

## Features✨ 
Secure Login: Authenticate users with a 4-digit PIN.
Account Management: Check balances, deposit, and withdraw funds with real-time updates.
Responsive Design: Works seamlessly on desktop, tablet, and mobile devices.
Transaction Logging: Tracks deposits and withdrawals in memory.
RESTful API: Backend endpoints for programmatic access.
Latest Tech: Built with modern web standards and Python 3.11+.

## Tech Stack🛠️ 

Layer	    Technology	                    Version
Backend	    Flask(Python Framework)	        3.0.x
Frontend	HTML5, CSS3, JavaScript (ES6+)	Latest
Server	    Gunicorn (WSGI Server)	        22.x
Deployment	Docker, NGINX	                Latest
Tools	    Git, GitHub Actions (CI/CD)	-
Testing	    Pytest	                        8.x

## Prerequisites📋 
Python: 3.11 or higher
Node.js: 20.x (optional, for frontend tooling if extended)
Docker: 24.x (for containerized deployment)
Git: 2.40+ for version control

## Quick Start🚀 
1. Clone the Repository
git clone https://github.com/Phionanamugga/atm-web-app.git
cd atm-web-app

2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv/Scripts/activate

3. Install Dependencies
pip install -r requirements.txt


4. Run the Application
python atm_server.py
Open your browser to http://localhost:5004.

## Project Structure🏗️ 
atm-web-app/
├── static/              # Static assets
│   ├── css/
│   │   └── style.css    # Styling for the frontend
│   └── js/
│       └── script.js    # Frontend logic
├── templates/
│   └── index.html       # Main HTML template
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── atm_server.py        # Flask backend
├── .github/             # GitHub Actions for CI/CD
│   └── workflows/
│       └── ci.yml
└── README.md            # This file

## Dependencies📦
Defined in requirements.txt:
Flask==3.0.0
gunicorn==22.0.0
To install:
pip install -r requirements.txt


## Docker Deployment🐳 
Build the Docker Image
docker build -t atm-web-app:latest .

### Run the Container
docker run -d -p 5000:5000 atm-web-app:latest
Access at http://localhost:5000.
Dockerfile

dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "atm_server:app"]

## API Endpoints🌐 
Endpoint	Method	Description	Request Body	Response Example
/	GET	Render main page	-	HTML page
/login	POST	Authenticate user	{"pin": "1234"}	{"message": "Login successful"}
/balance	GET	Get user balance	-	{"balance": 300000}
/deposit	POST	Deposit funds	{"amount": 5000}	{"message": "New balance: 305000"}
/withdraw	POST	Withdraw funds	{"amount": 10000}	{"message": "New balance: 295000"}
/logout	POST	Log out user	-	{"message": "Logged out"}

## Testing🧪 
Run tests with Pytest (optional setup):
pip install pytest
pytest tests/
Note: Add a tests/ folder with test cases (e.g., test_atm.py) for full coverage.

## Deployment🚀 
Using Heroku

Install Heroku CLI.
Create a Procfile:
text
web: gunicorn atm_server:app
Deploy:
heroku create atm-web-app
git push heroku main
Using GitHub Actions

CI/CD pipeline in .github/workflows/ci.yml for automated testing and deployment.

## Contributing🤝 
We welcome contributions! Follow these steps:
Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.
Please read CONTRIBUTING.md for details.

## License📜 
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments🌟 
Flask Community: For an awesome framework.
xAI: Inspiration from cutting-edge AI assistants like Grok.
You: For exploring this project!

## Contact📞 
Author: Phiona Namugga
GitHub: Phionanamugga
Latest Tech Highlights

Python 3.11: Faster runtime with new features like exception groups.
Flask 3.0: Improved async support and modern routing.
Docker: Containerization for consistent deployment.
GitHub Actions: Automated CI/CD for 2025 workflows.
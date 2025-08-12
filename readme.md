
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple Flask application using **Flask-SQLAlchemy** and **Werkzeug** for authentication.

---

## 🚀 Features
- User authentication with hashed passwords
- Database integration via SQLAlchemy
- Modular Flask app structure
- Ready for deployment

---

## 📦 Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>

2. Create and activate a virtual environment (recommended):

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt




---

🔑 Configuration

Create a .env file or set environment variables in your terminal:

SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///your_database.db


---

▶️ Running the Application

1. Set the Flask app environment variable:

# Windows (Powershell)
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# macOS / Linux
export FLASK_APP=app.py
export FLASK_ENV=development


2. Run the server:

flask run


3. Access the app:
http://127.0.0.1:5000

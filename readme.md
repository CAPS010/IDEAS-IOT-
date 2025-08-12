# Flask Application with PostgreSQL

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A secure Flask application using *Flask-SQLAlchemy, **PostgreSQL, and **Werkzeug* for authentication.  
The application uses environment variables to securely store database credentials.

---

## 🚀 Features
- PostgreSQL database integration
- Secure credential storage with .env
- User authentication with hashed passwords
- Auto-generated session secret key
- Ready for local development or deployment

---

## 📦 Requirements
- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL 14 or newer
- Virtual environment (recommended)

---

## ⚙ Installation

1. *Clone the repository*:
   ```bash
   git clone https://github.com/Aathisivansk/IDEAS-IOT-.git
   cd <your-repo-name>

2. Create and activate a virtual environment:

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Create a PostgreSQL database:

# Access PostgreSQL shell
psql -U postgres

# Inside psql
CREATE DATABASE ideasiot;
\q


5. Create a .env file (this file will not be committed to GitHub):

DATABASE_URL=postgresql://postgres:your_password@localhost:5432/ideasiot


6. Add .env to .gitignore:

.env




---

▶ Running the Application

1. Set the Flask app environment variables:

# Windows (Powershell)
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# macOS / Linux
export FLASK_APP=app.py
export FLASK_ENV=development


2. Run database migrations (if using Flask-Migrate):

flask db upgrade


3. Run the server:

flask run


4. Access the app:
http://127.0.0.1:5000




---

📌 Notes

The secret key is randomly generated each time the app starts (os.urandom(24)), so sessions reset on restart.

For production, use a fixed secure secret key in your .env file.

Do not commit .env to GitHub.



---

📜 License

This project is licensed under the MIT License.


---

💡 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss your ideas.

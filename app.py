from datetime import datetime
from flask import Flask, flash, redirect,render_template, request, session, url_for
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
# Secret key for session management
app.secret_key = os.urandom(24)


# Configure PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)   

# TABLE 1 LOGIN CREDENTIALS
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password_hash = db.Column(db.String(512), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	role = db.Column(db.String(50), nullable=False, default='Student')
	last_login = db.Column(db.DateTime, nullable=True)
	
	def __repr__(self):
		return f'<User {self.username}>'
	
class MotorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motor_id = db.Column(db.String(50), nullable=False)
    voltage = db.Column(db.Float, nullable=False)
    current = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)
    over_voltage = db.Column(db.Float, nullable=False)
    over_load_details = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<MotorData {self.motor_id} - Voltage: {self.voltage}, Current: {self.current}, Power: {self.power}>'

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))

    return render_template('dashboard.html', ur=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		if user and check_password_hash(user.password_hash, password):
			session['user_id'] = user.id
			session['username'] = user.username
			user.last_login = datetime.utcnow()
			db.session.commit()             
			return redirect(url_for('dashboard', username=username))
		flash('Invalid username or password', 'danger')
	return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']
		confirm_password = request.form['confirm_password']
		role = request.form['role']
		terms = request.form.get('terms')

		if not terms:
			flash('You must agree to the terms and conditions', 'danger')
			return redirect(url_for('register'))

		if password != confirm_password:
			flash('Passwords do not match', 'danger')
			return redirect(url_for('register'))

		password_hash = generate_password_hash(password)
		last_login = datetime.utcnow()
		new_user = User(username=username, email=email, password_hash=password_hash, role=role, last_login=last_login)
		db.session.add(new_user)
		db.session.commit()
		flash('Registration successful! You can now log in.', 'success')
		return redirect(url_for('login'))

	return render_template('register.html')

@app.route('/logout')
def logout():
    # Remove the user's ID and username from the session
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

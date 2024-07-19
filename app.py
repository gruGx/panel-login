from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Sekret do sesji

# Użytkownik i hasło do logowania
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html', error="Invalid credentials")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html')

@app.route('/restart', methods=['POST'])
def restart():
    if 'username' not in session:
        return redirect(url_for('home'))
    os.system('shutdown -r -t 0')  # Restart systemu (możesz zmienić na inną komendę)
    return 'System is restarting...', 200

if __name__ == '__main__':
    app.run(debug=True)


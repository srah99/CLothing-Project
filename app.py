from flask import Flask, render_template, request, redirect, url_for, session
from services.auth_service import AuthService
from services.firestore_service import FirestoreService

app = Flask(__name__)
app.secret_key = 'supersecretkey'

auth_service = AuthService()
firestore_service = FirestoreService()

@app.route('/')
def index():
    if 'user' in session:
        return f'Logged in as: {session["user"]["email"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth_service.login(email, password)
        if user:
            session['user'] = user
            return redirect(url_for('index'))
        return 'Failed to login'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


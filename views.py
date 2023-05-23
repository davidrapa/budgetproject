from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budgetproject.sqlite'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            return render_template('login.html', error='Invalid username or password')

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/income')
@login_required
def income():
    return render_template('income.html')

@app.route('/expenses')
@login_required
def expenses():
    return render_template('expenses.html')

@app.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Store feedback in memory (in production, use a database)
feedback_list = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    if username and password:  # Simple validation
        session['user'] = username
        return redirect(url_for('greeting'))
    return redirect(url_for('login'))

@app.route('/greeting')
def greeting():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('greeting.html', user=session['user'])

@app.route('/about')
def about():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('feedback.html', feedback_list=feedback_list)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if 'user' not in session:
        return redirect(url_for('login'))
    name = request.form['name']
    message = request.form['message']
    feedback_list.append({'name': name, 'message': message, 'date': datetime.now().strftime('%Y-%m-%d %H:%M')})
    return redirect(url_for('feedback'))

@app.route('/quiz')
def quiz():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('quiz.html')

@app.route('/quiz_result', methods=['POST'])
def quiz_result():
    if 'user' not in session:
        return redirect(url_for('login'))
    answers = request.form
    score = 0
    if answers.get('q1') == 'Paris':
        score += 1
    if answers.get('q2') == '4':
        score += 1
    if answers.get('q3') == 'Blue':
        score += 1
    return render_template('quiz_result.html', score=score)

@app.route('/age_calculator')
def age_calculator():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('age_calculator.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    if 'user' not in session:
        return redirect(url_for('login'))
    birth_date = request.form['birth_date']
    birth = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return render_template('age_result.html', age=age, birth_date=birth_date)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
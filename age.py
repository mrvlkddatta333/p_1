from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

CALCULATOR_HTML = '''
<h2>Age Calculator</h2>
<form method="POST">
    Enter your birth date: <input type="date" name="birth_date" required><br><br>
    <input type="submit" value="Calculate Age">
</form>
'''

RESULT_HTML = '''
<h2>Age Calculation Result</h2>
<p>Birth Date: {}</p>
<p>Your Age: {} years old</p>
<p>Days lived: {} days</p>
<a href="/">Calculate Again</a>
'''

@app.route('/', methods=['GET', 'POST'])
def age_calculator():
    if request.method == 'POST':
        birth_date = request.form['birth_date']
        birth = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.now()
        
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        days = (today - birth).days
        
        return RESULT_HTML.format(birth_date, age, days)
    
    return CALCULATOR_HTML

if __name__ == '__main__':
    app.run(debug=True, port=5006)
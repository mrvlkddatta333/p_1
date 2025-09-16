from flask import Flask, request, render_template_string

app = Flask(__name__)

QUIZ_HTML = '''
<h2>Simple Quiz</h2>
<form method="POST">
    <p>1. What is the capital of India?</p>
    <input type="radio" name="q1" value="Mumbai"> Mumbai<br>
    <input type="radio" name="q1" value="Delhi"> Delhi<br>
    <input type="radio" name="q1" value="Kolkata"> Kolkata<br><br>
    
    <p>2. What is 5 + 3?</p>
    <input type="radio" name="q2" value="7"> 7<br>
    <input type="radio" name="q2" value="8"> 8<br>
    <input type="radio" name="q2" value="9"> 9<br><br>
    
    <p>3. Which is a programming language?</p>
    <input type="radio" name="q3" value="Python"> Python<br>
    <input type="radio" name="q3" value="HTML"> HTML<br>
    <input type="radio" name="q3" value="CSS"> CSS<br><br>
    
    <input type="submit" value="Submit Quiz">
</form>
'''

RESULT_HTML = '''
<h2>Quiz Results</h2>
<p>Your Score: {}/3</p>
<p>{}</p>
<a href="/">Take Quiz Again</a>
'''

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        if request.form.get('q1') == 'Delhi':
            score += 1
        if request.form.get('q2') == '8':
            score += 1
        if request.form.get('q3') == 'Python':
            score += 1
        
        message = "Excellent!" if score == 3 else "Good!" if score >= 2 else "Try Again!"
        return RESULT_HTML.format(score, message)
    
    return QUIZ_HTML

if __name__ == '__main__':
    app.run(debug=True, port=5005)
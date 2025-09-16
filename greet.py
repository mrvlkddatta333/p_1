from flask import Flask, request, render_template_string

app = Flask(__name__)

FORM_HTML = '''
<h2>Greeting Application</h2>
<form method="POST">
    Enter your name: <input type="text" name="name" required><br><br>
    <input type="submit" value="Greet Me">
</form>
'''

GREETING_HTML = '''
<h2>Hello, {}!</h2>
<p>Welcome to our greeting application!</p>
<a href="/">Greet someone else</a>
'''

@app.route('/', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        name = request.form['name']
        return GREETING_HTML.format(name)
    return FORM_HTML

if __name__ == '__main__':
    app.run(debug=True, port=5002)
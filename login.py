from flask import Flask, request, render_template_string

app = Flask(__name__)
users = {}

LOGIN_HTML = '''
<h2>Login System</h2>
<form method="POST" action="/login">
    Username: <input type="text" name="username" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    <input type="submit" value="Login">
</form>
<p><a href="/signup">Don't have an account? Sign up</a></p>
'''

SIGNUP_HTML = '''
<h2>Sign Up</h2>
<form method="POST" action="/signup">
    Username: <input type="text" name="username" required><br><br>
    Password: <input type="password" name="password" required><br><br>
    <input type="submit" value="Sign Up">
</form>
<p><a href="/">Already have an account? Login</a></p>
'''

SUCCESS_HTML = '<h2>Welcome, {}!</h2><p><a href="/">Logout</a></p>'
ERROR_HTML = '<h2>Error: {}</h2><p><a href="/">Try Again</a></p>'

@app.route('/')
def home():
    return LOGIN_HTML

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return SUCCESS_HTML.format(username)
    return ERROR_HTML.format('Invalid username or password')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return ERROR_HTML.format('Username already exists')
        users[username] = password
        return SUCCESS_HTML.format(username)
    return SIGNUP_HTML

if __name__ == '__main__':
    app.run(debug=True, port=5001)
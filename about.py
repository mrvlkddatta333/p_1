from flask import Flask

app = Flask(__name__)

ABOUT_HTML = '''
<h2>About Me</h2>
<p><strong>Name:</strong> Flask Developer</p>
<p><strong>Skills:</strong> Python, Flask, Web Development</p>
<p><strong>Experience:</strong> Building simple web applications</p>
<p><strong>Interests:</strong> Programming, Technology, Learning</p>
<p><strong>Contact:</strong> developer@example.com</p>
<hr>
<p>This is a simple about page created using Flask framework.</p>
'''

@app.route('/')
def about():
    return ABOUT_HTML

if __name__ == '__main__':
    app.run(debug=True, port=5003)
from flask import Flask, request, render_template_string

app = Flask(__name__)
feedback_list = []

FEEDBACK_HTML = '''
<h2>Feedback Form</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Message: <textarea name="message" required></textarea><br><br>
    <input type="submit" value="Submit Feedback">
</form>

<h3>All Feedback:</h3>
{% for fb in feedback_list %}
<div style="border:1px solid #ccc; padding:10px; margin:10px 0;">
    <strong>{{ fb.name }}</strong> ({{ fb.email }})<br>
    {{ fb.message }}
</div>
{% endfor %}
'''

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        feedback_list.append({'name': name, 'email': email, 'message': message})
    
    return render_template_string(FEEDBACK_HTML, feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True, port=5004)
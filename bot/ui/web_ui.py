"""
Simple web interface for testing the chatbot.
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ''
    if request.method == 'POST':
        user_message = request.form['message']
        # Here you would call the chatbot backend
        response = f'You said: {user_message}'
    return f"<form method='post'><input name='message'><input type='submit'></form><p>{response}</p>"

if __name__ == '__main__':
    app.run(port=5001)

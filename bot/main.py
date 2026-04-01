"""
Entry point for the chatbot server.
Run this file to start the chatbot (e.g., Flask app).
"""
from flask import Flask, request, jsonify
from .config import get_config
from .nlp_connector import NLPConnector
from .response_generator import generate_response

app = Flask(__name__)
config = get_config()
nlp = NLPConnector(config)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    nlp_result = nlp.process_message(user_message)
    response = generate_response(nlp_result)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

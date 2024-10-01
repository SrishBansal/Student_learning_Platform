from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Example API endpoint for Gemini (replace with actual API)
GEMINI_API_URL = "https://api.gemini.ai/generate"
API_KEY = "AIzaSyAvtjxz8bhsTLS6coQ4yZcNy_mntFYxVuQ"

@app.route('/api/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    subject = request.json.get('subject')

    # Prepare the request to the AI model
    headers = {'Authorization': f'Bearer {API_KEY}'}
    data = {
        "input": user_input,
        "subject": subject
    }

    # Call the Gemini API
    response = requests.post(GEMINI_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return jsonify(result), 200
    else:
        return jsonify({"error": "Error communicating with AI service"}), 500

@app.route('/api/quiz', methods=['POST'])
def quiz():
    subject = request.json.get('subject')
    
    # Here you would generate quiz questions based on the subject
    questions = generate_quiz(subject)  # This function would be implemented

    return jsonify({"questions": questions}), 200

def generate_quiz(subject):
    # Placeholder function to create quiz questions
    return [
        {"question": f"What is a key concept in {subject}?", "options": ["Option 1", "Option 2", "Option 3", "Option 4"]},
        {"question": f"Explain an important fact about {subject}.", "options": []}
    ]

if __name__ == '__main__':
    app.run(debug=True)
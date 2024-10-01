from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

GEMINI_API_URL = "https://huggingface.co/transformers"  
GEMINI_API_KEY = "AIzaSyAvtjxz8bhsTLS6coQ4yZcNy_mntFYxVuQ"                        # Replace with your actual API key

@app.route('/api/ask', methods=['POST'])
def ask_gemini():
    data = request.json
    question = data.get('question')

    # Call the Gemini API
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json={"query": question})

    if response.status_code == 200:
        answer = response.json().get('answer', 'Sorry, I could not find an answer.')
        return jsonify({"answer": answer})
    else:
        return jsonify({"answer": "Error contacting the AI service."}), 500

if __name__ == '__main__':
    app.run(debug=True)
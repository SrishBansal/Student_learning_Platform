from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

GEMINI_API_URL = "https://huggingface.co/deepset/roberta-base-squad2"
GEMINI_API_KEY = "AIzaSyAvtjxz8bhsTLS6coQ4yZcNy_mntFYxVuQ"

@app.route('/api/ask', methods=['POST'])
def ask_gemini():
    data = request.json
    question = data.get('question')

    # Validate input
    if not question:
        return jsonify({"error": "Missing question in request body."}), 400

    # Call the Gemini API
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/json'
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json={"query": question})

    if response.status_code == 200:
        # Handle empty answer from Gemini
        answer = response.json().get('answer')
        if answer:
            return jsonify({"answer": answer})
        else:
            return jsonify({"answer": "Gemini did not provide a specific answer."})
    else:
        return jsonify({"error": f"Error contacting the AI service (status code: {response.status_code})"}), 500

if __name__ == '__main__':
    app.run(debug=True)
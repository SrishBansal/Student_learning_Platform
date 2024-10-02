from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

# Use environment variable for API key
#api_key= "AIzaSyC2DpVR1QcSHwlvh_UMZdTNNx63Kt4U0CY" #commented so that there is no leak issue
genai.configure(api_key=os.environ.get("api_key")) 

# Model configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
}

# Create a Gemini-1.5-pro model instance 
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

def initialize_chat_session(student_name, student_profile):
    greeting = f"Hello {student_name}! I'm your AI learning companion. I'm here to help you with {student_profile.get('preferred_subject', 'your studies')}."
    chat_history = [
        {"parts": [{"text": "You are an AI learning companion."}]},
        {"parts": [{"text": greeting}]},
    ]
    chat_session = model.start_chat(history=chat_history)
    return chat_session

def send_message(chat_session, user_input):
    try:
        message = {"parts": [{"text": user_input}]}
        response = chat_session.send_message(message)
        model_response = response.text if response else "Sorry, I didn't understand that."
        return model_response
    except Exception as e:
        print(f"Error: {e}")
        return "I encountered an error. Please try again later."

app = Flask(__name__)
chat_sessions = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("user_input")
    student_name = data.get("student_name")
    student_profile = data.get("student_profile", {})

    if not user_input:
        return jsonify({"error": "Missing user input"}), 400

    if student_name not in chat_sessions:
        chat_sessions[student_name] = initialize_chat_session(
            student_name, student_profile
        )

    chat_session = chat_sessions[student_name]
    response = send_message(chat_session, user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True) 
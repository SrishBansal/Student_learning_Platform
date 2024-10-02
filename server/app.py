import os
import google.generativeai as genai

# Use environment variable for API key
api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key="AIzaSyC2DpVR1QcSHwlvh_UMZdTNNx63Kt4U0CY")

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

# Function to initialize a chat session with a personalized greeting
def initialize_chat_session(student_name, student_profile):
    greeting = f"Hello {student_name}! I'm your AI learning companion. I'm here to help you with {student_profile['preferred_subject']}."
    chat_session = model.start_chat(history=[{"content": greeting}])
    return chat_session

# Function to send a personalized message and handle errors
def send_personalized_message(chat_session, user_input):
    try:
        response = chat_session.send_message(user_input)
        model_response = response.text if response else "Sorry, I didn't understand that."
        print(f"{student_name}: {user_input}") # type: ignore
        print(f"AI: {model_response}")
        return model_response
    except Exception as e:
        print(f"Error: {e}")
        return "I encountered an error. Please try again later."

# Main function to interact with the AI learning companion
def main():
    student_name = input("Enter your name: ")
    student_profile = {
        'age': int(input("Enter your age: ")),
        'preferred_subject': input("Enter your preferred subject: "),
        'learning_style': input("Enter your learning style (visual, auditory, kinesthetic): ")
    }

    chat_session = initialize_chat_session(student_name, student_profile)

    while True:
        user_input = input("Enter your message: ")
        if user_input.lower() == "quit":
            break
        model_response = send_personalized_message(chat_session, user_input)

if __name__ == "__main__":
    main()
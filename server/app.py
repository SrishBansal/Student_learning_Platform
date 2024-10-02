import requests

# Set your API endpoint and key
API_ENDPOINT = "https://api.gemini.ai/v1/chat/completions"
API_KEY = "AIzaSyAM6aieQA9pJANS_cLtkrIhTZGc4oyGphE"  
def get_answer(question, context):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # Create the payload for the API request
    payload = {
        "model": "gemini",  # Specify the model to use
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": context}  # Provide context if needed
        ],
        "max_tokens": 150,  # Adjust based on your needs
        "temperature": 0.7,  # Adjust creativity of responses
    }

    # Send the request to the Gemini API
    response = requests.post(API_ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        answer = response_data['choices'][0]['message']['content']
        return answer
    else:
        return f"Error: {response.status_code}, {response.text}"

# User interaction function
def learning_companion():
    print("Welcome to your AI Learning Companion! Type 'exit' to quit.")
    context = "The capital of France is Paris. It is known for its art, fashion, and culture."
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get an answer from the Gemini API
        answer = get_answer(user_input, context)
        print(f"AI: {answer}")

# Start the learning companion
learning_companion()

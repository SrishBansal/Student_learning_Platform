import requests
import os

# Set API endpoint and key as environment variables
API_ENDPOINT = os.environ['OPENAI_API_ENDPOINT']
API_KEY = os.environ['OPENAI_API_KEY']

def get_answer(question, context):
    """
    Send a request to the OpenAI API to get an answer to a question.

    Args:
    - question (str): The user's question.
    - context (str): The context for the question.

    Returns:
    - str: The answer to the question.
    """
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": context}
        ],
        "max_tokens": 150,
        "temperature": 0.7,
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        answer = response_data['choices'][0]['message']['content']
        return answer
    else:
        return f"Error: {response.status_code}, {response.text}"

def learning_companion():
    """
    The main function for the AI Learning Companion.
    """
    print("Welcome to your AI Learning Companion! Type 'exit' to quit.")
    context = "The capital of France is Paris. It is known for its art, fashion, and culture."

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        answer = get_answer(user_input, context)
        print(f"AI: {answer}")

if __name__ == "__main__":
    learning_companion()
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and project ID from environment variables
api_key = os.getenv('WATSONX_API_KEY')
project_id = os.getenv('WATSONX_PROJECT_ID')

def get_iam_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"Error getting IAM token: {response.status_code}")
        print(response.text)
        return None

def get_watsonx_response(prompt, iam_token):
    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    headers = {
        "Authorization": f"Bearer {iam_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    system_message = "You are a helpful AI assistant. Provide clear, concise, and accurate responses to the user's questions or requests. Do not generate additional user input or questions."
    full_prompt = f"{system_message}\n\nUser: {prompt}\n\nAssistant:"
    
    data = {
        "model_id": "ibm/granite-13b-chat-v2",
        "input": full_prompt,
        "parameters": {
            "temperature": 0.7,
            "max_tokens": 250,
        },
        "project_id": project_id
    }

    print("Outgoing API request:")
    print(json.dumps(data, indent=2))

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        print("\nIncoming API response:")
        print(json.dumps(response.json(), indent=2))
        
        generated_text = response.json()["results"][0]["generated_text"].strip()
        # Remove any additional "User:" prompts from the generated text
        if "\nUser:" in generated_text:
            generated_text = generated_text.split("\nUser:")[0]
        return generated_text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        if hasattr(e, 'response'):
            print(f"Status code: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        return None

def main():
    print("Welcome to AI Hackers Watsonx Test")
    
    iam_token = get_iam_token(api_key)
    if not iam_token:
        print("Failed to obtain IAM token. Exiting.")
        return

    print("AI Assistant is ready. Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please enter a question or request.")
            continue
        
        print("AI is thinking...")
        ai_response = get_watsonx_response(user_input, iam_token)
        
        if ai_response:
            print(f"\nAI Assistant: {ai_response}")
        else:
            print("Failed to get a response from the AI.")

if __name__ == "__main__":
    main()
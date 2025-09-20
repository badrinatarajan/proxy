import openai # openai v1.0.0+
import typing
from typing import Any

client = openai.OpenAI(api_key="anything",base_url="http://0.0.0.0:4000") # set proxy to base_url

def proxy_response(model: str, user_message:str)->Any:
    response = client.chat.completions.create(
        model=model, # model name set on litellm proxy, `litellm --model openai-gpt-4`
        messages=[{"role": "user", "content": user_message}]
    )
    return response


def main():
    user_message = "Explain the theory of Gravity in one Sentence"
    #Get user input to fetch from GPT4 or Mistral
    #user_message = input("Enter your message to be passed to LLM: ")
    model_choice = input("Enter model choice (gpt4/mistral): ").strip().lower()
    try:
        if model_choice == "mistral":
            model = "mistral-large-latest"
            
        elif model_choice == "gpt4":
            model = "openai-gpt-4o"
        else:
            raise ValueError("Invalid model choice. Please enter 'gpt4' or 'mistral'.")
           
        response = proxy_response(model, user_message)
        print(f'Response from {model}:')
        print(f'Response object: {response}')

        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
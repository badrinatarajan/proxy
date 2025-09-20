import os
from litellm import completion

# Make sure OPENAI_API_KEY is set in your environment
# Example: export OPENAI_API_KEY=your_actual_key
openai_api_key = os.getenv("OPENAI_APIKEY")
mistral_api_key = os.getenv("MISTRAL_APIKEY")

def fetch_gpt4_response(api_key:str, user_message:str)->dict:
    if not api_key:
        raise ValueError("API key is not set. Please set the OPENAI_APIKEY environment variable.")  
    response = completion(
        model="openai/gpt-4o",
        messages=[{"role": "user", "content": user_message}],
        api_key=api_key
    )
    return response

#print(response['choices'][0]['message']['content']) 
def fetch_mistral_response(api_key:str, user_message:str)->dict:
    if not api_key:
        raise ValueError("API key is not set. Please set the OPENAI_APIKEY environment variable.")  
    response = completion(
        model="mistral/mistral-large-latest",
        messages=[{"role": "user", "content": user_message}],
        api_key=api_key
    )
    return response

def main():
    user_message = "Explain the theory of Relativity in one sentence"
    #Get user input to fetch from GPT4 or Mistral
    user_message = input("Enter your message to be passed to LLM: ")
    model_choice = input("Enter model choice (gpt4/mistral): ").strip().lower()
    try:
        if model_choice == "mistral":
            response = fetch_mistral_response(mistral_api_key, user_message)
            print("Response from Mistral:")
            print(response['choices'][0]['message']['content'])
        else:
            response = fetch_gpt4_response(openai_api_key, user_message)
            print("Response from GPT-4:")
            print(response['choices'][0]['message']['content'])
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()
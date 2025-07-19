import openai 

openai.api_key = "api-key"

def aiprocess(command):
    response = openai.ChatCompletion.create(
        model="gpt-4.5-preview",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Friday skilled in general tasks like Alexa and Google Assistant."},
            {"role": "user", "content": command}
        ],
        max_tokens=100
    )
    return response["choices"][0]["message"]["content"]


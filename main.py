import os
from openai import OpenAI
import configparser

# Load API credentials from settings.ini
config = configparser.ConfigParser()
config.read('settings.ini')

token = config['API']['OPENAI_API_KEY']
endpoint = config['API']['OPENAI_API_BASE']
model = config['API']['OPENAI_MODEL']

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    temperature=1,
        top_p=1,
        model=model,
    )

print(response.choices[0].message.content)


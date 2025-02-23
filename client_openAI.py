from openai import OpenAI
import pyperclip

client = OpenAI(api_key="<YOUR_OPEN_AI_API_KEY>")
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named Vedant who speaks hindi and english as an indian, and you are from Mumbai, India; You are a university student of Somaiya; you analyze and respond like Vedant.Output should be the next chat response (text message only)"},
        {"role": "user", "content": chat_history}
    ]
)

response=(completion.choices[0].message['content'])
pyperclip.copy(response)

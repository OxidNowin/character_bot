import openai

from config import OPENAI_KEY


async def get_response(person, msg):
    prompt = (f'Instructions: You are {person}. Need to reply to user message\n'
              f'User message: {msg}\n')
    openai.api_key = OPENAI_KEY
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_msg = response.choices[0].text.strip()
    return response_msg

from data import config
from textgen.message import Message
import openai


async def generate_reply(message: str):
    openai.api_key = config.next_token()
    mess = Message(message)
    if mess.has_errors:
        return mess.error_message
    completion = openai.Completion.create(model=mess.model, prompt=mess.prompt,
                                          temperature=mess.temperature,
                                          max_tokens=mess.max_tokens, top_p=mess.top_p,
                                          frequency_penalty=mess.frequency_penalty,
                                          presence_penalty=mess.presence_penalty)
    return completion.choices[0].text

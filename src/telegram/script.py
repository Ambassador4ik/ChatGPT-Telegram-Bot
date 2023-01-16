from pyrogram import Client
from pyrogram import filters
from data import config
import openai


# TODO: Save variables to config
app = Client("my_account", config.telegram_app_id, config.telegram_app_hash)
api_key = config.openai_token

@app.on_message(filters.regex("^(?!!).+") & ~filters.me)
async def say_wise(client, message):
    global api_key
    openai.api_key = api_key
    mes = message.text
    completion = openai.Completion.create(model="text-davinci-003",
                                          prompt=mes,
                                          temperature=0.5,
                                          max_tokens=1000,
                                          top_p=1.0,
                                          frequency_penalty=0.5,
                                          presence_penalty=0.0)
    await app.send_message(message.chat.id, completion.choices[0].text, reply_to_message_id=message.id)

app.run()

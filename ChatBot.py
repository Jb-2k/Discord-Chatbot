import discord
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import requests
import json
import random

MODEL_NAME = ""
client = discord.Client()

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)


def generate_response(model, tokenizer, message):

    new_user_input_ids = tokenizer.encode(message + tokenizer.eos_token,
                                          return_tensors='pt')

    chat_history_ids = model.generate(
        new_user_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=0.8,
    )

    return tokenizer.decode(chat_history_ids[:,
                                             new_user_input_ids.shape[-1]:][0],
                            skip_special_tokens=True)


@client.event
async def on_ready():

    print("Bot is online")


@client.event
async def on_message(message):
    print(message.content)

    if message.author == client.user:
        return
    else:

        reply = handleMessage(message)
        await message.reply(reply)


def handleMessage(message):
    
    input = message.content
    reply = generate_response(model, tokenizer, input)
    print(reply)
    return reply


client.run(
    os.getenv("DISCORD_BOT_TOKEN"))

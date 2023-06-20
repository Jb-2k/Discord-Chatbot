# Discord-Chatbot
Instructions for creating a discord chatbot that will mimic the responses of the user you train it on

This code uses Microsoft's pretrained [Dialo-GPT-small](https://www.microsoft.com/en-us/research/project/large-scale-pretraining-for-response-generation/) model.


## Step one: Acquiring the data
The first thing to do is download the source data from the discord channel containing messages you want to use. For this I recommend using [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter) . Just click on the channel you want and download as a JSON. The more messages you have to work with, the better the bot will perform.

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/fe23b0bb-3dfe-4621-a9e1-f97e6bd5c86e)

## Step two: Extracting the data
Now that we have our raw data, we need to transform it into a format we can feed to the model. DialoGpt must be fed each message as well as the seven previous messages for context. This is what [DiscordChatBotExtractData.ipynb]() will do for us.
Before this however, we must first discover the ID of the specific user we want our bot to mimic. See [this guide](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) published by discord support on how to acquire that. 

Once you have this ID, paste the value into the USER_ID field at the top of [DiscordChatBotExtractData.ipynb](), along with the path to the raw channel data JSON file from the previous step, and a path where you want to output the training file.

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/0d49d1b9-dbde-402b-aa8f-f44a84f28a64)


Then run the notebook. Once it is finished, you should see a csv file at the path you specified in OUTPUT_PATH. This is the file we will use for model training

## Step three: Training the model and uploading to HuggingFace🤗
Now we are ready to train our model. Open [DiscordChatBotTraining.ipynb]() and set DATA_PATH to the csv file produced by the last step and run the notebook. 

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/8e29659f-ae94-46a4-aaf3-bc791789f7f3)

Training on a GPU will be much faster, using the free tier of GPUs available on google collab training will take less than an hour, depending on how much data you have.

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/1dc62539-e5e0-4fa6-8873-4c2811855042)

After we have trained our model, we want to upload it to huggingface🤗, you will have to login to huggingface using the cli. Change model_name to anything you like, this will be what the model is called on huggingface 

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/9a627132-a373-4e0b-a056-85c393097301)



## Step four: Creating a discord bot account
Now we have a trained model we need to create a discord bot account to send and recieve messages. Follow the steps in [this tutorial](https://discordpy.readthedocs.io/en/stable/discord.html) to create your bot, taking note of the generated token, we will need this for the final step
![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/1ac7b2cb-4d73-4712-86b3-c0b0a04f17a1)

## Step five: Deploying the model
Finally we are ready to deploy the model. Create a new project on [replit](https://replit.com/~)

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/6b6ee5d3-0f43-41ed-b139-a0af40085b06)

Upload [ChatBot.py]() to it. Change MODEL_NAME to the name of the model we uploaded to huggingface.

Next, create a new [secret](https://docs.replit.com/programming-ide/workspace-features/secrets) called DISCORD_BOT_TOKEN and set the value as the token generated in the previous step. This is very important as anyone with access to this unique token will have control of your bot, so you want to keep it seperate from your .py file, which will be publicly accessible.

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/d0a31e9c-1e7a-49b7-a225-3c722d2f69c8)


After this, you should be able to run the replit project and start chatting to your model in discord!

**Note on costs**: Because of the computational requirements of the model, you will have to purchase boosts for your replit project. The lowest tier boost is enough to run the small dialogpt model, this costs 20 replit cycles a day, about 20 US cents. You can also pay a further 20 cycles a day to have your project always on, so the bot will be active 24/7


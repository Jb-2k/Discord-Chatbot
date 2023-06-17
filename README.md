# Discord-Chatbot
Code and instructions for creating your own chatbot trained on data from discord conversations and deploying it as a discord chatbot using [replt](https://replit.com/~) . This code uses Microsoft's pretrained [Dialo-GPT-small](https://www.microsoft.com/en-us/research/project/large-scale-pretraining-for-response-generation/) model.

## Step one: Acquiring the data
The first thing to do is download the source data from the discord channel containing messages you want to use. For this I recommend using the easy to use open source [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter) . Just click on the channel you want and download as a JSON. The more messages you have to work with, the better the bot will perform.

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/fe23b0bb-3dfe-4621-a9e1-f97e6bd5c86e)

## Step two: Extracting the data
Now that we have our raw data, we need to transform it into a format we can feed to the model. DialoGpt must be fed each message as well as the seven previous messages for context. This is what [DiscordChatBotExtractData.ipynb]() will do for us.
Before this however, we must first discover the ID of the specific user we want our bot to mimic. See [this guide](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) published by discord support on how to acquire that. 

Once you have this ID, paste the value into the USER_ID field at the top of [DiscordChatBotExtractData.ipynb](), along with the path to the raw channel data JSON, and a path where you want to output the training file.

![image](https://github.com/Jb-2k/Discord-Chatbot/assets/91644188/edf30d28-0279-450c-9a8f-5615ceb7fe9c)

Then run the notebook. Once it is finished, you should see a csv file at the path you specified in OUTPUT_PATH. This is the file we will use for model training

## Step three: Training the model and uploading to HuggingFace🤗
Now we are ready to train our model. Open [DiscordChatBotTraining.ipynb]() and set DATA_PATH to the csv file produced by the last step and run the notebook. Training on a GPU will be much faster, using the free tier of GPUs available on google collab training will take less than an hour, depending on how much data you have.
After we have trained our model, we want to upload it to huggingface🤗


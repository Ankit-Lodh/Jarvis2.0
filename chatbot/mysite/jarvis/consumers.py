from channels.generic.websocket import AsyncWebsocketConsumer
import json
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
class botConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("connect")
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self,close_code):
        print("disconnect")
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    

    async def receive(self, text_data):

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':text_data,
            }
        )

        print ('>>>>',text_data)

        # pass

    async def deprocessing(self,event):
        print("---------------------------------------------------")
        print(event)
        print("----------------------------------------------")
        valOther=event['value']
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(valOther + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
        bot_input_ids = new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # pretty print last ouput tokens from bot
        text = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        await self.send(text)
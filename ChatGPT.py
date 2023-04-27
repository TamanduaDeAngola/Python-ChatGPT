import openai
from os import system

class ChatGPT:
    def __init__(self, **kwargs):
        openai.organization=kwargs['orgcode']
        openai.api_key=kwargs['api_key']
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = [
                {"role": "user", "content" : kwargs["question"]}
            ]
        )
        print("\n\x1b[36mChatGPT> "+response["choices"][0]["message"]["content"])

while 1:
    question = input("\n\x1b[94mYou> ")
    if question=="!clear": 
        system("clear")
        continue
    
    ChatGPT(orgcode='org-8jvFAZpnYV5WiDH2gwQAVNAf', api_key='[your api key here]', model="gpt-3.5-turbo", question=question)
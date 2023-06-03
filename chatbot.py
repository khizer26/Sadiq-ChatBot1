API_KEY= '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'
import openai
import os

os.environ['OPENAI_Key']=API_KEY
openai.api_key=os.environ['OPENAI_Key']

loop=True   
   
while loop:  #keeps running until 'exit' is typed
    prompt=input("AI:Hello. If you dont have any more questions, type exit.\n You:")
    
    if prompt=='exit':
        loop=False
    else:
        response=openai.Completion.create(engine='text-davinci-003',prompt=prompt,max_tokens=200)
        print(response['choices'][0]['text'])
        
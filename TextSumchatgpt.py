#This code is a simple chatbot that uses the OpenAI GPT-3.5 model to generate responses to user input.
#The chatbot maintains a conversation history in the form of a list of messages, with each message containing the role (system, user, or assistant) and the content of the message.
#The user can input messages, which are added to the conversation history. The chatbot then uses the conversation history to generate a response using the GPT-3.5 model.
#The generated response is added to the conversation history, and the chatbot continues the conversation by prompting the user for another input.
#The conversation continues in this manner until the user exits the chatbot by not providing any input.
import datetime
import openai

openai.api_key = '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'

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    message = input("User: ")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})    
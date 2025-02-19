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
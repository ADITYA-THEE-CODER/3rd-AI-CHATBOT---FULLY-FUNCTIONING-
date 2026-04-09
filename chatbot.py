import os 
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

chat_history = []

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    # 1. Add user message
    chat_history.append({"role": "user", "content": user_input})

    # 2. Send full history
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages = chat_history
    )

    # 3. Extract reply
    bot_reply = response.choices[0].message.content

    # 4. Print reply
    print("Chatbot:", bot_reply)

    # 5. Add bot reply to history
    chat_history.append({"role": "assistant", "content": bot_reply})

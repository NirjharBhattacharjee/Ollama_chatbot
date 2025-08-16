from ollama import chat

def main():
    conversation = [
        {"role": "system", "content": "You are a helpful assistant called Nirubot. Be concise and clear."}
    ]
    model = "nirubot:dev"

    print("Starting Nirubot. Type 'quit' to exit.")
    while True:
        user = input("You: ").strip()
        if user.lower() == "quit":
            break
        conversation.append({"role": "user", "content": user})
        resp = chat(model=model, messages=conversation)
        assistant = resp["message"]["content"]
        print("Bot:", assistant)
        conversation.append({"role": "assistant", "content": assistant})

if __name__ == "__main__":
    main()

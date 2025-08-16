from ollama import chat

def main():
    conversation = [
        {"role": "system", "content": "You are a helpful assistant called Nirubot. Be concise and clear."}
    ]
    model = "llama2"

    print("Starting Nirubot. Type 'quit' to exit.")
    while True:
        user = input("You: ").strip()
        if user.lower() == "quit":
            break
        if not user:
            continue

        conversation.append({"role": "user", "content": user})
        resp = chat(model=model, messages=conversation)
        assistant = resp["message"]["content"]   # note: 'message', not 'messages'
        print("Bot:", assistant)
        conversation.append({"role": "assistant", "content": assistant})

if __name__ == "__main__":
    main()

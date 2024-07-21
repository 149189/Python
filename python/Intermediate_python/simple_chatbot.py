#Create a simple rule-based chatbot that can respond to basic user inputs.
def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ").strip().lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

if __name__ == "__main__":
    chatbot()

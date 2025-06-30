def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        
        # Asking about well-being
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        
        # Asking for the chatbot's name
        elif "your name" in user_input:
            print("Chatbot: I'm just a simple rule-based chatbot!")

        # Weather response
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather now, but I hope it's sunny!")

        # Time-related question
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}.")

        # Help response
        elif "help" in user_input:
            print("Chatbot: You can ask me about time, greetings, or just have a casual chat!")

        # Unknown input
        else:
            print("Chatbot: I'm not sure I understand. Can you try asking something else?")

# Run the chatbot
chatbot()

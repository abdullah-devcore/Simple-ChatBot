# Function for chatbot replies
def chatbot_reply(user_input):

    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    
    elif user_input == "bye":
        return "Goodbye!"
    
    elif user_input == "name":
        return "I am a basic chatbot."
    
    else:
        return "Sorry, I don't understand."


# Main chatbot loop
print("Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    
    user = input("You: ").lower()

    response = chatbot_reply(user)
    print("Bot:", response)

    if user == "bye":
        break
import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I help you today?", "Hi there! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot created using nltk!", "My name is ChatBot, what's yours?"]
    ],
    [
        r"how are you?",
        ["I'm just a bunch of code, but I'm doing great! How about you?", "I'm fine, thank you! How can I assist you?"]
    ],
    [
        r"what can you do?",
        ["I can answer simple questions! Try asking me something.", "I'm here to answer your questions!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem, happy to help!"]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "Goodbye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you please ask something else?"]
    ]
]

# Create the chatbot with nltk's Chat class
chatbot = Chat(pairs, reflections)

# Start the chatbot
def chatbot_start():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye! Have a great day.")
            break
        else:
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_start()

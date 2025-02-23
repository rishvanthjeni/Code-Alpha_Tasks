import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I help you?"]],
    [r"how are you", ["I'm just a bot, but I'm doing great! How about you?", "I'm good! What about you?"]],
    [r"(.*) your name", ["I'm a chatbot created to assist you.", "I go by ChatBot. What's your name?"]],
    [r"my name is (.*)", ["Nice to meet you, %1!"]],
    [r"what can you do", ["I can chat with you, answer basic questions, and keep you company!"]],
    [r"quit|bye|exit", ["Goodbye! Have a great day!", "Bye! Talk to you later."]],
    [r"(.*)", ["I'm not sure how to respond to that.", "Can you rephrase that?"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
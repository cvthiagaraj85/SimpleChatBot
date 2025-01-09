import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello! How can I help you?"],
        "how are you": ["I'm a chatbot, so I don't have feelings, but thanks for asking!"],
        "bye": ["Goodbye! Have a great day!", "Bye! Take care!"],
        "default": ["I'm not sure I understand. Could you rephrase?"]
    }

    # Simple logic to handle user input
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return random.choice(responses["default"])

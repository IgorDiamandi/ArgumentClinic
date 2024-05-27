# argument_clinic/conversation_manager.py
import random
import re
import json

class ConversationManager:
    def __init__(self, response_file='data/responses.json'):
        with open(response_file, 'r') as file:
            self.responses = json.load(file)
        self.rules = [
            (re.compile(rule['pattern']), rule['responses'])
            for category in self.responses
            if category != "default"
            for rule in self.responses[category]
        ]
        self.default_responses = self.responses["default"]

    def get_response(self, user_input):
        for pattern, responses in self.rules:
            if pattern.search(user_input):
                return random.choice(responses)
        return random.choice(self.default_responses)

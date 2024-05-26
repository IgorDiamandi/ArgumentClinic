import json
import re


class RulesManager:
    def __init__(self, rules_file='rules_manager/rules.json'):
        self.default_response = None
        self.rules = None
        self.rules_file = rules_file
        self.load_rules()

    def load_rules(self):
        with open(self.rules_file, 'r') as file:
            data = json.load(file)
            self.default_response = data.get('default', "No it isn't!")
            self.rules = [(re.compile(rule['pattern'], re.IGNORECASE), rule['response']) for rule in
                          data.get('rules', [])]

    def get_response(self, user_input):
        for pattern, response in self.rules:
            if pattern.search(user_input):
                return response
        return self.default_response

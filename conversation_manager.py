class ConversationManager:
    def __init__(self, rules_manager):
        self.rules_manager = rules_manager

    def get_response(self, user_input):
        return self.rules_manager.get_response(user_input)

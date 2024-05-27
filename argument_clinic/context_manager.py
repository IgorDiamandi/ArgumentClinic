# argument_clinic/context_manager.py
class ContextManager:
    def __init__(self):
        self.contexts = {}

    def get_context(self, user_id):
        return self.contexts.get(user_id, {})

    def update_context(self, user_id, user_input, response):
        self.contexts[user_id] = {
            'last_input': user_input,
            'last_response': response
        }

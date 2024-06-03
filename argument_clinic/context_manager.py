import threading
import time
import random


class ContextManager:
    def __init__(self):
        self.contexts = {}
        self.timers = {}

    def get_context(self, user_id):
        return self.contexts.get(user_id, {})

    def update_context(self, user_id, user_input, response):
        self.contexts[user_id] = {
            'last_input': user_input,
            'last_response': response,
            'paid': True,
        }

    def reset_timer(self, user_id, callback):
        if user_id in self.timers:
            self.timers[user_id].cancel()
        delay = random.randint(20, 30)
        timer = threading.Timer(delay, callback, args=[user_id])
        self.timers[user_id] = timer
        timer.start()

    def set_paid_status(self, user_id, status):
        if user_id in self.contexts:
            self.contexts[user_id]['paid'] = status

    def get_paid_status(self, user_id):
        return self.contexts.get(user_id, {}).get('paid', True)

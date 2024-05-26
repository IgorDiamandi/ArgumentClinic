import threading
import random


class SessionTimer:
    clients = {}

    def __init__(self, user_id):
        self.user_id = user_id
        self.timer = None
        self.status = 'paid'  # possible values: 'paid', 'unpaid', 'notified'
        self.message = None
        SessionTimer.clients[user_id] = self

    def notify_prolongation(self):
        self.status = 'unpaid'
        self.message = """Sorry. The five minutes is up, 
        I’m not allowed to argue anymore. 
        If you want me to go on arguing, 
        you’ll have to pay for another five minutes."""
        self.status = 'notified'

    def start_timer(self):
        if self.status == 'paid':
            delay = random.randint(20, 30)
            self.timer = threading.Timer(delay, self.notify_prolongation)
            self.timer.start()

    def reset(self):
        if self.timer:
            self.timer.cancel()
        self.status = 'paid'
        self.message = None
        self.start_timer()

    @classmethod
    def add_client(cls, user_id):
        cls.clients[user_id] = SessionTimer(user_id)
        cls.clients[user_id].start_timer()

    @classmethod
    def get_client_status(cls, user_id):
        client = cls.clients.get(user_id)
        if client:
            return {'paid': client.status == 'paid', 'message': client.message}
        else:
            return {'paid': True, 'message': None}

    @classmethod
    def reset_client_status(cls, user_id):
        client = cls.clients.get(user_id)
        if client:
            client.reset()

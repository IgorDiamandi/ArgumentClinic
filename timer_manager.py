import threading
import random

clients = {}


def notify_prolongation(user_id):
    clients[user_id]['paid'] = False
    clients[user_id]['message'] = """Sorry. The five minutes is up, 
    I’m not allowed to argue anymore. 
    If you want me to go on arguing, 
    you’ll have to pay for another five minutes."""


def start_prolongation_timer(user_id):
    delay = random.randint(20, 30)
    timer = threading.Timer(delay, notify_prolongation, args=[user_id])
    timer.start()
    clients[user_id]['timer'] = timer


def add_client(user_id):
    clients[user_id] = {'paid': True, 'message': None, 'timer': None}
    start_prolongation_timer(user_id)


def get_client_status(user_id):
    return clients.get(user_id, {'paid': True, 'message': None})


def reset_client_status(user_id):
    if user_id in clients and clients[user_id]['timer']:
        clients[user_id]['timer'].cancel()
    clients[user_id]['paid'] = True
    clients[user_id]['message'] = None
    start_prolongation_timer(user_id)

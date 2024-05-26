from apscheduler.schedulers.background import BackgroundScheduler
import random

scheduler = BackgroundScheduler()
scheduler.start()

clients = {}

def notify_prolongation(user_id):
    clients[user_id]['paid'] = False
    clients[user_id]['message'] = "Sorry. The five minutes is up, I’m not allowed to argue anymore. If you want me to go on arguing, you’ll have to pay for another five minutes."

def start_prolongation_timer(user_id):
    delay = random.randint(20, 30)
    job_id = f"prolongation_{user_id}"
    scheduler.add_job(notify_prolongation, 'interval', seconds=delay, id=job_id, replace_existing=True, args=[user_id])

def add_client(user_id):
    clients[user_id] = {'paid': True, 'message': None}
    start_prolongation_timer(user_id)

def get_client_status(user_id):
    return clients.get(user_id, {'paid': True, 'message': None})

def reset_client_status(user_id):
    clients[user_id]['paid'] = True
    clients[user_id]['message'] = None
    start_prolongation_timer(user_id)

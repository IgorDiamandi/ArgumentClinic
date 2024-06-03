class UserProfileManager:
    def __init__(self):
        self.profiles = {}

    def get_user_profile(self, user_id):
        if user_id not in self.profiles:
            self.profiles[user_id] = {
                'paid': True
            }
        return self.profiles[user_id]

    def reset_payment_status(self, user_id):
        if user_id in self.profiles:
            self.profiles[user_id]['paid'] = True

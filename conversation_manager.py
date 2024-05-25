class ConversationManager:
    def __init__(self, rules_manager):
        self.rules_manager = rules_manager

    def get_response(self, user_input):
        return self.rules_manager.get_response(user_input)


    def start_conversation(self):
        print("Welcome to the Argument Clinic! Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower().strip() == "exit":
                print("Conversation ended.")
                break
            response = self.rules_manager.get_response(user_input)
            print(f"Argument Clinic: {response}")
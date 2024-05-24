from rules_manager import RulehisManager
from conversation_manager import ConversationManager

def main():
    rules_manager = RulesManager()
    conversation_manager = ConversationManager(rules_manager)
    conversation_manager.start_conversation()

if __name__ == "__main__":
    main()

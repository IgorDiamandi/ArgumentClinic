from flask import Flask, request, jsonify, render_template
from rules_manager.rules_manager import RulesManager
from conversation_manager import ConversationManager

app = Flask(__name__)
rules_manager = RulesManager()
conversation_manager = ConversationManager(rules_manager)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    response = conversation_manager.get_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)

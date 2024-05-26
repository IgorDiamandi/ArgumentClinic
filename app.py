from flask import Flask, render_template, request, jsonify
from timer_manager import add_client, get_client_status, reset_client_status
from conversation_manager import ConversationManager
from rules_manager.rules_manager import RulesManager

app = Flask(__name__)

# Initialize the RulesManager and ConversationManager
rules_manager = RulesManager()
conversation_manager = ConversationManager(rules_manager)

@app.route('/')
def index():
    user_id = request.remote_addr  # Use IP address as a simple user identifier
    add_client(user_id)
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_id = request.remote_addr
    user_input = request.json.get('user_input')
    client_status = get_client_status(user_id)
    if client_status['paid']:
        response = conversation_manager.get_response(user_input)  # Use user_input to get the response
    else:
        response = "I'm very sorry, but I told you I'm not allowed to argue unless you've paid."
    return jsonify({'response': response})

@app.route('/check_status', methods=['GET'])
def check_status():
    user_id = request.remote_addr
    client_status = get_client_status(user_id)
    return jsonify({'message': client_status['message'], 'paid': client_status['paid']})

@app.route('/pay', methods=['POST'])
def pay():
    user_id = request.remote_addr
    reset_client_status(user_id)
    return jsonify({'message': "Here you are, go on then!"})

if __name__ == "__main__":
    app.run(debug=True)

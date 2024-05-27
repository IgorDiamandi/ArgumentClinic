# app.py
from flask import Flask, render_template, request, jsonify
from argument_clinic.conversation_manager import ConversationManager
from argument_clinic.context_manager import ContextManager
from argument_clinic.user_profile import UserProfileManager

app = Flask(__name__)

# Initialize the managers
conversation_manager = ConversationManager()
context_manager = ContextManager()
user_profile_manager = UserProfileManager()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_id = request.remote_addr
    user_input = request.json.get('user_input')
    response = conversation_manager.get_response(user_input)
    context_manager.update_context(user_id, user_input, response)

    return jsonify({'response': response})


@app.route('/pay', methods=['POST'])
def pay():
    user_id = request.remote_addr
    user_profile_manager.reset_payment_status(user_id)
    return jsonify({'message': "Here you are, go on then!"})


if __name__ == "__main__":
    app.run(debug=True)

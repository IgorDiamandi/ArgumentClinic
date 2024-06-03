from flask import Flask, render_template, request, jsonify
from argument_clinic.conversation_manager import ConversationManager
from argument_clinic.context_manager import ContextManager
from argument_clinic.user_profile import UserProfileManager

app = Flask(__name__)

conversation_manager = ConversationManager()
context_manager = ContextManager()
user_profile_manager = UserProfileManager()


def interrupt_argument(user_id):
    context_manager.set_paid_status(user_id, False)
    context_manager.update_context(user_id, '',
                                   "Time's up, you'll have to pay 5 pounds for an additional 5 minutes of argument")


@app.route('/')
def index():
    user_id = request.remote_addr
    context_manager.reset_timer(user_id, interrupt_argument)
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_id = request.remote_addr
    user_input = request.json.get('user_input')

    if not context_manager.get_paid_status(user_id):
        response = "No argument till you're paying"
    else:
        context = context_manager.get_context(user_id)
        response = conversation_manager.get_response(user_input, context)
        context_manager.update_context(user_id, user_input, response)
        context_manager.reset_timer(user_id, interrupt_argument)

    return jsonify({'response': response})


@app.route('/pay', methods=['POST'])
def pay():
    user_id = request.remote_addr
    context_manager.set_paid_status(user_id, True)
    context_manager.reset_timer(user_id, interrupt_argument)
    return jsonify({'message': "Here you are, go on then!"})


if __name__ == "__main__":
    app.run(debug=True)

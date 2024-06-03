// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const prolongButton = document.getElementById('prolong-button');

    function appendMessage(actor, message, className) {
        const messageElement = document.createElement('div');
        messageElement.className = `chat-message ${className}`;

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = message;

        messageElement.appendChild(messageContent);
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMessage() {
        const userMessage = userInput.value;
        if (userMessage.trim() === '') return;

        appendMessage('User', userMessage, 'user-message');
        userInput.value = '';

        const response = await fetch('/get_response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: userMessage })
        });
        const data = await response.json();
        appendMessage('Clinic', data.response, 'clinic-message');

        if (data.response === "No argument till you're paying") {
            prolongButton.style.display = 'block';
        }
    }

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    sendButton.addEventListener('click', sendMessage);

    prolongButton.addEventListener('click', async () => {
        const response = await fetch('/pay', {
            method: 'POST'
        });
        const data = await response.json();
        appendMessage('Clinic', data.message, 'clinic-message');
        prolongButton.style.display = 'none';
    });
});

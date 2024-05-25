document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const rulesList = document.getElementById('rules-list');

    // Function to append messages to chat
    function appendMessage(actor, message, className) {
        const messageElement = document.createElement('div');
        messageElement.className = `chat-message ${className}`;

        const actorLabel = document.createElement('div');
        actorLabel.className = 'chat-actor';
        actorLabel.textContent = actor;

        const messageContent = document.createElement('div');
        messageContent.textContent = message;

        messageElement.appendChild(actorLabel);
        messageElement.appendChild(messageContent);

        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Function to send messages
    async function sendMessage() {
        const userMessage = userInput.value;
        if (userMessage.trim() === '') return;

        appendMessage('Customer', userMessage, 'user-message');
        userInput.value = '';

        const response = await fetch('/get_response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: userMessage })
        });
        const data = await response.json();
        appendMessage('MR. BARNARD', data.response, 'bot-message');
    }

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Function to load rules
    async function loadRules() {
        const response = await fetch('/static/rules.json');
        const data = await response.json();
        data.rules.forEach(rule => {
            const listItem = document.createElement('li');
            listItem.textContent = `${rule.pattern}: ${rule.response}`;
            rulesList.appendChild(listItem);
        });
    }

    // Load rules on page load
    loadRules();
});

document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const rulesList = document.getElementById('rules-list');
    const prolongButton = document.getElementById('prolong-button');

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

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    prolongButton.addEventListener('click', async () => {
        const response = await fetch('/pay', {
            method: 'POST'
        });
        const data = await response.json();
        appendMessage('MR. BARNARD', data.message, 'bot-message');
        prolongButton.style.display = 'none';
    });

    // Function to load rules
    async function loadRules() {
        const response = await fetch('/static/guide.json');
        const data = await response.json();
        data.rules.forEach((rule, index) => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<b>Rule #${index + 1}:</b> ${rule.text}`;
            rulesList.appendChild(listItem);
        });
    }

    loadRules();

    async function checkStatus() {
        const response = await fetch('/check_status');
        const data = await response.json();
        if (data.message) {
            appendMessage('MR. BARNARD', data.message, 'bot-message');
            prolongButton.style.display = 'block';
        }
        setTimeout(checkStatus, 30000);
    }

    checkStatus();
});

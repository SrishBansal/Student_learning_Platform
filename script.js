document.addEventListener("DOMContentLoaded", () => {
    App.init();
});

const App = (() => {
    function init() {
        UI.loadHeader();
        UI.loadFooter();
        UI.loadContent();
        document.getElementById('ask-button').addEventListener('click', askQuestion);
    }

    async function askQuestion() {
        const userInput = document.getElementById('user-input').value;
        const responseDiv = document.getElementById('response');

        if (!Validator.validateInput(userInput)) {
            UI.showError(responseDiv, 'Please enter a question.');
            return;
        }

        UI.showLoader(responseDiv);

        try {
            const response = await API.postQuestion(userInput);
            UI.showResponse(responseDiv, response.answer);
        } catch (error) {
            UI.showError(responseDiv, `Error: ${error.message}`);
        }
    }

    return { init };
})();

const UI = (() => {
    function loadHeader() {
        const header = document.getElementById('header');
        header.innerHTML = `<h1>AI Learning Companion</h1>`;
    }

    function loadFooter() {
        const footer = document.getElementById('footer');
        footer.innerHTML = `<p>&copy; 2024 Learning Companion. All rights reserved.</p>`;
    }

    function loadContent() {
        const content = document.getElementById('content');
        content.innerHTML += `<p>Welcome to your personalized learning experience!</p>`;
    }

    function showLoader(element) {
        element.innerHTML = `
            <div class="loader">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>`;
    }

    function showResponse(element, message) {
        element.innerHTML = `<p class="response">${message}</p>`;
        element.classList.add('fade-in');
    }

    function showError(element, message) {
        element.innerHTML = `<p class="error">${message}</p>`;
        element.classList.add('fade-in');
    }

    return {
        loadHeader,
        loadFooter,
        loadContent,
        showLoader,
        showResponse,
        showError
    };
})();

const API = (() => {
    const apiKey = 'AIzaSyAM6aieQA9pJANS_cLtkrIhTZGc4oyGphE'; 

    async function postQuestion(question) {
        const context = "The capital of France is Paris. It is known for its art, fashion, and culture."; 
        const response = await fetch('https://api.gemini.ai/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: "gemini",
                messages: [
                    { role: "user", content: question },
                    { role: "assistant", content: context }
                ],
                max_tokens: 150,
                temperature: 0.7,
            }),
        });

        if (!response.ok) {
            throw new Error('Failed to fetch the answer.');
        }

        const data = await response.json();
        return { answer: data.choices[0].message.content };
    }

    return {
        postQuestion
    };
})();

const Validator = (() => {
    function validateInput(input) {
        return input.trim() !== '';
    }

    return {
        validateInput
    };
})();

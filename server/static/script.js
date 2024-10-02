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
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_input: userInput,
                    student_name: "John Doe", 
                    student_profile: {
                        age: 15,               
                        preferred_subject: "Math",
                        learning_style: "Visual"
                    }
                })
            });

            if (!response.ok) {
                throw new Error('Failed to get response from the server.');
            }

            const data = await response.json();
            UI.showResponse(responseDiv, data.response);

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
        footer.innerHTML = `<p>© 2024 Learning Companion. All rights reserved.</p>`;
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


const Validator = (() => {
    function validateInput(input) {
        return input.trim() !== '';
    }

    return {
        validateInput
    };
})();

// Initialize the app
App.init(); 
document.addEventListener("DOMContentLoaded", () => {
    loadHeader();
    loadFooter();
    loadContent();

    document.getElementById('ask-button').addEventListener('click', askQuestion);
});

function loadHeader() {
    const header = document.getElementById('header');
    header.innerHTML = `<h1>AI Learning Companion</h1>`;
}

function loadFooter() {
    const footer = document.getElementById('footer');
    footer.innerHTML = `<p>&copy; 2024 Learning Companion</p>`;
}

function loadContent() {
    const content = document.getElementById('content');
    content.innerHTML += `<p>Welcome to your personalized learning experience!</p>`;
}

async function askQuestion() {
    const userInput = document.getElementById('user-input').value;
    const responseDiv = document.getElementById('response');

    if (!userInput) return;

    try {
        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userInput }),
        });

        const data = await response.json();
        responseDiv.innerHTML = `<p>${data.answer}</p>`;
    } catch (error) {
        responseDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}

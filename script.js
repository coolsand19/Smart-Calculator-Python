document.addEventListener('DOMContentLoaded', () => {
    const universalInput = document.getElementById('universal-input');
    const languageOutput = document.getElementById('language-output');
    const resetQueryBtn = document.getElementById('reset-query-btn');
    const equationInput = document.getElementById('equation');
    const resultInput = document.getElementById('result');
    const buttons = document.querySelector('.buttons');
    const equalsButton = document.getElementById('equals');
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    let equation = '';
    let result = '';
    let isEqualsPressed = false;

    // Dark Mode
    darkModeToggle.addEventListener('change', () => {
        document.body.classList.toggle('dark-mode');
    });

    // Universal Input
    universalInput.addEventListener('keydown', async (event) => {
        if (event.key === 'Enter') {
            const query = universalInput.value;
            if (!query) return;

            try {
                const response = await fetch('http://127.0.0.1:8000/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ equation: query }),
                });

                const data = await response.json();

                if (data.error) {
                    languageOutput.textContent = `Error: ${data.error}`;
                } else {
                    languageOutput.textContent = data.result;
                }
            } catch (error) {
                languageOutput.textContent = 'An error occurred while fetching the result.';
                console.error('Error:', error);
            }
        }
    });

    // Reset Query
    resetQueryBtn.addEventListener('click', () => {
        universalInput.value = '';
        languageOutput.textContent = '';
    });

    // Button Clicks
    buttons.addEventListener('click', (event) => {
        const button = event.target;
        const buttonText = button.textContent;

        if (button.tagName !== 'BUTTON') {
            return;
        }

        handleInput(buttonText);
    });

    // Keyboard Input
    document.addEventListener('keydown', (event) => {
        // Prevent keyboard input from interfering with the universal input
        if (document.activeElement === universalInput) {
            return;
        }

        const key = event.key;

        if (/[0-9]/.test(key)) {
            handleInput(key);
        } else if (/[\+\-\*\/]/.test(key)) {
            handleInput(key);
        } else if (key === '%') {
            handleInput('%');
        } else if (key === '.') {
            handleInput('.');
        } else if (key === 'Enter' || key === '=') {
            event.preventDefault();
            handleInput('=');
        } else if (key === 'Backspace') {
            handleInput('←');
        } else if (key.toLowerCase() === 'c') {
            handleInput('C');
        }
    });

    function handleInput(input) {
        if (input === 'C') {
            equation = '';
            result = '';
            isEqualsPressed = false;
        } else if (input === '←') {
            equation = equation.slice(0, -1);
            result = '';
            isEqualsPressed = false;
        } else if (input === '=') {
            if (isEqualsPressed) {
                equation = result;
                result = '';
                isEqualsPressed = false;
            } else {
                if (equation === '') return;
                try {
                    result = eval(equation);
                    isEqualsPressed = true;
                } catch (error) {
                    result = 'Error';
                }
            }
        } else {
            if (isEqualsPressed) {
                if (/[\+\-\*\/]/.test(input)) {
                    equation = result + input;
                } else {
                    equation = input;
                }
                isEqualsPressed = false;
            } else {
                equation += input;
            }
            result = '';
        }

        equationInput.value = equation;
        resultInput.value = result;
    }
});
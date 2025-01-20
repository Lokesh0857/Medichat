from flask import Flask, request, jsonify
import requests
# Initialize Flask app
app = Flask(__name__)

# Ollama API endpoint
OLLAMA_API_URL = "ollama run llama3.2"

# Home route
@app.route('/')
def home():
    return """
    <h1>Ollama AI Chatbot</h1>
    <div>
        <form id="chatForm">
            <label for="userInput">Ask me anything:</label><br>
            <input type="text" id="userInput" name="userInput" required><br><br>
            <button type="submit">Send</button>
        </form>
        <div id="chatResponse"></div>
    </div>
    <script>
        const form = document.getElementById('chatForm');
        form.onsubmit = async (e) => {
            e.preventDefault();
            const userInput = document.getElementById('userInput').value;
            const responseDiv = document.getElementById('chatResponse');
            responseDiv.innerText = 'Thinking...';

            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userInput })
            });

            const data = await response.json();
            responseDiv.innerText = `AI: ${data.response}`;
        };
    </script>
    """

# Chat API route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    # Prepare the request payload for Ollama API
    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": user_message}]
    }

    try:
        # Make a request to Ollama API
        response = requests.post('ollama run llama3.2', json=payload)
        response_data = response.json()
        ai_message = response_data['response']
        return jsonify({"response": ai_message.strip()})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

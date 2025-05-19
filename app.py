from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Add this to respond to GET requests at "/"
@app.route('/', methods=['GET'])
def index():
    return "✅ Flask backend is running!"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '').lower().strip()

    if user_input == "hi":
        reply = "hello, Ronamae Salve :)"
    else:
        reply = "I don't understand."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    print("✅ Flask server is running at http://localhost:5000")
    app.run(debug=True)



from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Jenkins Docker build!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received:", data)  # You’ll see this in console
    return "Webhook received!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

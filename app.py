import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Wi-Fi!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))  # default for local dev
    app.run(host='0.0.0.0', port=port)


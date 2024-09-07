from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, pfSense-like Project!"

if __name__ == '__main__':
    app.run(debug=True)

# Create a function to check if a given IP address is valid

from flask import Flask

server = Flask(__name__)

# Define a route for the root URL ("/")
@server.route("/")
def index():
    # Function that handles requests to the root URL
    # return "Hello, World!"

    return {
        'message': 'Hello, World!'
    }
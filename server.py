from flask import Flask, jsonify, request
import pyshorteners
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return jsonify("Hello, This is home route")

# Define a route that accepts a parameter and returns a message
# @app.route('/greet/<name>')
# def greet(name):
#     return f"Hello, {name}! Welcome to Flask."

@app.route('/shortner', methods=['POST'])
def shortner():
    link = request.form['link']
    s = pyshorteners.Shortener()
    shortLink = (s.tinyurl.short(link))
    print(link, '==', shortLink )
    return shortLink

if __name__ == '__main__':
    app.run(debug=True)

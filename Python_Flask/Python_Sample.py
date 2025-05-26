from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello World" # printing



def hello2():
    return "my name is Pranay" # printing


@app.route('/enter_name')

def name():
    return "What is Your Name? My name is ___"

app.run(debug=True)


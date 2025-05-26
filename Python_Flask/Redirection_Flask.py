from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder="Files")

@app.route('/')

def hello():
    return render_template('Hello_World.html')

app.run(debug = True)
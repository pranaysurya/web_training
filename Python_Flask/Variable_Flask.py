from flask import Flask

app = Flask(__name__)

@app.route('/<float:date>') 
def Hello(date):
    return "date = %f " %date

app.run(debug=True)
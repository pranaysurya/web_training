from flask import Flask, request, jsonify

app = Flask(__name__)

#https://www.google.com/search?q=hello

#http://127.0.0.1:5000/add?num1=1,num2=2

@app.route('/')
def home():
    return "<a href='http://127.0.0.1:5000/add?num1=1&num2=2'>Hello</a>"

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return jsonify({
            'num1': num1,
            'num2': num2,
            'result': result
        })
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide numeric values.'})

if __name__ == '__main__':
    app.run(debug=True)
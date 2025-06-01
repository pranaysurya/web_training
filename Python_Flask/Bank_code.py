from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "Html_Files")

@app.route('/')
def Bank_Login():
    return render_template("Bank_Login.html")

balance = 0

@app.route('/balance', methods = ["GET"])
def Balance():
    return render_template("Bank_Balance.html", value = balance)

@app.route('/deposit', methods = ["GET", "POST"])
def Deposit():
    global value
    deposit = request.form['deposit_value'] 

    return render_template("Bank_Balance.html", value = deposit)

@app.route('/withdrawal')
def Withdrawal():
    return render_template("Bank_Withdrawal.html")

app.run(debug=True)

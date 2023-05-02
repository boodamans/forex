from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"

symbols=[]

@app.route("/")
def homepage():
    list = []
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    symbols = dict.keys(data['symbols'])

    print(symbols)

    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    print('Route found!')

    convfrom = request.form.get('from')
    convto = request.form.get('to')
    amount = request.form.get('amount')

    url = f'https://api.exchangerate.host/convert?from={convfrom}&to={convto}&amount={amount}'
    response = requests.get(url)
    data = response.json()
    result = data['result']
    rounded = round(result, 2)
    print(rounded)

    # print(convfrom, convto, amount)
    
    return render_template('index.html', rounded=rounded, convto = convto)
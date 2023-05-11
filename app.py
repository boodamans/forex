from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"

symbols=[]

@app.route("/")
def homepage():
    symbols_url = 'https://api.exchangerate.host/symbols'
    symbols_response = requests.get(symbols_url)
    data = symbols_response.json()
    symbols = dict.keys(data['symbols'])

    return render_template("index.html", symbols=symbols)

@app.route('/convert', methods=['POST'])
def convert():
    try:
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

        symbols_url = 'https://api.exchangerate.host/symbols'
        symbols_response = requests.get(symbols_url)
        data = symbols_response.json()
        symbols = dict.keys(data['symbols'])
    
        return render_template('index.html', rounded=rounded, convto = convto, symbols=symbols)
    
    except TypeError:
        err = 'Invalid amount'
        return redirect('/')

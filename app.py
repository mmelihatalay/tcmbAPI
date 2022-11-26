from flask import Flask
import APICalls
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<h1>Welcome to TCMB exchange API</h1>"


@app.route("/exchange/<currency>")
def currencyExchange(currency):
    tcmb = APICalls.TCMBAPICall()
    try:
        return tcmb.getCurrentExchange(currency)
    except:
        return {'Warning': 'Not a valid currency'}


@app.route("/exchange")
def Exchange():
    tcmb = APICalls.TCMBAPICall()
    return tcmb.getAllCurrencies()

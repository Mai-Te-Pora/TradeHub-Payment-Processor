from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, FileField, IntegerField, validators, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import NumberInput
import payment_processor

# This app instance is what is missing from `redirect.py`
app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = '=hwqwM$D774|x#P'

# Flask-Bootstrap requires this line
Bootstrap(app)

#See payment_processor.py
prices = payment_processor.calculate_payment()

#Creating dict of amounts with tokens for display
tokens = {str(prices[0]) + " USDC",
        str(prices[1]) + " BUSD",
        str(prices[2]) + " SWTH",
        str(prices[3]) + " LKT",
        str(prices[4]) + " CEL",
        str(prices[5]) + " ETH",
        }

class SubmitForm(FlaskForm):
    opt = SelectField('Choose Token', choices=[(t, f"{t}") for t in tokens])
    hash = StringField('Please enter the Txn Hash of the Switcheo Tradehub Internal Transfer')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', "PUT"])
def index():
    title = "Payment Processor"
    to_address = payment_processor.to_address()

    #Display token is USDC
    token = 'USDC'
    fee = prices[0]

    #Create Payment Form
    form = SubmitForm()
    return render_template('index.html', title = title, fee = fee, token = token, to_address=to_address, form=form)

@app.route('/', methods=['POST'])
def my_form_post():
    TxnHash = request.form['hash']
    token = request.form['opt']
    token, fee = payment_processor.user_input(token, prices)
    success, token, fee, title, header_message, rtn_message = payment_processor.confirm_payment(token, fee, TxnHash)
    return render_template('template.html', title = title, token=token, fee=fee, header_message=header_message, rtn_message=rtn_message)

app.run(host='localhost', port=5000)

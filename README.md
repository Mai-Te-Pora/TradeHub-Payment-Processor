# TradeHub-Payment-Processor
Tradehub blockchain internal transfer used as Payment Processor
Requires Python 3.8+
Requires Tradehub
Install via pip install tradehub

Python file possesses the base functionality to check user input of a TxnHash with a registered token (swth) and amount.

Example File:
The example file gives a demonstration of how the functionality can be used as a payment processor. It is a Flask run App (not ready for production) built to assist potential HTML developers in implementing TradeHub payments on your site. (Note: Requires TradeHub Wallet - See dem.exchange to sign up!)

Running example:
Example will require Flask, Flask-wtf
Nagivate to Example folder in terminal
Run python example.py
Proram will run on localhost:5000

Notes:
Receiver address will need to change before implementation. It is currently set to programmers' public address.

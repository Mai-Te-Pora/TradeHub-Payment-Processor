# TradeHub-Payment-Processor
Tradehub blockchain internal transfer used as Payment Processor<br>
Requires Python 3.8+<br>
Requires Tradehub<br>
Install via pip install tradehub<br>
<br>
Python file possesses the base functionality to check user input of a TxnHash with a registered token (swth) and amount.<br>
<br>
Example File:<br>
The example file gives a demonstration of how the functionality can be used as a payment processor with multiple tokens (Switcheo, Ethereum, Celsius Network, USD Coin, Binance USD). It is a Flask run App (not ready for production) built to assist HTML developers in implementing TradeHub payments on their site. (Note: Requires TradeHub Wallet - See dem.exchange to sign up!)<br>
<br>
Running example:<br>
Example will require Flask, Flask-wtf<br>
Nagivate to Example folder in terminal<br>
Run python example.py<br>
Program will run on localhost:5000<br>

Notes:<br>
Receiver address will need to change before implementation. It is currently set to programmers' public address.

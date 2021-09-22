# IMPORTING IMPORTANT LIBRARIES
from datetime import timedelta
import asyncio
import time
import iso8601
import json
import random
from tradehub.public_account_client import PublicClient
import logging
import sys

#Note: Enter your own receiver address. Currently listed with programmers' address
receiver_address = "swth1dwdvy48exj22st0zvwk8s3k9tfnksrj9v7fhuu"

def confirm_payment():
    #Setting up logger
    root = logging.getLogger()
    root.setLevel(logging.WARNING)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    #Initiating msg dict
    msg = {}

    #Txn Hash for testing...see example/payment_processor.py
    #More functionality is needed - pass Txn Hash to confirm_payment
    #Functionality example can be found at example/payment_processor.py
    TxnHash = 'ENTER Txn Hash'
    denom = 'swth'

    #Connect to Tradehub Public Client and retrieve transaction data
    pc = PublicClient(network='mainnet', trusted_uris=["http://54.255.5.46:5001", "http://175.41.151.35:5001"])
    data = pc.get_transaction(TxnHash)

    #Parse out msg from data nd store in msg dict
    for m in data['msgs']:
        if 'msg' in m:
            msg = json.loads(m['msg'])

    #Retrieve to_address from msg
    to_address = msg['to_address']

    #retrieve amount from msg
    amount = msg['amount']

    #Check if amount, token and fee match
    if amount[0]['denom']== denom:
        if (int(amount[0]['amount'])/100000000) == fee:
            #Do Something
            print("Success")
        else:
            root.error("The fee amount didn't match. Please contact customer support.")
    else:
        root.error("The denom amount didn't match. Please contact customer support.")

def to_address():
    return receiver_address

def calculate_payment():
    #Do something to calculate payment and return the value
    #For purpose of example, I am using a random int between 100-500
    fee = random.randrange(100,500)
    return fee

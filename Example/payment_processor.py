# IMPORTING LIBRARIES
import random
from tradehub.public_account_client import PublicClient
import logging
import sys

#To Payment Address..Please change to YOUR PUBLIC ADDRESS
#For purposes of example, the address is the programmers c1im4cu5'
receiver_address = "swth1dwdvy48exj22st0zvwk8s3k9tfnksrj9v7fhuu"

#Dict of dicts tradehub pairs and divisions
denoms = {
        'swth':{'denom':'swth', 'decimals':100000000},
        'lkt':{'denom':'lkt.7ef7febf', 'decimals':1000000000000000000},
        'usdc1':{'denom':'usdc1', 'decimals':1000000},
        'busd1':{'denom':'busd1', 'decimals':1000000000000000000},
        'eth1':{'denom':'eth1', 'decimals':100000000},
        'cel1':{'denom':'cel1', 'decimals':10000},
        }

def confirm_payment(denom, fee, TxnHash):
    #Setting up logger
    root = logging.getLogger()
    root.setLevel(logging.WARNING)

    #Setting up logger to print on terminal-stdout (Note: Need to set to DEBUG if you want to see all processes)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    #Initial msg to hold dict data
    msg = {}
    TxnHash = TxnHash
    denom = denom
    fee = fee

    #Initiate return messages
    success = False
    title = "Fail"
    header_message = "Unsucessful"
    rtn_message = "The program was unsuccessful. Please contact contact c1im4cu5 on github."

    #Connect to Tradehub public client
    pc = PublicClient(network='mainnet', trusted_uris=["http://54.255.5.46:5001", "http://175.41.151.35:5001"])
    #Retrieve transaction details from publc client
    data = pc.get_transaction(TxnHash)

    #Confirm "msgs" in transaction details
    try:
        for m in data['msgs']:
            if 'msg' in m:
                msg = json.loads(m['msg'])
    except:
        root.error("Cannot find msgs in transaction details.")
        return success, fee, title, header_message, rtn_message

    #Confirm "msg" and associated address, amount in transaction details
    try:
        to_address = msg['to_address']
        amount = msg['amount']
    except:
        root.error("The Txn Hash could be incorrect. Cannot find address and/or amount in transaction details.")
        return success, fee, title, header_message, rtn_message

    #Confirm amount of denom/token matches expected
    if denom in amount[0]['denom']:
        #Check if amount paid matches invoice
        print (int(amount[0]['amount'])/denoms[denom]['decimals'])
        if (int(amount[0]['amount'])/denoms[denom]['decimals']) == fee:
            #Success! Do Something
            #For example, we are printing Success in terminal and returning values for an html page
            print("Success")
            success = True
            title = "Success"
            header_message = "SUCCESS"
            rtn_message = "Thank you for the donation/payment!"
            return success, denom, fee, title, header_message, rtn_message
        else:
            root.error("The fee amount didn't match")
            return success, denom, title, fee, header_message, rtn_message
    else:
        root.error("The denom amount didn't match")
        return success, denom, fee, title, header_message, rtn_message

def to_address():
    return receiver_address

def calculate_payment():
    #Connect to Tradehub public client
    pc = PublicClient(network='mainnet', trusted_uris=["http://54.255.5.46:5001", "http://175.41.151.35:5001"])

    #Get Current Markets
    swth_price = pc.get_market_stats('swth_usdc1')
    lkt_price = pc.get_market_stats('lkt1_usdc1')
    cel_price = pc.get_market_stats('cel1_usdc1')
    busd_price = pc.get_market_stats('busd1_usdc1')
    eth_price = pc.get_market_stats('eth1_usdc1')

    #Do something to calculate payment and return the value
    #For purpose of example, I am using a random int between 2 and 7
    fee = random.randrange(2,7)
    usdc_price = float(fee)

    #Using the USDC price, calculate all other token amounts
    swth_amt = round(usdc_price/float(swth_price[0]['last_price']))
    lkt_amt = round(usdc_price/float(lkt_price[0]['last_price']))
    cel_amt = round(usdc_price/float(cel_price[0]['last_price']), 2)
    busd_amt = round(usdc_price/float(busd_price[0]['last_price']), 2)
    eth_amt = round(usdc_price/float(eth_price[0]['last_price']), 4)

    #Group prices together for return
    current_prices = [usdc_price, busd_amt, swth_amt, lkt_amt, cel_amt, eth_amt]

    return current_prices

def user_input(selection, prices):
    #User Selected Token and Price
    selection = selection
    prices = prices

    #Initiating variables
    price = 0
    token = ""

    #Checking string selection for token
    if "USDC" in selection:
        token = "usdc1"
        price = float(prices[0])
    elif "BUSD" in selection:
        token = "busd1"
        price = float(prices[1])
    elif "SWTH" in selection:
        token = "swth"
        price = float(prices[2])
    elif "LKT" in selection:
        token = "lkt.7ef7febf"
        price = float(prices[3])
    elif "CEL" in selection:
        token = "cel1"
        price = float(prices[4])
    elif "ETH" in selection:
        token = "eth1"
        price = float(prices[5])
    return token, price

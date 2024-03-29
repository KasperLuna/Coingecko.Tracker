#!/usr/bin/env python
from pycoingecko import CoinGeckoAPI
import time
from prettytable import PrettyTable
cg = CoinGeckoAPI()
table = PrettyTable()
table.border = False


usd_coins = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "ADA": "cardano",
    "DOT": "polkadot",
    "ALGO": "algorand",
    "LINK": "chainlink",
    "XTZ": "tezos",
    "ONE": "harmony"
}

php_coins = {
    "SLP": "smooth-love-potion",
    "AXS": "axie-infinity"
}


r = "\033[0;31;40m"  # Red
y = "\033[0;33;40m"
g = "\033[0;32;40m"  # Green
x = "\033[0m"  # Reset


def list_keys(to_list):
    return list(to_list.keys())


def list_vals(to_list):
    return list(to_list.values())


def trend(num):
    parse = float(num)
    if parse > 0:
        return g+str(parse)+x
    elif parse < 0:
        return r+str(parse)+x
    else:
        return parse

# coin = array of coins
# pair = array of coin symbols
# source = json array source query (coins, axie)
# currency = string abbrev of currency


def enter(coin, pair, source, currency):
    i = 0
    length = len(coin)
    for i in range(length):
        pairname = pair[i]+'-'+str.upper(currency)
        price = source[coin[i]][currency]
        change = trend('{:.2f}'.format(
            source[coin[i]][currency+'_24h_change']))

        table.add_row([pairname, price, change])


while True:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    table.clear_rows()

    import datetime
    d = datetime.datetime.today()
    dateTimeNow = d.strftime("%d-%m-%Y %H:%M:%S")
    print(dateTimeNow)

    coins = cg.get_price(ids=list_vals(usd_coins),
                         vs_currencies='usd', include_24hr_change='true')
    axie = cg.get_price(ids=list_vals(php_coins), vs_currencies='php',
                        include_24hr_change='true')
    usdt = cg.get_price(ids='tether', vs_currencies='php')['tether']['php']
    table.field_names = ["Pair", "Price", "24h%"]

    enter(list_vals(usd_coins), list_keys(usd_coins), coins, "usd")
    enter(list_vals(php_coins), list_keys(php_coins), axie, "php")

    print(table)
    print('')
    print("USDT-PHP: {}".format(usdt))

    time.sleep(10)

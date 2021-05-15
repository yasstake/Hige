
import json
import time

import urllib.request


BB_LIQUIDATION_URL = "https://api.bybit.com/v2/public/liq-records?symbol=BTCUSD&limit=1000"


def get_liquidation(from_id = 0):
    '''
    accsss bybit Liquidation API and print data
    :param from_id: record id (from parameter)
    :return: next record id to be get from.
    '''

    request = urllib.request.Request(BB_LIQUIDATION_URL + "&from=" + str(from_id))

    liquid_id = 0
    liquid_qty = 0
    liquid_side = ""
    liquid_time = 0
    liquid_symbol = ""
    liquid_price = 0

    with urllib.request.urlopen(request) as response:

        body = response.read()
        json_message = json.loads(body)

        for liquid in json_message['result']:
            liquid_id = liquid['id']
            liquid_qty = liquid['qty']
            liquid_side = liquid['side']
            liquid_time = liquid['time']
            liquid_symbol = liquid['symbol']
            liquid_price = liquid['price']

            print(liquid_time/1_000, ',', liquid_symbol, ',', liquid_side, ',', liquid_qty, ',', liquid_price, ',,,,,')
            #print(liquid_id, ',', liquid_qty,' ,', liquid_side, ',', pd.Timestamp(ts_input=liquid_time*1_000_000), ',', liquid_symbol, ',', liquid_price)

    if liquid_id != 0:
        return liquid_id + 1

    return from_id


if __name__ == '__main__':
    last_id = 0
    count = 3

    print('timestamp,symbol,side,size,price,tickDirection,trdMatchID,grossValue,homeNotional,foreignNotional')

    while True:
        last_id = get_liquidation(last_id)
        time.sleep(1)

        if count == 0:
            break
        count -= 1


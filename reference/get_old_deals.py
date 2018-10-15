#!/usr/bin/python3

import get_cheapest_prices
import json

def get_yesterday():
    sortopts = 'order by x.lastseen desc'
    #querydate = '= subdate(curdate(),3)'
    #querydate = '= curdate() -7'
    querydate = 'between curdate() - interval \'7\' day and curdate()'
    cheapDict = {None}
    cheapDict = get_cheapest_prices.main(querydate,sortopts)
    print(cheapDict)
    with open("/var/www/pricer/pricer/sevendayDict.dict","w") as fo:
        fo.write(json.dumps(cheapDict))
    #return cheapDict


def load_yesterday():
    cheapDict = json.load(open("/var/www/pricer/pricer/sevendayDict.dict"))
    print('Printing cheapDict from file')
    print(cheapDict)
        

if __name__ == '__main__':
    get_yesterday()
    #load_yesterday()
    #get_yesterday()

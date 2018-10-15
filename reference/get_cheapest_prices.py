#!/usr/bin/python3
#from __future__ import print_function
import datetime
import mysql.connector
import sys
import sanitizer

def main(querydate, sortopts):
    cnx = mysql.connector.connect(user='parsley',password='wmScanner!', database='deal_data')
    cursor = cnx.cursor()
    
    query = ("select f.name, f.upc, f.sku, f.storeId, f.msrp, f.salePrice, DATE_FORMAT(f.last_seen_date, '%m/%d/%Y'), f.imageUrl "
             "from (  select name, upc, sku, storeId, msrp, last_seen_date as lastseen, min(salePrice) as minprice, imageUrl "
             "from deals where last_seen_date "+ querydate +" group by upc ) as x inner join deals as f "
             "where (f.upc = x.upc and f.salePrice = x.minprice and f.last_seen_date = x.lastseen) group by upc " + sortopts + ";")
    #original query that works
    #query = ("select f.name, f.upc, f.sku, f.storeId, f.msrp, f.salePrice, DATE_FORMAT(f.last_seen_date, '%m/%d/%Y') "
    #         "from (  select name, upc, sku, storeId, msrp, last_seen_date as lastseen, min(salePrice) as minprice "
    #         "from deals where last_seen_date "+ querydate +" group by upc ) as x inner join deals as f "
    #         "on (f.upc = x.upc and f.salePrice = x.minprice and f.last_seen_date = x.lastseen) group by upc " + sortopts + ";")
    
    cursor.execute(query)
    
    #print(cursor)
    #print("UPC | barcode link | SKU | storeId | onlinePrice | storePrice | Product Name", sep = '\t')
    print("{:10} | {:12} | {:37} | {:9} | {:^7} | {:9} | {:9} | {}".format("Date", "UPC", "barcode link", 
                "SKU", "storeId", "online", "store", "Product Name"))
    cheapDict = {}
    count = int(0)
    for (name, upc, sku, storeId, onlinePrice, storePrice, date, imageUrl) in cursor:
        itemname = (name[:48] + '..') if len(name) > 48 else name
        #onlinePrice = onlinePrice // 100
        #price = "$" + {storePrice:,.2f}
        
        cheapDict[count] = { 
                'imageUrl': imageUrl,
                'name': name,
                'storeId': storeId,
                'upc': upc,
                'sku': sku,
                'onlinePrice': ("${:8,.2f}".format((onlinePrice / 100.00))),
                'storePrice': ("${:8,.2f}".format((storePrice / 100.00))),
                'date': date,
            }
        count += 1
        print("{6} | {1} | https://candybarcode.com/{1} | {2:9} | {3:7} | ${4:8,.2f} | ${5:8,.2f} | {0} "
                .format(itemname, upc, sku, storeId, (onlinePrice / 100.00), (storePrice / 100.00), date))
    #return cursor 
    cursor.close()
    cnx.close()
    #print(cheapDict)
    return cheapDict

if __name__ == '__main__':
    if len(sys.argv) == 2:
        querydate = ('= curdate() -' + str(sanitizer.sanitize_num_input("How many days ago? ", int, None, 1, 30, range(1,30))))
        sortopts = ('order by x.lastseen desc')
    else:
        querydate = '= curdate()'
        sortopts = ""
    main(querydate,sortopts)

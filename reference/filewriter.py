#!/usr/bin/python3

#This is the filewriter function derived from dbwriter to write to file instead of db
# File will be read in by dbwriter to use one connection instead of hundreds. 
from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector.constants import ClientFlag
config = {
        'user': 'ssldbuser',
        'password': 'sslDB1@3$',
        'host': 'pricer.tk',
        'port': '3306',
        'database': 'deal_data',
        }


def db_writer(itemData,storeId,categoryId,email=None,cnx=None):
    #Sometimes items don't display an online price, let's work around that.
    try:
        msrp = int(itemData['data']['online']['price']['priceInCents'])
    except KeyError:
        msrp = int('999999')
        pass
    try:
        stockstatus = str(itemData['data']['online']['inventory']['status'])
    except KeyError:
        stockstatus = str("N/A")
        pass
    #TODO: strip single and double quotes from name for compatibility
    itemName = str(itemData['data']['common']['name']).replace('"','')
    itemName = str(itemData['data']['common']['name']).replace('\'','')
    try:
        item_data = {
                "name": itemName,
                "upc": str(itemData['data']['common']['productId']['upca']),
                "msrp": msrp,
                "salePrice": int(itemData['data']['inStore']['price']['priceInCents']),
                "storeId": int(storeId),
                "status": stockstatus,
                "requestId": str(itemData['meta']['requestId']),
                "webUrl": str(itemData['data']['common']['productUrl']),
                "imageUrl": str(itemData['data']['common']['productImageUrl']),
                "productId": str(itemData['data']['common']['productId']['productId']),
                "sku": str(itemData['data']['common']['productId']['wwwItemId']),
                "categoryId": categoryId,
                }
        print(item_data)
        f = open("/media/ramdisk/itemdata.dict","a")
        f.write(str(item_data))
        f.close()
    except:
        pass


def watchlist_writer(itemData,storeId,categoryId,cnx=None):
    #Sometimes items don't display an online price, let's work around that.
    try:
        msrp = int(itemData['data']['online']['price']['priceInCents'])
    except KeyError:
        msrp = int('999999')
        pass
    try:
        stockstatus = str(itemData['data']['inStore']['inventory']['status'])
    except KeyError:
        stockstatus = str("N/A")
        pass
    #TODO: strip single and double quotes from name for compatibility
    itemName = str(itemData['data']['common']['name']).replace('"','')
    itemName = str(itemData['data']['common']['name']).replace('\'','')
    try:
        item_data = {
                "name": itemName,
                "upc": str(itemData['data']['common']['productId']['upca']),
                "msrp": msrp,
                "salePrice": int(itemData['data']['inStore']['price']['priceInCents']),
                "storeId": int(storeId),
                "status": stockstatus,
                "requestId": str(itemData['meta']['requestId']),
                "webUrl": str(itemData['data']['common']['productUrl']),
                "imageUrl": str(itemData['data']['common']['productImageUrl']),
                "productId": str(itemData['data']['common']['productId']['productId']),
                "sku": str(itemData['data']['common']['productId']['wwwItemId']),
                "categoryId": categoryId,
                }
        print(item_data)
        f = open("/media/ramdisk/watchlist.dict","a")
        f.write(str(item_data))
        f.close()
    except:
        pass


def db_from_file(itemData):
    #setup our db connection
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    today = datetime.now().date()
    for key,value in itemData.items():
        item_data = {
                '`name`': str(value['name']),
                'upc': str(value['upc']),
                'msrp': str(value['msrp']),
                'salePrice': str(value['salePrice']),
                'storeId': str(value['storeId']),
                '`status`': str(value['status']),
                'requestId': str(value['requestId']),
                'webUrl': str(value['webUrl']),
                'imageUrl': str(value['imageUrl']),
                'productId': str(value['productId']),
                'sku': str(value['sku']),
                'last_seen_date': today,
                'categoryId': str(value['categoryId']),
                }
        add_data_2db = ("INSERT INTO deals "
                        "(`name`, upc, msrp, salePrice, storeId, `status`, "
                        "last_seen_date, webUrl, imageUrl, requestId, productId, sku, categoryId) "
                        "VALUES (%(`name`)s, %(upc)s, %(msrp)s, %(salePrice)s, %(storeId)s, "
                        "%(`status`)s, %(last_seen_date)s, %(webUrl)s, %(imageUrl)s, %(requestId)s, "
                        "%(productId)s, %(sku)s, %(categoryId)s)")
        cursor.execute(add_data_2db, item_data)
    #After all has been inserted, let's commit.
    cnx.commit()

def watchlist_from_file(itemData):
    #setup our db connection
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    today = datetime.now().date()
    for key,value in itemData.items():
        item_data = {
                '`name`': str(value['name']),
                'upc': str(value['upc']),
                'msrp': str(value['msrp']),
                'salePrice': str(value['salePrice']),
                'storeId': str(value['storeId']),
                '`status`': str(value['status']),
                'requestId': str(value['requestId']),
                'webUrl': str(value['webUrl']),
                'imageUrl': str(value['imageUrl']),
                'productId': str(value['productId']),
                'sku': str(value['sku']),
                'last_seen_date': today,
                'categoryId': str(value['categoryId']),
                }
        add_data_2db = ("INSERT INTO watchlist "
                        "(`name`, upc, msrp, salePrice, storeId, `status`, "
                        "last_seen_date, webUrl, imageUrl, requestId, productId, sku, categoryId) "
                        "VALUES (%(`name`)s, %(upc)s, %(msrp)s, %(salePrice)s, %(storeId)s, "
                        "%(`status`)s, %(last_seen_date)s, %(webUrl)s, %(imageUrl)s, %(requestId)s, "
                        "%(productId)s, %(sku)s, %(categoryId)s)")
        cursor.execute(add_data_2db, item_data)
    #After all has been inserted, let's commit.
    cnx.commit()

def main(itemData,storeId):
    db_writer(itemData,storeId)


if __name__ == '__main__':
    itemData = {}
    storeId = int(0)
    main(itemData,storeId)

#!/usr/bin/python3
# Test loop.py program to iterate through pages of clearance data from walmart.com using their dev api
#
#FIXME: Make the loop stop when user doesn't want next page instead of having to ctrl+c
#TODO: Maybe make a menu to select which category we want to search instead of having to input numbers?
#The below line is a holdover from pre-python3 port of the code
#from __future__ import print_function
import requests, sys

# Sample API calls using curl    
# Follow this format when building urls using python below
# 3944 is Electronics
# 1105910_1231258_1231262 is iPhones
#curl -s "https://api.walmartlabs.com/v1/paginated/items?category=3944&specialOffer=clearance&apiKey=frt6ajvkqm4aexwjksrukrey&format=json
#curl -s "https://api.walmartlabs.com/v1/paginated/items?category=1105910_1231258_1231262&specialOffer=clearance&apiKey=frt6ajvkqm4aexwjksrukrey&format=json"
def next_url(itemData):
    nextURL = 'https://api.walmartlabs.com' + str(itemData['nextPage'])
    return nextURL

def get_data(itemData):
    for i in range(0,99):
        try:
            print(itemData['items'][(i)]['upc'], itemData['items'][(i)]['name'], itemData['items'][(i)]['msrp'], itemData['items'][(i)]['salePrice'])
        except KeyError as keyerr:
            if str(keyerr) == '\'msrp\'':
                try:
                    print(itemData['items'][(i)]['upc'], itemData['items'][(i)]['name'], '0', itemData['items'][(i)]['salePrice'])
                except KeyError as ke2:
                    if str(ke2) == '\'salePrice\'':
                        pass
                pass
            elif str(keyerr) == '\'salePrice\'':
                print(itemData['items'][(i)]['upc'], itemData['items'][(i)]['name'], itemData['items'][(i)]['msrp'], '0')
                pass
            pass
        except IndexError:
            print('I think we\'ve hit the end of the list...')
            break


def get_page(itemData):    
    global count
    _APIKEY = str('frt6ajvkqm4aexwjksrukrey')
    _CATEGORY = str('3944')
    if count < 1:
        #Preferred way: see examples above.
        url = ('https://api.walmartlabs.com/v1/paginated/items?category={1}&specialOffer=clearance&apiKey={0}&format=json'.format(_APIKEY, _CATEGORY))

        #url = "https://api.walmartlabs.com/v1/paginated/items?category=3944&specialOffer=clearance&apiKey=frt6ajvkqm4aexwjksrukrey&format=json"
        upcreq = requests.get(url)
        itemData = upcreq.json()
        #print itemData(1)
        count += 1
        get_data(itemData)
    else:    
        # Next Page URL for more clearance results.
        response = input("Do you want to hit the next page?")
        if response == "n":
            #Exit
            sys.exit(0)
        print('https://api.walmartlabs.com' + str(itemData['nextPage']))
        url = next_url(itemData)
        upcreq = requests.get(url)
        itemData = upcreq.json()
        get_data(itemData)
            
    return itemData
    
def main():
    itemData = {}
    global count
    count = int(0)
    while True:
        itemData = get_page(itemData)


#The proper way to invoke our script main calls
if __name__ == '__main__':
    main()

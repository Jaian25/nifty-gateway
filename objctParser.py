


def parseObject(object):
    img = object['NiftyObject']['image_preview_url']
    name = object['NiftyObject']['name']
    token = object['NiftyObject']['tokenId']
    address = object['NiftyObject']['contractAddress']
    timestamp = object['Timestamp']
    type = object['Type']
    price = 0
    if type == 'listing':
        price = object['ListingAmountInCents']
    if type == 'sale':
        price = object['SaleAmountInCents']
    return name,token,address,timestamp,type,price,img
import discord
import requests
import cv2

def genImage(img):
    vidcap = cv2.VideoCapture(img)
    success,image = vidcap.read()
    cv2.imwrite("image.jpg", image)
    return

def sendWebhookv2(name,token,address,timestamp,type,price,img):
    webhook = discord.Webhook.partial(875747881976488007, 'rvUhsOv-PuMcwgOmS12p-4GBk0xVRFqlzV3uW3ZgzR6XnSnrnEG77mKPr1BNYGbd0QYV', adapter=discord.RequestsWebhookAdapter())
    cstm_txt= ''
    price = float(price)/100
    nfty_url = f'https://niftygateway.com/marketplace?collection={address}&tokenId={token}'
    #print("Here")
    if type == 'listing':
        cstm_txt = f'**[{name} was listed for ${price}]({nfty_url})\n**'
    else:
        cstm_txt = f'**[{name} was sold for ${price}]({nfty_url})\n**'
    genImage(img)
    with open(file='image.jpg', mode='rb') as f:
        my_file = discord.File(f)
    webhook.send(cstm_txt,file=my_file)
    return
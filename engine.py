from niftyAPI import *
import json
from objctParser import parseObject
from webhook_v2 import sendWebhookv2
enlisted_id = []

def cycle():
    global enlisted_id
    events = get_events()
    for i in events:
        try:
            id = json.dumps(i)
            if i in enlisted_id:
                continue
            enlisted_id.append(i)
            if len(enlisted_id) > 50 :
                enlisted_id= enlisted_id[30:]
            try:
                #work begins
                name,token,address,timestamp,type,price,img = parseObject(i)
                print(name,token,address,timestamp,type,price,img)
                try:
                    sendWebhookv2(name,token,address,timestamp,type,price,img)
                    #sendTwitter(name,token,address,timestamp,type,price,img)
                except:
                    print("error in sending webhook",name)
            except:
                print("Error in parsing one single object !!")
        except:
            print("Error in getting events")

        

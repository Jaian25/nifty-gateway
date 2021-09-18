import requests
import json

def get_events():
    lst = []
    url = 'https://api.niftygateway.com/market/all-data/'
    headers = {'Referer': 'https://niftygateway.com/', 'content-type': 'application/json',
        'pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Origin': 'https://niftygateway.com/'
        }
    payload = {"current":'1',"size":'30',"cancelToken":{"promise":{}},"timeout":'30000'}
    x = requests.post(url, headers=headers, json=payload)
    #print(x.text)
    jsonn = json.loads(x.text)
    #print(*jsonn['data']['meta']['page'],sep='\n')

    for i in reversed(jsonn['data']['results']):
        try:
            id = i['NiftyObject']['unmintedNiftyObjThatCreatedThis']['contractObj']['userWhoCreated_id']
            print(id)
            if str(id) == '9822':
                lst.append(i)
                #q = open(f'sample_result.json', 'w', encoding='utf-8')
                #json.dump(i, q, ensure_ascii=False, indent=4)
                #print(i['NiftyObject'])
        except:
            continue
    return lst



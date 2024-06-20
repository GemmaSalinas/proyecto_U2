import json 
import requests

def formar_json():
    dic_data={
    'switches':[
    {"model":'CAT3750',
     "model2" :'CAT3760'}],
    'routers':{'name':'CSR100V',
                'vendor':'cisco',
                'type':'hardware'
                }
    }

    dic_data2={
    'router':[
    {"model":'7206VXR',
     "so" :'Cisco IOS',
     "vendor" :'Cisco',
     "type" :'hardware' 
     }],
    'server1':[
    {'name':'server_Sergio',
     'service':'WEB',
     'remote_conection':'SSH',
     'linux distribution':'Mint'
                }],
    'server2':[
    {'name':'server_Gemma',
     'service1':'DNS',
     'service2':'WEB',
     'linux distribution':'Centos 8'
                }],
    'server3':[
    {'name':'server_Ana',
     'service1':'FTP',
     'service2':'DHCP',
     'linux distribution':'Centos 8'
                }]
    }

    print(json.dumps(dic_data2, indent=2, sort_keys=True))
    
    with open("./data/infraestructura.json", 'w') as file:
        json.dump(dic_data2,file,indent=4,sort_keys=True)

def get_api_ips():
    response = requests.get('http://ip-api.com/json/24.48.0.1')
    response2 = requests.get('http://ip-api.com/json/8.8.8.8?fields=61439')
    
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "X-Cisco-Meraki-API-Key": "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response3 = requests.request('GET', url, headers=headers, data = payload)




    #print(response3)
    with open("./data/apis_primera.json", 'w') as file:
        json.dump(response.json(),file,indent=4,sort_keys=True)
        json.dump(response2.json(),file,indent=4,sort_keys=True)
        
    with open("./data/apis_devnet.json", 'w') as file:
        json.dump(response3.json(),file,indent=4,sort_keys=True)
        json.dump(response4.json(),file,indent=4,sort_keys=True)


if __name__ == '__main__':
    #formar_json()
    get_api_ips()




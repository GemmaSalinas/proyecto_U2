import requests

requests.packages.urllib3.disable_warnings()

def get_ipdomain():
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type":"application/yang-data+json"
    }

    url = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/ip/domain/name/"
    response = requests.get(url, auth=('developer', 'C1sco12345'), headers=headers, verify=False)
    print(response.json())
    #print(response.status_code)

if __name__ == '_main_':
    get_ipdomain()
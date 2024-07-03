import requests
import json
requests.packages.urllib3.disable_warnings()

url = "https://192.168.56.104/restconf/data/ietf-interfaces:interfaces"

headers= {"Accept":"application/yang-data+json",
"Content-type":"application/yang-data+json"}

basicauth = ("cisco","cisco123!")

resp  = requests.get(url, auth=basicauth, headers=headers,verify=False)

#print(resp.json())


data = resp.json()
interface = data['ietf-interfaces:interfaces']['interface'][0]
ipv4 = interface.get('ietf-ip:ipv4', {}).get('address', [{}])[0]


table_data = [
    ['Name', interface['name']],
    ['Description', interface['description']],
    ['Type', interface['type']],
    ['Enabled', interface['enabled']],
    ['IPv4 Address', ipv4.get('ip', '')],
    ['Netmask', ipv4.get('netmask', '')]
]


field_width = 25
value_width = 30


def print_row(field, value):
    print(f'| {field:<{field_width}} | {value:<{value_width}} |')

border_line = f'+-{"-" * field_width}-+-{"-" * value_width}-+'
print(border_line)
for field, value in table_data:
    print_row(field, value)
    print(border_line)
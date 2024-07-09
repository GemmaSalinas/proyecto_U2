import json
import requests
requests.packages.urllib3.disable_warnings()

def get_interfaces():
    module="data/ietf-interfaces:interfaces"
    resp = requests.get(f'{api_url}{module}', auth=basicauth, headers=headers, verify=False)
    print(json.dumps(resp.json(), indent=4))
    data_json = resp.json()

    if resp.status_code==200:
        
        for key, valor in data_json.items():
            print(f'Nombre de la interface: {valor["interface"][:]['name']}')
            print(f'Descripción de la interface: {valor["interface"][:]['description']}')
            print(f'Status de la interface: {valor["interface"][:]['enabled']}')
    else:
        print(f'Error al realizar la consulta del modulo {module}') 
 
 
def get_restconf_native():
    module="data/Cisco-IOS-XE-native:native"
    resp=requests.get(f'{api_url}{module}',auth=basicauth,headers=headers, verify=False)
    if resp.status_code==200:
       print(json.dumps(resp.json(),indent=4))
    else:
      print(f'Error al consumir la API para el modulo {module}')   
      
def get_banner():
    module="data/Cisco-IOS-XE-native:native/banner/motd"  #atraves de la diagonal entro a un dato que está en raizzz
    resp=requests.get(f'{api_url}{module}',auth=basicauth,headers=headers, verify=False)
    if resp.status_code==200:
           print(json.dumps(resp.json(),indent=4))
    else:
      print(f'Error al consumir la API para el modulo {module}')   
      
def put_banner():
    banner={
    "Cisco-IOS-XE-native:motd": {
        "banner": "### Solo tienen permiso los privilegiados de piel blanca"
    }
}

    module="data/Cisco-IOS-XE-native:native/banner/motd"     
    resp=requests.put(f'{api_url}{module}',data=json.dumps(banner),auth=basicauth,headers=headers, verify=False)
    if resp.status_code==204:
        print("Actualización exitosa")
    else:
      print(f'Error, no se puede realizarla actualización al modulo')   
      
def post_loopback():
    dloopback = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback100",
    "description": "Configured by RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "172.16.100.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
})

    module="data/ietf-interfaces:interfaces"     
    resp=requests.post(f'{api_url}{module}',auth=basicauth,headers=headers,data=dloopback, verify=False)
    if resp.status_code==201:
        print(f'Se insertó correctamento {dloopback} ')
    else:
        print(f'Error al insertar elemento al módulo {module}')   
    #print(f'{api_url}{module}')
    #print(resp.status_code)
    #print(json.dumps(resp.json(),indent=4))
    
def del_loopback():
    module="data/ietf-interfaces:interfaces/interface=Loopback100" #para ir a un elemente le damos con igual y nombre del elemento
  
    dloopback = {}
    resp=requests.delete(f'{api_url}{module}',auth=basicauth,headers=headers,data=dloopback, verify=False)        
    if resp.status_code==204:
        print(f'Se eliminó correctamente')
    else:
        print(f'Error al eliminar')   
        #inteFACES GRAFICAS AMIGABLES QUE NOS PERMITAN ESTO, YA ESTA LOOPBACK YBANNER ENTONCEA AGREGARLE OTROS DOS ELEMENTO SDIFERENTES DE IOS CIE NATIVE
        #de forma colaborativo en equipo,el siguiente juevebes 
        
    #print(f'{api_url}{module}')
    #print(resp.status_code)
    #print(json.dumps(resp.json(),indent=4))
    
def vty_lines():
    module = "data/Cisco-IOS-XE-native:native/line/vty"
    vty = json.dumps({
        "Cisco-IOS-XE-native:vty": [
            {
                "first": 0,
                "last": 4,
                "login": {
                    "local": [None]
                },
                "password": {
                    "secret": "cisco123"
                },
                "transport": {
                    "input": {
                        "input": ["ssh"]
                    }
                }
            },
            {
                "first": 5,
                "last": 15,
                "login": {
                    "local": [None]
                },
                "password": {
                    "secret": "cisco456"
                },
                "transport": {
                    "input": {
                        "input": ["ssh"]
                    }
                }
            }
        ]
    })
    
    resp = requests.patch(f'{api_url}{module}', data=vty, auth=basicauth, headers=headers, verify=False)
    #print(resp.status_code)
            
    if resp.status_code == 204:
        print("Líneas VTY configuradas correctamente.")
    else:
        print(f'Error al configurar las líneas VTY')
        #print(resp.text)
   
   
   
    #resp=requests.get(f'{api_url}{module}',auth=basicauth,headers=headers, verify=False)
    
    #print(json.dumps(resp.json(),indent=4))  

def configure_dhcp_pool():
    module = "data/Cisco-IOS-XE-native:native/ip/dhcp"
    pool_config = json.dumps({
        "Cisco-IOS-XE-native:dhcp": {
            "Cisco-IOS-XE-dhcp:pool": [
                {
                    "id": "LAN",
                    "network": {
                        "primary-network": {
                            "number": "192.168.1.0",
                            "mask": "255.255.255.0"
                        }
                    },
                    "default-router": {
                        "default-router-list": ["192.168.1.1"]
                    },
                    "dns-server": {
                        "dns-server-list": ["8.8.8.8", "8.8.4.4"]
                    }
                }
            ]
        }
    })
   
    resp = requests.patch(f'{api_url}{module}', data=pool_config, auth=basicauth, headers=headers, verify=False)
    resp=requests.get(f'{api_url}{module}',auth=basicauth,headers=headers, verify=False)
    print(json.dumps(resp.json(), indent=4))  
    print(resp.status_code)
               
if __name__ == '__main__':
    #module:operations, data
    api_url = "https://192.168.56.104/restconf/"
    headers = {"Accept": "application/yang-data+json",
               "Content-type": "application/yang-data+json"
               }
    basicauth = ("cisco", "cisco123!")
    #get_interfaces()
    #get_restconf_native()
    #get_banner()
    #put_banner()
    #post_loopback()
    #del_loopback()
    #vty_lines()
    configure_dhcp_pool()

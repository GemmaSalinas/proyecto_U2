
#pip install lxml
import xml.etree.ElementTree as ET

def ejemplo():
    tree = ET.parse('./data/router.xml')
    raiz = tree.getroot()
    print (raiz)

    hostname = raiz.find('hostname').text
    print(f'El nombre del router es {hostname}')

    interfaces = raiz.find('interfaces')

    for interface in interfaces.findall('interface'):
        nombrei = interface.find('name').text   
        ip = interface.find('ip').text
        submask = interface.find('subnet').text
        print(f"Interface: {nombrei} \nip:{ip} \nMáscara de red: {submask}")
        
def infra():
    tree = ET.parse('./data/infraestructura.xml')
    raiz = tree.getroot()
    
    print('Información de la infraestructura:')
    router=raiz.find('router')
    print("\n---Router---")
    for device in router.findall('device'):
        model = device.find('model').text   
        so = device.find('so').text
        type = device.find('type').text
        vendor = device.find('vendor').text
        
        print(f"Modelo: {model} \nSO:{so} \nTipo: {type} \nVendedor: {vendor}")
    
    server1=raiz.find('server1')
    print("\n---Servidor 1---")
    for server in server1.findall('server'):
        linux_distribution = server.find('linux_distribution').text   
        name = server.find('name').text
        remote_connection = server.find('remote_connection').text
        service = server.find('service').text
        
        print(f"Distribución Linux: {linux_distribution} \nNombre:{name} \nConexión remota: {remote_connection} \nServicio: {service}")
   
    server2=raiz.find('server2')
    print("\n---Servidor 2---")
    for server in server2.findall('server'):
        linux_distribution = server.find('linux_distribution').text   
        name = server.find('name').text
        service1 = server.find('service1').text
        service2 = server.find('service2').text
        
        print(f"Distribución Linux: {linux_distribution} \nNombre:{name} \nServicio 1: {service1} \nServicio 2: {service2}")
   
    print("\n---Servidor 3---")
    server3=raiz.find('server3')
    for server in server3.findall('server'):
        linux_distribution = server.find('linux_distribution').text   
        name = server.find('name').text
        service1 = server.find('service1').text
        service2 = server.find('service2').text
        
        print(f"Distribución Linux: {linux_distribution} \nNombre:{name} \nServicio 1: {service1} \nServicio 2: {service2}")
   
if __name__ == '__main__':
    infra()

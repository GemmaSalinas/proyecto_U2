import napalm
from jinja2 import Environment, FileSystemLoader
import yaml

def connect_to_iosxr(hostname, username, password):
    # Obtiene el controlador de NAPALM para IOS XR
    driver_iosxr = napalm.get_network_driver("ios")
    
    # Parámetros adicionales para Netmiko
    optional_args = {
        'timeout': 120,
        'conn_timeout': 120,
        'banner_timeout': 200,
        'auth_timeout': 120,
        'session_log': 'session_log.txt',
        'global_delay_factor': 2
    }

    # Crea una instancia del dispositivo con las credenciales proporcionadas
    device = driver_iosxr(
        hostname=hostname,
        username=username,
        password=password,
        optional_args=optional_args
    )

    try:
        print(f"Connecting to {hostname} ...")
        # Abre la conexión con el dispositivo
        device.open()
        
        print("Getting device facts ...")
        # Obtiene los datos básicos del dispositivo
        device_facts = device.get_facts()
        print("Device facts:")
        print(device_facts)
        
        # Cargar configuración
        device.load_merge_candidate(filename=None, config=get_template_config(device_facts["vendor"]))
        print("\nDiff:")
        print(device.compare_config())
        
        # Preguntar al usuario si desea aplicar los cambios
        choice = input("\nWould you like to commit these changes? [yN]: ")
        if choice.lower() == "y":
            print("Committing ...")
            device.commit_config()
        else:
            print("Discarding ...")
            device.discard_config()
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Cierra la conexión con el dispositivo
        device.close()
        print("Connection closed.")

def get_template_config(vendor):
    # Cargar datos de configuración desde un archivo YAML
    config_data = yaml.load(open('proyecto3/Cisco_template.yml'), Loader=yaml.FullLoader)
    
    # Cargar la plantilla jinja2
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('proyecto3/Cisco_template.j2')
    
    # Renderizar y retornar la configuración
    rendered_config = template.render(config_data)
    print(rendered_config)
    return rendered_config

if __name__ == '__main__':
    # Datos del dispositivo
    hostname = "192.168.56.104"  # Cambia esto por la IP correcta de tu router IOS XR
    username = "cisco"
    password = "cisco123!"
    
    connect_to_iosxr(hostname, username, password)

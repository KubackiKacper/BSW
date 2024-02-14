from netmiko import ConnectHandler

# Informacje o urządzeniu Cisco
device_ip='192.168.0.13'
device = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': 'Cisco',
    'password': 'Cisco',
    'secret': 'Cisco',  # Jeśli jest wymagane hasło enable
}
print(device)

# Utwórz połączenie
connection = ConnectHandler(**device)

# Wejdź do trybu enable
connection.enable()

# Przykładowa konfiguracja
config_commands = [
    'configure terminal',
    'hostname dzialaj',
    'interface dot11Radio 0',
    'station-role root',
    'exit',
    'dot11 ssid NAME_OF_SSID',
    'guest-mode',
    'authentication open',
    'authentication key-management wpa version 2',
    'wpa-psk ascii Cisco123',
    'exit',
    'interface dot11Radio 0',
    'encryption mode ciphers aes-ccm',
    'ssid NAME_OF_SSID',
    'channel least-congested',
    'no shutdown',
    'exit'

]


output = connection.send_config_set(config_commands)

# Wyświetl wynik
print(output)

# Zamknij połączenie
connection.disconnect()

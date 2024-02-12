from netmiko import ConnectHandler

# Informacje o urządzeniu Cisco
device_ip='192.168.0.19'
device = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': 'cisco',
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
    'hostname repeater',
    'interface dot11Radio 0',
    'encryption mode ciphers aes-ccm',
    'ssid test_wlan',
    'exit',
    'station-role repeater',
    'exit',
    'dot11 ssid test_wlan',
    'guest-mode',
    'infrastructure-ssid',
    'authentication open',
    'authentication key-management wpa version 2',
    'wpa-psk ascii Cisco123',
    'exit',
    'interface bvI 1',
    'ip address 192.168.0.19 255.255.255.0',
    'no shutdown',
    'exit',
    'ip default-gateway 192.168.0.1',
    'interface dot11Radio 0',
    'no shutdown',
    'exit'

]


output = connection.send_config_set(config_commands)

# Wyświetl wynik
print(output)

# Zamknij połączenie
connection.disconnect()


config_commands = [
    'hostname repeater',
    'interface dot11Radio 0',
    'encryption mode ciphers aes-ccm',
    'ssid test_wlan',
    'exit',
    'station-role repeater',
    'exit',
    'dot11 ssid test_wlan',
    'guest-mode',
    'infrastructure-ssid',
    'authentication open',
    'authentication key-management wpa version 2',
    'wpa-psk ascii Cisco123',
    'exit',
    'interface bvI 1',
    'ip address 192.168.0.19 255.255.255.0',
    'no shutdown',
    'exit',
    'ip default-gateway 192.168.0.1',
    'interface dot11Radio 0',
    'no shutdown',
    'exit'

]
test = 'test'
config_commands.append(test)
print(config_commands)
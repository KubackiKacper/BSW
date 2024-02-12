global root_config_commands
    
root_config_commands = [
        'configure terminal',
        'interface dot11Radio 0',
        'station-role root',
        'exit',
        '',
        'guest-mode',
        'authentication open',
        'authentication key-management wpa version 2',
        '',
        'exit',
        'interface dot11Radio 0',
        'encryption mode ciphers aes-ccm',
        '',
        'channel least-congested',
        'no shutdown',
        'exit'
        ]
    
    test = 'test'
    root_config_commands.insert(2, test)

    with open(file_path1, 'w') as file1:
        for line in root_config_commands:
            file1.write(str(line) + '\n')
    with open(file_path2, 'w') as file2:
            file2.write("tu bedzie skrypt repeater.")

    
    file1.close()
    file2.close()
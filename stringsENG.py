select_language_string = "Select Language / Wybierz Język"
#*--------------------------------------------------------------------------------------------------------------------------------------------------
english_strings = {
    'next_button': "Next",
    'back_button': "Back",
    'dark_mode': "Dark Mode",
    'light_mode': "Light Mode",
    'start_str': "Start",
    'lbc_str': "Link Budget Calculator",
    'page1_str': """Location and 
File Name""",
    'page3_str': """Main Device 
Information""",
    'page4_str': """Subsidiary 
Device 
Information""",
    'page2_str': """Main Device 
Configuration""",
    'page5_str': """Subsidiary 
Device 
Configuration""",
    'page6_str': """File Transfer 
to Devices""",
    'page7_str': "End",

    'welcome_string': "Welcome to the configuration file editor for Cisco access points",

    'welcome_desc': """The application is designed to assist in preparing a ready-made script file containing commands to set various options for devices that make up a wireless bridge configuration.

You will be asked to provide information about specific settings to create a configuration that fully meets your requirements.

Before starting, make sure that both devices are connected to power and the home router.""",

    #!-----------------------------------------------------------
    'link_budget_label_str': "Link Budget Calculator (optional)",
    'Ptx_entry_str': "Pᵗˣ - Transmitter output power    [dBm]",
    'Gtx_entry_str': "Gᵗˣ - Transmitter antenna gain    [dBi]",
    'Ltx_entry_str': "Lᵗˣ - Transmitter losses    [dB]",
    'Lfs_entry_str': "Lᶠˢ - Free space losses    [dB]",
    'Lm_entry_str': "Lᵐ - Miscellaneous losses    [dB]",
    'Grx_entry_str': "Gʳˣ - Receiver antenna gain    [dBi]",
    'Lrx_entry_str': "Lʳˣ - Receiver losses    [dB]",
    'wrong_value_entered_str': """The character entered is not allowed, please try again.
The decimal separator for numbers is '.'""",
    'not_all_values_entered_str': "Not all values have been provided, please try again",
    'distance_str': "Distance in meters",
    'frequency_str': "Frequency in MHz",
    'lfs_tg_str': "Gtx - Transmitter antenna gain in dB",
    'lfs_rg_str': "Grx - Receiver antenna gain in dBi",
    'link_budget_help_str': """What is a link budget calculator?

A link budget is an analysis and balance of power in a communication system. This term is used to consider the power received by the receiver. It includes all signal gains and losses until it is received by the receiver. Factors such as losses due to the use of cables, fibers, and other Tx/Rx chain elements, antenna gains, amplifiers, etc., as well as propagation losses during the transmission of the signal through the air or other medium, are taken into account.

The general equation for the link budget calculator is: Received Power (dBm) = Transmitted Power (dBm) + Gain (dB) - Losses (dB)

It is more specifically described in the diagram below:
""",
    'link_budget_help_str2': """
where:
T - Transmitter,
R - Receiver,

From the above diagram, the derived equation is : Pʳˣ = Pᵗˣ + Gᵗˣ - Lᵗˣ - Lᶠˢ - Lᵐ + Gʳˣ - Lʳˣ
where:
Pᵗˣ - Transmitter output power [dBm],
Gᵗˣ - Transmitter antenna gain [dBi],
Lᵗˣ - Transmitter losses - signal power losses in the transmitter itself and its components, such as cables and connectors used for connecting the transmitting antenna [dBi],
Lᶠˢ - Free space losses, that are dependend on frequency and distance [dB],
Lᵐ - Miscellaneous losses, including signal attenuation through obstacles, impact of atmospheric conditions [dB],
Gʳˣ - Receiver antenna gain [dBi],
Lʳˣ - Receiver losses - signal power losses in the receiver and its components, such as cables and connectors used for connecting the receiving antenna [dB],
""",
    #! PAGE 1------------------------------------------------------
    'file_name_lbl_str': "Enter the name for the configuration file",
    'no_null_file_name': "The file name cannot be empty",
    'correct_file_name': "The entered file name is correct",
    'incorrect_file_name': "The character you are trying to enter is not allowed",
    'select_path_button': "Select path",
    'help_button': "Help",
    'path_entry_lbl_str': "Choose the location to create the file",
    'result_lbl': "Result",
    'calculate_button_str': "Calculate",
    'reset_button_str': "Reset",

    'help_lbl_str': """The file name determines what the configuration file, prepared after completing all the steps of the application, will be called. The file name can consist of lowercase and uppercase letters, numbers, and the '_' character. Two configuration files will be created: one for the main device (root) and one for the subsidiary device (repeater).""",

    'help2_lbl_str': """The file path specifies where the finished files will be saved. The default path for files is the path displayed in the selection field. If you do not use the path selection, the files will be created in the default location.""",

    "filename_placeholder": "Enter the file name",

    "warning_filename_str": """The file name is empty, please enter a valid file name.

The file name can consist of lowercase and uppercase letters, numbers, and the '_' character.""",
    #! PAGE 2------------------------------------------------------------
    'page2_lbl_str': "Main Device Configuration",
    'ssid_lbl_str': "Enter the SSID to be used for the network after configuration",
    'password_lbl_str': "Enter the password to secure the network (WPA2)",
    'root_ip_lbl_str': "Enter the target IP address for the device after configuration",

    'ssid_good': "The entered network name is correct",
    'ssid_null': "The network name cannot be empty",
    'ssid_incorrect_character': "The character you are trying to enter is not allowed",
    'ssid_too_much_char': "The network name cannot exceed 32 characters",

    'password_null': "The password cannot be empty",
    'password_characters_min': "The password must have at least 8 characters",
    'password_characters_max':"The password can contain 63 characters maximum",
    'password_good': "The entered password is correct",
    'password_invalid': "The entered password is invalid",
    'password_digit': "The password must contain at least one digit 0-9",
    'password_letter': "The password must contain at least one uppercase letter [A-Z]",

    'ip_incorrect_character': "The character you are trying to enter is not allowed",
    'ip_null': "The IP address cannot be empty",
    'ip_ok': "The entered character is correct",
    'ip_morethan15': "The IP address cannot have more than 15 characters",
    'ip_moredots': "You cannot enter this character",
    # !----------------------------------------------------------------------------------------------
    'bridge_type_lbl': "Choose the desired type of wireless bridge",
    'wifi_bridge_str': "Wi-Fi Bridge",
    'wap_str': "Wireless Access Point",
    'ip_start': "Enter the initial IP address of the device before configuration",
    'username_start_str': "Enter the username for the device",
    'username_ok': "The entered username is correct",
    'username_bad': "The character you are trying to enter is not allowed",
    'username_null': "The username cannot be empty",

    'password_start_lbl_str': "Enter the password for the device",
    'password_start_null': "The password cannot be empty",
    'password_start_ok': "The entered password is correct",
    'password_start_bad': """The character you are 
trying to enter is not allowed""",

    'button_root_show': "Show",
    'button_root_hide': "Hide",

    'password_secret_start_lbl_str': "Enter the secret password (optional)",
    'password_secret_start_null': "The password cannot be empty",
    'password_secret_start_ok': "The entered password is correct",
    'password_secret_start_bad': """The character you are 
trying to enter is not allowed""",

    'page3_invalid_str': """The provided values do not meet the criteria or are empty, please try again.
The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255""",

    'page4_invalid_str': """The provided values do not meet the criteria or are empty, please try again.
The subsidiary device IP address cannot be the same as the main device IP address.
The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255""",

    'page5_default_lbl': "Configuration for the subsidiary device",
    'ipaddr_nonroot_lbl': "Enter the target IP address for the subsidiary device after configuration",
    'ipaddr_dg_nonroot_lbl': "Enter the default gateway IP address for the home router",
    'page6_default_lbl': "File Transfer to Devices",

    'page3_help_str': """The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255

The username and password for the device are the login credentials for an authorized user to configure the device. The default values for the username are 'cisco' and for the password 'Cisco'.
The 'secret' password is used if the device requires a password to enter privileged mode. The default value for the 'secret' password is 'Cisco'. If your device does not require a password to enter privileged mode, you can leave the field blank.

The application can generate 2 types of scripts, depending on the selected checkbox. If the checkbox is unchecked, the last selected option will be remembered.
The 'Wi-Fi Bridge' configuration allows for broadcasting a Wi-Fi network. With this configuration, you will be able to connect to a wireless network (WLAN) using devices such as a laptop or phone.""",
    'page3_help_str1':"""
The 'Wireless Access Point' configuration allows for a direct connection to the device using the 'GigabitEthernet' port and an RJ-45 cable. If you choose this configuration, you will be able to connect the device to a switch to create a LAN, but you will not be able to connect to a Wi-Fi network.
""",

    'page4_help_str': """The subsidiary device IP address cannot be the same as the main device IP address.

The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255

The username and password for the device are the login credentials for an authorized user to configure the device. The default values for the username are 'cisco' and for the password 'Cisco'.
The 'secret' password is used if the device requires a password to enter privileged mode. The default value for the 'secret' password is 'Cisco'. If your device does not require a password to enter privileged mode, you can leave the field blank.""",

    'page2_help_str': """SSID (Service Set Identifier) is the unique name that identifies a wireless local area network (WLAN).

The password used to secure the network must meet the WPA2 encryption format requirements. To meet the password requirements, it must:
- Have at least 8 characters,
- Have at least one uppercase letter [A-Z],
- Have at least one digit 0-9,
- Can use special characters such as '!', '@', '#' etc.

IP adresses cannot be the same.
The target IP address, as the name suggests, specifies what IP address the device should assume after configuration.
The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255

The subnet mask is a numerical identifier that specifies which bits in the IP address are assigned to network identification and which are assigned to host identification in that network. The subnet mask is used in conjunction with an IP address to determine which network a given IP address belongs to.
The default subnet mask is 255.255.255.0, or in short /24 (24-bit), which provides 256 possible host addresses in one subnet.
If you are interested in choosing a different subnet mask, expand the list with the available masks:
- 255.255.255.128 (/25) - Offers 128 possible host addresses,
- 255.255.255.192 (/26) - Offers 64 possible host addresses,
- 255.255.255.224 (/27) - Offers 32 possible host addresses,
- 255.255.255.240 (/28) - Offers 16 possible host addresses,
- 255.255.255.248 (/29) - Offers 8 possible host addresses,
- 255.255.255.252 (/30) - Offers 4 possible host addresses.
""",
    'page2_ivalid_values_str': """The provided values do not meet the criteria or are empty, please try again.
The password used to secure the network must meet the WPA2 encryption format requirements. To meet the password requirements, it must:
- Have at least 8 characters,
- Have at least one uppercase letter [A-Z],
- Have at least one digit 0-9,
- Can use special characters such as '!', '@', '#' etc.
configuration

IP addresses cannot be the same.
The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255""",

    'page5_ivalid_values_str': """The provided values do not meet the criteria or are empty, please try again.

The IP address cannot be the same.

The IP address must meet the following conditions:
Class A: 0.0.0.0-127.255.255.255, or
Class B: 128.0.0.0 - 191.255.255.255, or
Class C: 192.0.0.0 - 223.255.255.255""",

    'send1_lbl_str': "File transfer to the device has been successful. Connect the console cable to the second device and click the button to send the file to the second device.",
    'send2_lbl_str':"File transfer to the device has been successful. You can unplug the console cable from the device and redirect to the next page.",
    'send1_error_lbl_str': "File transfer to the device has failed. Check if the entered IP address and authentication credentials are correct.",
    'final_step_lbl_str': """Creation of configuration files was successful. The final step in the configuration is to transfer them to the devices. Establish a connection to the device using the console port and a client that supports network protocols, such as PuTTy. Below are two buttons: one for sending the file to the main device and one for sending the file to the subsidiary device. After clicking first button please wait for few seconds, the aplication will try to send configuration file to the device. Second button is hidden until you will press first button. Verify that the provided information is correct. If you notice any errors in the information, go back to the previous steps and change the configuration values.
Initial and target values for the main device:""",
    'ip_last_page': "Initial IP",
    'username_last_page': "Username",
    'password_last_page': "Password",
    'password_en_last_page': "Password (secret)",

    'ip2_last_page': "Target IP",
    'ip3_last_page':"Target IP interface G0",
    'ssid_last_page': "Network Name",
    'password2_last_page': "Network Password",

    'values_non_root_last_page': "Initial and target values for the subsidiary device:",
    'ip_dg_last_page': "Default Gateway IP",
    'last_page_passwords_show': "Show passwords",
    'last_page_passwords_hide': "Hide passwords",
    'send_to_root_button_text': "Send file to main device",
    'send_to_non_root_button_text': "Send file to subsidiary device",
    'end_lbl': "Thank you for using the script file configuration application for wireless bridges. I hope the application met your expectations and you are satisfied the configuration process.",
    'end': "End",
    
    'devices_btn_str': "Device Selection",
    'devices_str1': """When selecting devices for configuring a wireless bridge, several factors should be taken into consideration. Firstly, determine whether the device requires external antennas for connection and whether the Effective Isotropic Radiated Power (EIRP) - the radio signal power transmitted by the antenna in a specific direction, will not be exceeded.

If your configuration is within the same building, there is no need to purchase external antennas. An appropriate device meeting your requirements is the Cisco AIR-SAP1602I-E-K9. The cost of one device is approximately 158 PLN / unit. If you do not have a switch supporting Power over Ethernet (PoE) technology, it is necessary to purchase an external power supply for the devices, such as the Cisco AD10048P3. The cost of one power supply is around 40 PLN / unit.

If your configuration needs to provide a connection up to 1 kilometer away, the device that will provide the connection is the Cisco AIR-SAP1602E-E-K9, a wireless access point with external antennas. The cost of one device is around 1200 PLN / unit. If you do not have a switch supporting Power over Ethernet (PoE) technology, it is necessary to purchase an external power supply for the devices, such as the Cisco AD10048P3. The cost of one power supply is around 40 PLN / unit.

If your configuration needs to provide a connection farther than 1 kilometer away, you will need to purchase the Cisco AIR-SAP1602E-E-K9 device and an external antenna that will strengthen the signal in order to allow the devices to connect. There are many antennas compatible with the device, and below are some suggestions for individual devices:
- Directional antennas:
    - Cisco Aironet AIR-ANT2410Y-R, antenna gain for 2.4 GHz frequency = 10 dBi, cost approximately 865 PLN / unit,
    - Cisco Aironet AIR-ANT5160NP-R, antenna gain for 2.4 GHz frequency = 6 dBi, cost approximately 800 PLN / unit,
- Sector antennas (increasing range in a specific direction):
    - Cisco Aironet AIR-ANT2460NP-R, antenna gain for 2.4 GHz frequency = 6 dBi, cost approximately 300 PLN / unit,
- Panel antennas:
    - Cisco Aironet AIR-ANT2547VG-N, antenna gain for 2.4 GHz frequency = 7 dBi, cost approximately 300 PLN / unit,

These are just a few suggestions regarding external antennas for the device. The most important factor indicating whether a specific antenna can be used in the configuration is the EIRP indicator. The EIRP value is calculated based on the power transmitted by the antenna (in dBm) and the antenna gain (in dBi). This is particularly important in the case of regulations and standards concerning radio signal power, as EIRP takes into account both the power transmitted by the transmitter and the antenna gain, allowing for a better determination of the actual range and potential impact of the signal on the environment. In Poland, for the 2.4 GHz band, the maximum EIRP value is 20 dBm. If this value is exceeded, it is possible to adjust the transmit power and receiver sensitivity, but this is not recommended as it may affect the quality of the connection. Below is a calculator to help calculate EIRP. The default power for the proposed devices is 22 dBm; the cable attenuation may depend on the length, type, and construction of the cable.
General equation for calculating the EIRP value:
Transmitter power + Antenna gain - Cable attenuation * Cable length
""",
    'eirp_power': "Device Power [dBm]",
    'eirp_cable': "Cable Loss [db/m]",
    'eirp_lencable': "Cable Length [m]",
    'eirp_antenna': "Antenna Gain [dBi]",

    'root2_ip_lbl_str': "Enter the destination IP address of the Gigabitethernet port after configuration completion.",
    'nonroot2_ip_lbl_str': "Enter the destination IP address of the Gigabitethernet port after configuration completion."
}



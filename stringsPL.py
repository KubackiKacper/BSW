select_language_string = "Select Language / Wybierz Język"
#*--------------------------------------------------------------------------------------------------------------------------------------------------
polish_strings = {
    'next_button':"Dalej",
    'back_button':"Wstecz",
    'dark_mode':"Tryb Ciemny",
    'light_mode':"Tryb Jasny",
    'start_str':"Start",
    'lbc_str':"Budżet Łącza",
    'page1_str':"""Lokalizacja i 
nazwa plików""", 
    'page3_str':"""Infromacje dla 
urządzenia głównego""",
    'page4_str':"""Informacje 
dla urządzenia
podrzędnego""",
    'page2_str':"""Konfiguracja dla
urządzenia głównego""",
    'page5_str':"""Konfiguracja
dla urządzenia
podrzędnego""",
    'page6_str':"""Przesyłanie plików
do urządzeń""",
    'page7_str':"Koniec",

    'welcome_string':"""Witaj w edytorze ustawień plików konfiguracyjnych dla 
punktów dostępowych firmy Cisco""",

    'welcome_desc':"""Aplikacja ma na celu pomoc w przygotowaniu gotowego pliku skryptowego zawierającego komendy ustawiające poszczególne opcje dla urządzeń, składających się na konfigurację mostu bezprzewodowego.

Zostaniesz poproszony o udzielenie informacji na temat konkretnych ustawień, w celu utworzenia konfiguracji, w pełni spełniającej twoje wymagania.

Przed rozpoczęciem upewnij się, że obydwa urządzenia są podpięte do zasilania oraz rutera domowego""",
#!-----------------------------------------------------------
    'link_budget_label_str':"Kalkulator budżetu łącza (opcjonalne)",
    'Ptx_entry_str':"Pᵗˣ - Wyjściowa moc nadajnika w dBm",
    'Gtx_entry_str':"Gᵗˣ - Zysk anteny nadajnika w dB",
    'Ltx_entry_str':"Lᵗˣ - Straty nadajnika w dBi",
    'Lfs_entry_str':"Lᶠˢ - Straty w wolnej przestrzeni w dB",
    'Lm_entry_str':"Lᵐ - Różne straty w dB",
    'Grx_entry_str':"Gʳˣ - Zysk anteny odbiornika w dB",
    'Lrx_entry_str':"Lʳˣ - Straty z odbiornika w dB",
    'wrong_value_entered_str':"""Wprowadzony znak jest niedozwolony, spróbuj ponownie
Separatorem dziesiętym dla liczb jest ' . ' """,
    'not_all_values_entered_str':"Nie wszystkie wartości zostały podane, spróbuj ponownie",
    'distance_str':"Dystans w M",
    'frequency_str':"Częstotliwość w GHz",
    'lfs_tg_str':"Gᵗˣ - Zysk anteny nadajnika w dB",
    'lfs_rg_str':"Gʳˣ - Zysk anteny odbiornika w dBi",
    'link_budget_help_str':"""Czym jest kalkulator budżetu łącza?
    
Budżet łącza to analiza i bilans mocy w systemie łączności. Termin ten używany jest do uwzględniania mocy odbieranej przez odbiornik. Obejmuje on wszystkie zyski oraz straty sygnału, dopóki nie zostanie on odebrany przez odbiornik. Uwzględniane są czynniki takie jak straty z powodu użycia kabli, włókien i innych elementów łańcucha Tx/Rx, zyski anteny, wzmacniaczy itp., oraz straty propagacyjne podczas podróży nadanego sygnału przez powietrze lub inne medium.

Ogólne równanie dla kalkulatora budżetu łącza to: Moc Odbierna(dBm) = Moc Nadawcza(dBm) + Zysi(dB) - Straty(dB) 

Bardziej szczegółowo opisuje to schemat poniżej:
""",
    'link_budget_help_str2':"""
Z czego wynika równanie: Pʳˣ = Pᵗˣ + Gᵗˣ - Lᵗˣ - Lᶠˢ - Lᵐ + Gʳˣ - Lʳˣ
gdzie,
T - transmiter,
R - odbiornik,
Pᵗˣ - Wyjściowa moc nadajnika w dBm
Gᵗˣ - Zysk anteny nadajnika w dB
Lᵗˣ - Straty nadajnika w dBi
Lᶠˢ - Straty w wolnej przestrzeni w dB
Lᵐ  - Różne straty w dB
Gʳˣ - Zysk anteny odbiornika w dB
Lʳˣ - Straty z odbiornika w dB
""",
#! PAGE 1------------------------------------------------------
    'file_name_lbl_str':"""Podaj nazwę, jaką ma przyjąć plik konfiguracyjny""",
    'no_null_file_name':"Nazwa pliku nie może być pusta",
    'correct_file_name':"Wprowadzona nazwa pliku jest poprawna",
    'incorrect_file_name':"Znak, który próbujesz wprowadzić jest niedozwolony",
    'select_path_button':"Wybierz ścieżke",
    'help_button':"Pomoc",
    'path_entry_lbl_str':"Wybierz lokalizację utworzenia pliku",
    'result_lbl':"Wynik",
    'calculate_button_str':"Oblicz",
    'reset_button_str':"Reset",
    
    
    'help_lbl_str':"Nazwa pliku określa, jak ma nazywać się plik konfiguracyjny, który zostanie przygotowany po przejściu przez wszystkie kroki aplikacji. Nazwa pliku może się składać z małych oraz dużych liter, cyfr i znaku '_'. Zostaną utworzone dwa pliki konfiguracyjne: jeden dla urządzenia głównego (root) oraz jeden dla urządzenia podrzędnego (repeater) ",

    'help2_lbl_str':"Ścieżka pliku określa, gdzie zostaną zapisane gotowe pliki. Domyślną scieżką dla plików jest ścieżka widoczna w polu wyboru. Jeżeli nie skorzystasz z wyboru ścieżki pliki zostaną utworzone w lokacji domyślnej.",

    "filename_placeholder":"Wprowadź nazwę pliku",
    
    "warning_filename_str":"""Nazwa pliku jest pusta, wprowadź poprawną nazwę pliku

Nazwa pliku może się składać z małych oraz dużych liter, cyfr i znaku '_'""",
#! PAGE 2------------------------------------------------------------
    'page2_lbl_str':"Konfiguracja dla głównego urządzenia",
    'ssid_lbl_str':"Podaj SSID, które ma przyjąć sieć, po ukończeniu konfiguracji", #!!!!!!!
    'password_lbl_str':"Podaj hasło, którym ma być zabezpieczona sieć (WPA2) ",#!!!!!!!
    'root_ip_lbl_str':"Podaj docelowy adres IP urządzenia, po ukończeniu konfiguracji",#!!!!!!!
    

    'ssid_good':"Wprowadzona nazwa sieci jest poprawna",
    'ssid_null':"Nazwa sieci nie może być pusta",
    'ssid_incorrect_character':"Znak, który próbujesz wprowadzić jest niedozowolony",
    'ssid_too_much_char':"Nazwa sieci nie może przekraczać 32 znaków",

    'password_null': "Hasło nie może być puste",
    'password_characters_min':"Hasło nie może mieć mniej niż 8 znaków",
    'password_characters_max':"Hasło nie może przekraczać 63 znaków",
    'password_good':"Wprowadzone hasło jest poprawne",
    'password_invalid':"Wprowadzone hasło jest niepoprawne",
    'password_digit':"Hasło musi zawierać conajmniej jedną liczbę 0-9",
    'password_letter':"Haso musi zawierać conajmniej jedną dużą literę [A-Z]",
    
    'ip_incorrect_character':"Znak, który próbujesz wprowadzić jest niedozowolony",
    'ip_null':"Adres IP nie może być pusty",
    'ip_ok':"Wprowadzony znak jest poprawny",
    'ip_morethan15':"Adres IP nie może mieć więcej niż 15 znaków",
    'ip_moredots':"Nie możesz juz wprowadzić tego znaku",
#!----------------------------------------------------------------------------------------------
    'bridge_type_lbl':"Wybierz oczekiwany rodzaj mostu bezprzewodowego",
    'wifi_bridge_str':"Most Wi-Fi",
    'wap_str':"Bezprzewodowy punkt dostępowy",
    'ip_start':"Podaj adres IP urządzenia, przed rozpoczęciem konfiguracji",#!!!!!!!
    'username_start_str':"Podaj nazwę użytkownika dla urządzenia",
    'username_ok':"Wprowadzona nazwa użytkownika jest poprawna",
    'username_bad':"Wprowadzony znak jest niedozwolony",
    'username_null':"Nazwa użytkownika nie może byc pusta",
    
    'password_start_lbl_str':"Podaj hasło dla urządzenia",
    'password_start_null':"Hasło nie może być puste",
    'password_start_ok':"Wprowadzone hasło jest poprawne",
    'password_start_bad':"""Wprowadzony znak 
jest niedozwolony""",
    'button_root_show':"Pokaż",
    'button_root_hide':"Ukryj",
    
    'password_secret_start_lbl_str':"Podaj hasło secret(opcjonalne)",
    'password_secret_start_null':"Hasło nie może być puste",
    'password_secret_start_ok':"Wprowadzone hasło jest poprawne",
    'password_secret_start_bad':"""Wprowadzony znak 
jest niedozwolony""",
    'page3_invalid_str':"""Podane wartości nie spełniają kryteriów lub są puste, spróbuj ponownie.
Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255""",

    'page4_invalid_str':"""Podane wartości nie spełniają kryteriów lub są puste, spróbuj ponownie.
Adres IP urządzenia podrzędnego nie może być taki sam jak adres IP urządzenia głównego.
Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255""",
    
    'page5_default_lbl':"Konfiguracja dla urządzenia podrzędnego",
    'ipaddr_nonroot_lbl':"Podaj docelowy adres IP dla urządzenia podrzędnego, po ukończeniu konfiguracji",
    'ipaddr_dg_nonroot_lbl':"Podaj bramę domyślną sieci dla rutera domowego",
    'page6_default_lbl':"Przesyłanie plików do urządzeń",

    'page3_help_str':"""Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255

Nazwa użytkownika oraz hasło dla urządzenia to dane do logowania dla autoryzowanego użytkownika w celu możliwości konfiguracji urządzenia. Domyślnymi wartościami dla nazwy użytkownika jest: 'cisco', a dla hasła 'Cisco'.
Hasło 'secret' to hasło wykorzystywane, jeżeli do przejscia w tryb uprzywilejowany urządzenie wymaga podania hasła. Domyślna wartość dla hasła secret to 'Cisco', jeżeli twoje urządzenie nie wymaga podawania hasła do przejścia w tryb uprzywilejowany, możesz pozostawić pole jako puste.
Aplikacja jest w stanie wygenerować 2 rodzaje skryptów, w zależności od zaznaczonego pola wyboru. W przypadku odznaczenia pola wyboru, zostanie zapamiętana ostatnia wybrana opcja.
 
Konfiguracja 'Most Wi-Fi' umożliwia rozgłaszanie sieci Wi-Fi . Dzięki tej konfiguracji będziesz w stanie połączyć się z siecią bezprzewodową (WLAN) za pomocą urządzeń takich jak laptop czy telefon.
""",
    'page3_help_str1':"""
Konfiguracja 'Bezprzewodowy punkt dostępowy' umożliwia bezpośrednie połączenie z urządzeniem za pomocą portu 'GigabitEthernet' oraz kabla RJ-45. W przypadku wyboru tej konfiguracji, będziesz mógł podpiąć urządzenie do przełącznika w celu utworzenia sieci LAN, natomiast nie będziesz mógł połączyć się z siecią Wi-Fi.
""",
    'page4_help_str':"""Adres IP urządzenia podrzędnego nie może być taki sam jak urządzenia głównego.

Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255

Nazwa użytkownika oraz hasło dla urządzenia to dane do logowania dla autoryzowanego użytkownika w celu możliwości konfiguracji urządzenia. Domyślnymi wartościami dla nazwy użytkownika jest: 'cisco', a dla hasła 'Cisco'.
Hasło 'secret' to hasło wykorzystywane, jeżeli do przejscia w tryb uprzywilejowany urządzenie wymaga podania hasła. Domyślna wartość dla hasła secret to 'Cisco', jeżeli twoje urządzenie nie wymaga podawania hasła do przejścia w tryb uprzywilejowany, możesz pozostawić pole jako puste.""",

    'page2_help_str':"""SSID (Service Set Identifier) to inaczej unikalna nazwa, która identyfikuje bezprzewodową sieć lokalną (WLAN).

Hasło, którym ma być zabezpieczona sieć musi spełniać warunki formatu szyfrowania WPA2. Aby spełnić warunki hasła musi ono miec:
-Conajmniej 8 znaków,
-Conajmniej jedną dużą literę,
-Conajmniej jedną cyfrę,
-Można użyć znaku specjalnego takiego jak '!', '@', '#' itp.

Adresy IP nie mogą być takie same.
Docelowy adres IP jak sama nazwa wskazuje, określa jaki adres IP ma przyjąć urządzenie po zakończeniu konfiguracji.
Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255

Maska podsieci to liczbowy identyfikator, który określa, które bity w adresie IP są przypisane do identyfikacji sieci, a które do identyfikacji hostów w tej sieci. Maska podsieci jest używana w połączeniu z adresem IP, aby określić, do której sieci należy dany adres IP.
Domyślną maską podsieci jest maska 255.255.255.0 lub w skrócie /24 (24-bitowa), która oferuje 256 możliwych adresów hostów w jednej podsieci.
Jeżeli interesuje cię wybór innej maski podsieci, rozwiń listę z dostępnymi maskami:
-255.255.255.128 (/25) - Oferuje 128 możliwych adresów hostów,
-255.255.255.192 (/26) - Oferuje 64 możliwe adresy hostów,
-255.255.255.224 (/27) - Oferuje 32 możliwe adresy hostów,
-255.255.255.240 (/28) - Oferuje 16 możliwych adresów hostów,
-255.255.255.248 (/29) - Oferuje 8 możliwych adresów hostów,
-255.255.255.252 (/30) - Oferuje 4 możliwe adresy hostów.
""",
    'page2_ivalid_values_str':"""Podane wartości nie spełniają kryteriów lub są puste, spróbuj ponownie.
Hasło, którym ma być zabezpieczona sieć musi spełniać warunki formatu szyfrowania WPA2. Aby spełnić warunki hasła musi ono miec:
-Conajmniej 8 znaków,
-Conajmniej jedną dużą literę,
-Conajmniej jedną cyfrę,
-Można użyć znaku specjalnego takiego jak '!', '@', '#' itp.

Adresy IP nie mogą być takie same.
Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255""",

    'page5_ivalid_values_str':"""Podane wartości nie spełniają kryteriów lub są puste, spróbuj ponownie.

Adresy IP nie mogą być sobie równe.

Adres IP musi spełniać następujące warunki:
Klasa A: 0.0.0.0-127.255.255.255, lub
Klasa B: 128.0.0.0 - 191.255.255.255, lub
Klasa C: 192.0.0.0 - 223.255.255.255""",

    'send1_lbl_str':"Przesył pliku do urządzenia zakończył się sukcesem, przepnij kabel konsolowy do drugiego urządzenia i kliknij w przycisk odpowiadający za przesył pliku do drugiego urządzenia",
    'send2_lbl_str':"Przesył pliku do urządzenia zakończył się sukcesem. Możesz odłączyć kabel od urządzenia i przejść do następnego kroku.",
    'send1_error_lbl_str':"Przesyłanie pliku do urządzenia nie powiodło się, sprawdź czy podany adres IP oraz dane uwierzytelniające są poprawne ",
    'final_step_lbl_str':"""Pliki konfiguracyjne zostały pomyślnie utworzone. Ostatnim krokiem w konfiguracji jest przesłanie ich do urządzeń. Nawiąż połączenie z urządzeniem za pomocą portu konsolowego oraz klienta obsługującego protokoły sieciowe np. PuTTy. Poniżej znajdują się dwa przyciski: Jeden służący do wysłania pliku do urządzenia głównego, drugi do urządzenia podrzędnego. Po kliknięciu w przycisk odczekaj chwile, aplikacja podejmie próbe wysyłki pliku do urządzenia. Drugi przycisk zostanie ukazany po kliknięciu pierwszego. Zweryfikuj czy podane informacje są poprawne, jeżeli zauważyłeś w nich jakiś błąd, wróć do poprzednich kroków i zmień wartości dla konfiguracji.
Wartości początkowe oraz docelowe dla urządzenia głównego: """,
    'ip_last_page':"IP początkowe",
    'username_last_page':"Nazwa użytkownika",
    'password_last_page':"Hasło",
    'password_en_last_page':"Hasło (secret)",
    
    'ip2_last_page':"IP docelowe",
    'ip3_last_page':"IP port G0 docelowe",
    'ssid_last_page':"Nazwa sieci",
    'password2_last_page':"Hasło do sieci",
    
    'values_non_root_last_page':"Wartości początkowe oraz docelowe dla urządzenia podrzędnego:",
    'ip_dg_last_page':"IP bramy domyślnej",
    'last_page_passwords_show':"Pokaż hasła",
    'last_page_passwords_hide':"Ukryj hasła",
    'send_to_root_button_text':"Prześlij plik do urządzenia głównego",
    'send_to_non_root_button_text':"Prześlij plik do urządzenia podrzędnego",
    'end_lbl':"Dziękuje za skorzystanie z aplikacji do konfiguracji plików skryptowych dla mostów bezprzewodowych. Mam nadzieję, że aplikacja spełniła Twoje oczekiwania i ułatwiła proces konfiguracji.",
    'end':"Zakończ",
    'devices_btn_str':"Dobór urządzeń",
    'devices_str1':"""Przy doborze urządzeń do konfiguracji mostu bezprzewodowego należy wziąć pod uwage kilka kwestii. Po pierwsze, czy urządzenie wymaga dołączenia zewnętrznych anten w celu zapewnienia połączenia oraz czy wskaźnik  efektywnej izotropowej mocy promieniowania (EIRP), czyli moc sygnału radiowego transmitowanego przez antene w określonym kierunku nie zostanie przekroczony.

Jeżeli twoja konfiugracja ma mieć miejsce w tym samym budynku, nie ma potrzeby zaopatrzania się w zewnętrzne anteny, a urządzeniem, które spełni twoje oczekiwania jest Cisco AIR-SAP1602I-E-K9. Koszt jednego urządzenia to około 158zł / szt. Jeżeli nie posiadasz przełącznika obsługującego technologie Power over Ehternet (PoE), konieczne jest zaopatrzenie się w zewnętrzny zasilacz do urządzeń, np Cisco AD10048P3. Koszt jednego zasilacza to około 40 zł / sztuka.

Jeżeli twoja konfiguracja ma zapewnić połączenie w miejscu oddalonym maksymalnie o 1 kilometr, urządzeniem które zapewni połączenie jest Cisco AIR-SAP1602E-E-K9, czyli punkt dostępowy z zewnęnrznymi antenami. Koszt jednego urządzenia to około 1200zł / szt. Jeżeli nie posiadasz przełącznika obsługującego technologie Power over Ehternet (PoE), konieczne jest zaopatrzenie się w zewnętrzny zasilacz do urządzeń, np Cisco AD10048P3. Koszt jednego zasilacza to około 40 zł / sztuka.

Jeżeli twoja konfiguracja ma zapewnić połączenie w miejscu oddalonym dalej niż 1 kilometr, niezbędne będzie zaopatrzenie się w urządzenie Cisco AIR-SAP1602E-E-K9 oraz zewnętrzną antene, której zasięg zapewni możliwość połączenia się ze sobą urządzeń. Jest wiele anten, które są kompatybilne z urządzeniem, poniżej znajdują się propozycje poszczególnych urządzeń:
-Anteny kierunkowe:
    -Cisco Aironet AIR-ANT2410Y-R, zysk anteny dla częstotliwości 2.4 gHz = 10 dBi, koszt około 865zł / szt,
    -Cisco Aironet AIR-ANT5160NP-R, zysk anteny dla częstotliwości 2.4 gHz = 6 dBi, koszt około 800zł / szt,
-Anteny sektorowe (zwiększające zasięg w określonym kierunku):
    -Cisco Aironet AIR-ANT2460NP-R, zysk anteny dla częstotliwości 2.4 gHz = 6 dBi, koszt około 300zł / szt,
-Anteny panelowe:
    -Cisco Aironet AIR-ANT2547VG-N, zysk anteny dla częstotliwości 2.4 gHz = 7 dBi, koszt około 300zł / szt,

To tylko kilka propozycji dotyczących zewnętrznych anten dla urządzenia. Najważniejszym czynnikiem który świadczy o tym, czy można wykorzystać daną antene w konfiguracji jest wskaźnik EIRP. Wartość EIRP jest obliczana na podstawie mocy transmitowanej przez antenę (w dBm) oraz zysku anteny (w dBi). Jest to szczególnie istotne w przypadku regulacji i norm dotyczących mocy sygnału radiowego, ponieważ EIRP uwzględnia zarówno moc transmitowaną przez nadajnik, jak i zysk anteny, co pozwala na lepsze określenie rzeczywistego zasięgu i potencjalnego wpływu sygnału na otoczenie. W Polsce dla pasma 2.4 gHz, maksymalna wartośc EIRP może wynosić 20dBm. W przypadku przekroczenia tej wartości, można dostosować moc nadawania oraz czułość odbiornika, jednakże jest to działanie, które może wpłynąć na jakość połączenia, dlatego jest ono niezalecane.  Poniżej znajduje się kalkulator, pomagający w obliczeniu EIRP. Domyślną mocą dla proponowanych urządzeń jest 22dBm, tłumiennośc kabla może zależeć od: długości, typu oraz budowli kabla.
Ogólne równanie dla obliczania wartości EIRP: 
Moc nadajnika + Zysk anteny - Tłumienność kabla * Długość kabla
""",
    'eirp_power':"Moc urządzenia [dBm]",
    'eirp_cable':"Tłumienność kabla [db/m]",
    'eirp_lencable':"Długość kabla [m]",
    'eirp_antenna':"Zysk Anteny [dBi]",

    'root2_ip_lbl_str':"Podaj docelowy adres IP portu Gigabitethernet, po ukończeniu konfiguracji",
    'nonroot2_ip_lbl_str':"Podaj docelowy adres IP portu Gigabitethernet, po ukończeniu konfiguracji"
}


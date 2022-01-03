import socket                       


for port in range(0, 1024):                                         #określenie skanowanych portów
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #obiekty z biblioteki socket
    mysocket.settimeout(1)

    ip = '8.8.8.8'                                                  
    address = (ip, port)                                            #zapisanie gniazda (socket) jako tuple

    result = mysocket.connect_ex(address)                           #wartość False jest zwracana w sytuacji gdy zostanie 
                                                                    #nawiązane połączenia
    if result == 0:
        print('port', port, 'jest otwarty')
    else:
        print('port', port, 'jest zamknięty')


    mysocket.close()
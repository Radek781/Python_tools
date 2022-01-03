import requests

if __name__ == '__main__':
    sess = requests.Session()
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    sess.proxies = proxies
    sess.verify = False

    login, password = 'user', 'pass'                    #dane do logowania

    data = {                                            #słownik z parametrami do logowania
        'login': login,
        'password': password
    }
    sess.post('http://127.0.0.1/login', data=data)  #wysyłanie POST z argumentami, parametr data powoduje, że parametry
                                                        #zostają sywłane w BODY żądania
                                                        #nie korzystamy z resp i będziemy widzieć odpowiedź jedynie w Burpie
    
    sess.cookies.set("mycookie", "myvalue", domain="127.0.0.1")     #ręczne ustawianie ciasteczek

    sess.get('http://127.0.0.1/profile')

    


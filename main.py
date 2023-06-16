import requests


def lifecell_auth(phone_number, password):
    base_url = 'https://api.lifecell.ua/mobile/'

    endpoint = 'auth'
    url = base_url + endpoint

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        'phone': phone_number,
        'password': password
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        auth_data = response.json()
        access_token = auth_data.get('access_token')
        return access_token
    else:
        print('Авторизация не удалась. Код ответа:', response.status_code)
        return None

phone_number = '+380634937124'
password = 'TukBh358'

access_token = lifecell_auth(phone_number, password)

if access_token:
    print('Авторизация успешна. Access token:', access_token)
else:
    print('Авторизация не удалась.')

import requests


def get_user(credentials):
    url = "http://localhost:7999/api/users/"
    payload = ""
    header_part = f'Basic {credentials}'
    headers = {"Authorization": header_part}
    response = requests.request("GET", url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        return response.status_code


# print(get_user('YWRtaW46MTIzNDU='))

def post_user(login, password):
    url = "http://localhost:7999/api/users/"
    headers = {"Content-Type": "application/json"}
    payload = {
        'username': f'{login}',
        'password': f'{password}'
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.status_code)
    return response.status_code


def get_apartments(credentials):
    url = "http://localhost:7999/api/apartments/"
    payload = ""
    header_part = f'Basic {credentials}'
    headers = {"Authorization": header_part}
    response = requests.request("GET", url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        return response.status_code


def post_apartments(credentials, user, name, address):
    url = "http://localhost:7999/api/apartments/"
    header_part = f'Basic {credentials}'
    headers = {"Content-Type": "application/json",
               "Authorization": header_part}
    payload = {
        'name': f'{name}',
        'address': f'{address}',
        'user': user
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.status_code)
    print(response.json())
    return response.status_code


def get_contracts(credentials):
    url = "http://localhost:7999/api/contracts/"
    header_part = f'Basic {credentials}'
    headers = {"Authorization": header_part}
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        return response.status_code


def post_contract(credentials, name, date, provider, type, apartment_id):
    url = "http://localhost:7999/api/contracts/"
    header_part = f'Basic {credentials}'
    headers = {"Content-Type": "application/json",
               "Authorization": header_part}
    payload = {
        'name': f'{name}',
        'date': f'{date}',
        'provider': provider,
        'type': f'{type}',
        'apartment': apartment_id
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    print(response.json())
    return response.status_code

def delete_contract(credentials, id):
    url = f'http://localhost:7999/api/contracts/{id}/'
    header_part = f'Basic {credentials}'
    headers = {"Content-Type": "application/json",
               "Authorization": header_part}
    response = requests.request("DELETE", url, headers=headers)
    print(response.status_code)
    return response.status_code

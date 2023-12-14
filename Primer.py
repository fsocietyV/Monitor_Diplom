import requests
import json

# Замени 'your_api_key' на свой API ключ
api_key = 'your_api_key'

def get_latest_version(software_name):
    url = f'https://api.example.com/latest/{software_name}'
    headers = {'X-API-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['version']

# Пример использования функции
software_name = 'Firefox'
latest_version = get_latest_version(software_name)
print(f'Последняя версия {software_name} - {latest_version}')

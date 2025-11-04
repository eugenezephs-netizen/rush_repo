import requests

response = requests.get("http://ip.jsontest.com/")
# Выводит статус код ответа
print(response.status_code)
# Выводит JSON-ответ
print(response.json())
import requests
response = requests.head('https://www.example.com')
print(f"Програма запустилась, відповідь від сайту буде: {response.status_code}")
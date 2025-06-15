import time
import requests

url = input('Enter url: ')

while True:
    q = requests.get(url + '/api/swagger/')

    res = q
    print(res)
    time.sleep(20)

import requests
import re
url='https://api.xeggex.com/api/v2/ticker/MAXE/USDT/'
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    try:
        r=requests.get(url)
        if r.status_code == 200:
            response=r.json()
            print(response['last_price'])
            break
        else:
            print(f"Failed to connect (Status code: {r.status_code}). Retrying...")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        # 增加尝试次数
    attempts += 1
if attempts >= max_attempts:
    print("Failed to retrieve data after multiple attempts.")
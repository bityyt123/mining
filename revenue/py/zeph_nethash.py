import requests
import re
url='https://explorer.zephyrprotocol.com/api/networkinfo'
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    try:
        r=requests.get(url)
        if r.status_code == 200:
            response=r.json()
            netinfo=response['data']
            nh_h=netinfo['hash_rate']
            nh_m=nh_h/1000000
            print(round(nh_m,2))
            break
        else:
            print(f"Failed to connect (Status code: {r.status_code}). Retrying...")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        # 增加尝试次数
    attempts += 1
if attempts >= max_attempts:
    print("Failed to retrieve data after multiple attempts.")
import requests
import re
url='https://explorer.dynexcoin.org/api'
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    try:
        r=requests.get(url)
        if r.status_code == 200:
            response=r.json()
            data = response[0]
            block_header = data['block_header']
            nh_h = block_header['hashrate']
            nh_m=nh_h/1000000
            print(int(nh_m))
            break
        else:
            print(f"Failed to connect (Status code: {r.status_code}). Retrying...")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        # 增加尝试次数
    attempts += 1
if attempts >= max_attempts:
    print("Failed to retrieve data after multiple attempts.")
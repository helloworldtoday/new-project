from curl_cffi import requests
import random, time,json
from concurrent.futures import ThreadPoolExecutor, as_completed
user_name = input("enter user name:")
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
]
def search(name, url):
        try:
            headers = {
                        "User-Agent": random.choice(USER_AGENTS),
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": '"Windows"',
                        "Sec-Fetch-Dest": "document",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-Site": "none", 
                        "Sec-Fetch-User": "?1",
            }
            res = requests.get(url.rstrip("/") + "/" + user_name, impersonate="chrome120", headers=headers, timeout=5)
            time.sleep(random.uniform(1.5,5.5))
            if res.status_code == 200 and len(res.text) > 1 *1024:
                return f"found!! {name}: {url}{user_name}"
            elif res.status_code == 404:
                return f"{name}: page not found"
            elif res.status_code == 429:
                return f"{name}: too many request"
            else:
                return f"{name}: error{res.status_code}"
        except:
            print("未知錯誤")
with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_name = {executor.submit(search, name, url): name for name, url in data.items()}
            for future in as_completed(future_name):
                o_name = future_name.get(future)
                print(future.result())



            


from curl_cffi import requests
import random, time,json,logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from random_url import make_rand_url
from config import headers, tor_proxies, status_massage, data
user_name = input("enter user name:")
use_tor = input("use tor [y/n]:")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def search(name, url):
        global use_tor
        use_tor = str(use_tor).strip().lower() == "y"
        proxies = tor_proxies if use_tor else None
        try:
            random_url = make_rand_url(url)
            res = requests.get(random_url,proxies=proxies, headers=headers, timeout=10)
            base = {
                "code": res.status_code,
                "length": len(res.text),
                "url": random_url
            }

            res = requests.get(url.rstrip("/") + "/" + user_name, impersonate="chrome120", headers=headers, timeout=5, proxies=proxies)
            time.sleep(random.uniform(1.5,5.5))
            different = abs(base.get("length") - len(res.text))
            tolerance = max(100, base.get("length") * 0.1)
            if res.status_code == 404 or tolerance >= different:
                return f"{name}: page not found"
            for code, text in status_massage.items():
                if int(code) == res.status_code:
                    return f"{name}: {text}"
            if res.status_code == 200:
                return f"Found !!{name}: {url}"
        except Exception as e:
            logger.error(f"{name} error: {e}")
def run():
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_name = {executor.submit(search, name, url): name for name, url in data.items()}
            for future in as_completed(future_to_name):
                logger.info(future.result())
if __name__ == '__main__':
    run()



            


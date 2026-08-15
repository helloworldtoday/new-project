from curl_cffi import requests
import random, time,logging,threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from random_url import make_rand_url
from config import base_headers, tor_proxies, status_massage, data, USER_AGENTS
user_name = input("enter user name:")
use_tor = input("use tor [y/n]:").strip().lower() == "y"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def combine_headers():
    headers = dict(base_headers)
    headers["User-Agent"] = random.choice(USER_AGENTS)
    return headers
     
def search(name, url, use_tor):
        proxies = tor_proxies if use_tor else None
        try:
            session = get_session()
            headers = combine_headers()
            random_url = make_rand_url(url)
            res = session.get(random_url,proxies=proxies,impersonate="chrome120", headers=headers, timeout=10)
            base = {
                "code": res.status_code,
                "length": len(res.text),
                "url": random_url
            }

            res = session.get(url.rstrip("/") + "/" + user_name, impersonate="chrome120", headers=headers, timeout=10, proxies=proxies)
            time.sleep(random.uniform(1.5,5.5))
            different = abs(base.get("length") - len(res.text))
            tolerance = max(100, base.get("length") * 0.1)
            if res.status_code == 404 or tolerance >= different:
                return f"{name}: page not found"
            for code, text in status_massage.items():
                if code == res.status_code:
                    return f"{name}: {text}"
            if res.status_code == 200:
                return f"Found !!{name}: {url}{user_name}"
            return f"{name} error: {res.status_code}"
        except Exception as e:
            logger.error(f"{name} error: {e}")
def run():
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_name = {executor.submit(search, name, url, use_tor): name for name, url in data.items()}
            for future in as_completed(future_to_name):
                logger.info(future.result())
if __name__ == '__main__':
    run()



            


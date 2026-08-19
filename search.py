from curl_cffi import requests
import random, time,logging,threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from random_url import make_rand_url
from config import base_headers, tor_proxies, status_massage, data, USER_AGENTS
from check import check_keywords
from summ import summary

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
     
def search(name, url,user_name, use_tor):
        proxies = tor_proxies if use_tor else None
        try:
            session = get_session()
            headers = combine_headers()
            random_url = make_rand_url(url)
            res = session.get(random_url,proxies=proxies,impersonate="chrome120", headers=headers, timeout=10)
            base_length = len(res.text)

            target = url.replace("{username}", user_name)
            res = session.get(target, impersonate="chrome120", headers=headers, timeout=10, proxies=proxies)
            time.sleep(random.uniform(1.5,5.5))
            have_keyword = check_keywords(html=res.text)

            signals = {
                "status_code": res.status_code,
                "base_length": base_length,
                "keyword_hit": have_keyword,
                "res_length": len(res.text)
            }
            reasons = summary(signals=signals)
            return {"name": name, "url": target, "reasons": reasons}
        except Exception as e:
            logger.error(f"{name} error: {e}")
def run(user_name, use_tor, Max_workers=5):
        with ThreadPoolExecutor(max_workers=Max_workers) as executor:
            future_to_name = {executor.submit(search, name, url, user_name, use_tor): name for name, url in data.items()}
            for future in as_completed(future_to_name):
                logger.info(future.result())
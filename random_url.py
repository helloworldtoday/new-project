import random,string
from urllib.parse import urlparse

def make_rand_url(url):
    parsed_url = urlparse(url)
    ramdom_letters = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    random_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{ramdom_letters}"
    return random_url


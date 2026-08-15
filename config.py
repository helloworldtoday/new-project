import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
]
base_headers = {
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

tor_proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

status_massage = {
    301: "Moved Permanently",
    429: "too many request",
    304: "Not Modified",
    400: "Bad Request",
    403: "Forbidden",
    401: "Unauthorized"
}

data = {
    "Facebook": "https://facebook.com/",
    "Instagram": "https://instagram.com/",
    "Threads": "https://www.threads.net/@",
    "LINE 官方帳號": "https://page.line.me/",
    "X": "https://x.com/",
    "TikTok": "https://tiktok.com/@",
    "LinkedIn": "https://www.linkedin.com/in/",
    "巴哈姆特": "https://home.gamer.com.tw/homeindex.php?owner=",
    "Dcard": "https://dcard.tw/@",
    "YouTube": "https://youtube.com/@",
    "蝦皮購物": "https://shopee.tw/",
    "露天市集": "https://www.ruten.com.tw/store/",
    "旋轉拍賣": "https://tw.carousell.com/u/",
    "Pinkoi": "https://www.pinkoi.com/store/"
}
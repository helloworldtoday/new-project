import re
from config import keywords

def check_keywords(html):
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if not match:
        return False
    title = match.group(1).lower().strip()
    if not title:
        return False    
    return any(keyword in title for keyword in keywords)



from config import status_massage

def summary(signals):
    reason = []
    res_length = signals.get("res_length")
    base_length = signals.get("base_length")
    status_code = signals.get("status_code")
    keyword_hit = signals.get("keyword_hit")
    different = abs(res_length - base_length)
    tolerate = max(100, base_length * 0.05) 
    if status_code == 404:
        reason.append("頁面不存在\n")
    if different >= tolerate and status_code == 200:
        reason.append("可能網頁被重新導向\n")
    for code, massage in status_massage.items():
        if code == status_code:
            reason.append(f"狀態碼:{code}| {massage}\n")
    if keyword_hit:
        reason.append("包含錯誤關鍵字，網頁可能不存在。\n")

    return reason
        
    
        
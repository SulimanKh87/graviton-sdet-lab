import time, requests

def http_latency(url="https://www.amazon.com", timeout=3):
    t0 = time.perf_counter()
    r = requests.get(url, timeout=timeout)
    return r.status_code, (time.perf_counter() - t0)


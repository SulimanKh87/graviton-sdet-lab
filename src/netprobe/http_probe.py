import time
import requests
import yaml
import pathlib

# Load configuration once at import
CONFIG_PATH = pathlib.Path("config.yaml")

if CONFIG_PATH.exists():
    CONFIG = yaml.safe_load(CONFIG_PATH.read_text())
else:
    CONFIG = {
        "network": {
            "http_urls": ["https://www.amazon.com"],
            "latency_threshold_ms": 1000,
        }
    }


def http_latency(url=None, timeout=3):
    """
    Measure HTTP latency for one or more URLs.
    Returns a list of tuples: [(url, status_code, latency_ms), ...]
    """
    urls = CONFIG["network"]["http_urls"] if url is None else [url]
    results = []

    for u in urls:
        try:
            t0 = time.perf_counter()
            r = requests.get(u, timeout=timeout)
            latency_ms = (time.perf_counter() - t0) * 1000
            results.append((u, r.status_code, latency_ms))
        except requests.RequestException as e:
            # Capture failures as code=0 with latency=-1
            results.append((u, 0, -1))
            print(f"[WARN] HTTP request failed for {u}: {e}")

    return results


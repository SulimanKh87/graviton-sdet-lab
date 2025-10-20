import pytest
import yaml
import pathlib
from src.netprobe.http_probe import http_latency

# Load test parameters
CONFIG_PATH = pathlib.Path("config.yaml")
CONFIG = yaml.safe_load(CONFIG_PATH.read_text())
LAT_THRESHOLD = CONFIG["network"]["latency_threshold_ms"]


@pytest.mark.sanity
def test_http_latency_threshold():
    """
    Sanity: verify each configured URL responds and latency is within threshold.
    Accepts any valid HTTP status < 600 to tolerate redirects / maintenance.
    """
    for url, code, latency in http_latency():
        assert 100 <= code < 600, f"{url} returned invalid code {code}"
        assert latency >= 0, f"{url} produced negative latency"
        assert latency <= LAT_THRESHOLD, (
            f"{url} latency {latency:.1f}ms exceeds threshold {LAT_THRESHOLD}ms"
        )


@pytest.mark.regression
def test_http_handles_failures(monkeypatch):
    """
    Regression: simulate request failure to confirm graceful handling.
    """
    import requests

    def fake_get(*args, **kwargs):
        raise requests.RequestException("network down")

    monkeypatch.setattr(requests, "get", fake_get)
    results = http_latency("https://fake.test")
    assert isinstance(results, list)
    assert results[0][1] == 0  # code = 0 for failed request
    assert results[0][2] == -1  # latency = -1 for failed request


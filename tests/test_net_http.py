import pytest
from src.netprobe.http_probe import http_latency

@pytest.mark.sanity
def test_http_latency_ok():
    code, latency = http_latency()
    # Accept any valid HTTP code below 600
    assert 100 <= code < 600, f"Unexpected status code: {code}"
    # Latency should be non-negative
    assert latency >= 0

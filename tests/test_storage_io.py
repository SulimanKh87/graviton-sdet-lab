import pytest
from src.storageprobe.io_probe import rw_throughput

@pytest.mark.regression
def test_rw_throughput_runs():
    w, r = rw_throughput(1_000_000)
    assert w > 0 and r > 0

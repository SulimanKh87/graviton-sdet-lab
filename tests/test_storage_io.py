import pytest, yaml, pathlib
from src.storageprobe.io_probe import rw_throughput

CONFIG = yaml.safe_load(pathlib.Path("config.yaml").read_text())
MIN_W = CONFIG["storage"]["min_write_MBps"] * 1_000_000
MIN_R = CONFIG["storage"]["min_read_MBps"] * 1_000_000

@pytest.mark.regression
def test_rw_throughput_threshold():
    w, r = rw_throughput(5_000_000)
    assert w >= MIN_W, f"Write speed too low: {w/1_000_000:.2f} MB/s"
    assert r >= MIN_R, f"Read speed too low: {r/1_000_000:.2f} MB/s"

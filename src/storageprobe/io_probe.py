import os, time, tempfile

def rw_throughput(bytes_size=1_000_000):
    data = b"0" * bytes_size
    with tempfile.TemporaryDirectory() as d:
        out = os.path.join(d, "blk")
        t0 = time.perf_counter()
        with open(out, "wb") as f:
            f.write(data)
        wps = bytes_size / (time.perf_counter() - t0)

        t1 = time.perf_counter()
        with open(out, "rb") as f:
            _ = f.read()
        rps = bytes_size / (time.perf_counter() - t1)
    return wps, rps


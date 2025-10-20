import subprocess, re

def cpu_info():
    out = subprocess.check_output(["lscpu"], text=True, errors="ignore")
    info = {}
    for line in out.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            info[k.strip()] = v.strip()
    return info

def has_flag(flag):
    with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as f:
        return bool(re.search(rf"\b{re.escape(flag)}\b", f.read()))

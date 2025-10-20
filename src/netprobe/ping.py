import subprocess

def ping(host="8.8.8.8", count=2, timeout=2):
    try:
        out = subprocess.run(
            ["ping", "-c", str(count), "-W", str(timeout), host],
            capture_output=True, text=True, check=True
        )
        return True, out.stdout
    except subprocess.CalledProcessError as e:
        return False, (e.stdout or "") + (e.stderr or "")
    except FileNotFoundError as e:
        return False, f"ping not found: {e}"
import subprocess

def ping(host="8.8.8.8", count=2, timeout=2):
    try:
        out = subprocess.run(
            ["ping", "-c", str(count), "-W", str(timeout), host],
            capture_output=True, text=True, check=True
        )
        return True, out.stdout
    except subprocess.CalledProcessError as e:
        return False, (e.stdout or "") + (e.stderr or "")
    except FileNotFoundError as e:
        return False, f"ping not found: {e}"

import argparse, subprocess, sys, os

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--suite", choices=["sanity", "regression"], default="sanity")
    p.add_argument("-n", "--workers", type=int, default=1)
    p.add_argument("--html", default="report.html")
    args = p.parse_args()

    os.makedirs("artifacts", exist_ok=True)
    html_path = os.path.join("artifacts", args.html)

    cmd = [
        sys.executable, "-m", "pytest", "tests",
        "-m", args.suite,
        f"--html={html_path}", "--self-contained-html",
        "-n", str(args.workers),
        "--cov=src", "--cov-report=term"
    ]
    print("Running:", " ".join(cmd))
    return subprocess.call(cmd)

if __name__ == "__main__":
    raise SystemExit(main())


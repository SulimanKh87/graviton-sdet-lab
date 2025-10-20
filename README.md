# graviton-sdet-lab

Linux-based test automation framework for Amazon SDE/SDET practice.

## Features
- CPU/OS probes (`lscpu`, `/proc`, `/etc/os-release`)
- Network probes (ping, HTTP latency)
- Storage I/O sanity checks
- pytest markers: sanity (fast) & regression (deep)
- Parallel test runs, HTML report, code coverage

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.orchestrator.cli --suite sanity -n 2 --html sanity.html

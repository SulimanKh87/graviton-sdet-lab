# 🧩 graviton-sdet-lab

A **Linux-based test automation framework** inspired by Amazon SDE/SDET validation tools.  
It performs system health checks for **CPU, Network, and Storage**, runs in **parallel**,  
generates **HTML & coverage reports**, and supports **Docker + CI/CD**.

---

## 🚀 Features
- **CPU & OS probes:** `/proc`, `lscpu`, `/etc/os-release`
- **Network probes:** ICMP `ping`, HTTP latency (with YAML thresholds)
- **Storage probe:** read/write throughput verification
- **Suite markers:** `@pytest.mark.sanity` (fast) / `@pytest.mark.regression` (deep)
- **Config file:** `config.yaml` for latency/throughput thresholds
- **Parallel execution:** via `pytest-xdist`
- **HTML reporting + coverage:** via `pytest-html` and `pytest-cov`
- **Dockerized:** reproducible Linux environment
- **CI/CD Ready:** GitHub Actions workflow for automated testing & artifact upload

---

## 📁 Project Structure
graviton-sdet-lab/
│
├── src/
│ ├── framework/ # (future config/util extensions)
│ ├── sysprobe/ # CPU / OS data collection
│ ├── netprobe/ # Network ping + HTTP latency
│ ├── storageprobe/ # Disk I/O checks
│ └── orchestrator/ # CLI entry point
│
├── tests/ # pytest suites
├── config.yaml # thresholds for latency / throughput
├── Dockerfile # containerized environment
├── requirements.txt # dependencies
└── .github/workflows/ci.yml # CI pipeline

yaml
Copy code

---

## ⚙️ Installation (Linux / WSL2)
```bash
git clone https://github.com/<your-username>/graviton-sdet-lab.git
cd graviton-sdet-lab
python3 -m venv .venv && source .venv/bin/activate
pip install -U pip -r requirements.txt
🧪 Running Tests
Sanity suite (fast):

bash
Copy code
python -m src.orchestrator.cli --suite sanity -n 2 --html sanity.html
Regression suite (deeper):

bash
Copy code
python -m src.orchestrator.cli --suite regression -n 2 --html regression.html
HTML reports are saved in artifacts/ → open with:

bash
Copy code
explorer.exe artifacts/sanity.html
🧱 Docker Usage
Build & Run container:

bash
Copy code
docker build -t graviton-sdet-lab .
docker run --rm -v "$(pwd)/artifacts":/app/artifacts graviton-sdet-lab
This runs the sanity suite inside a clean Linux container
and mounts reports back to your host at artifacts/sanity.html.

⚙️ CI/CD (GitHub Actions)
The workflow .github/workflows/ci.yml automatically:

Installs dependencies

Runs pytest -m sanity

Uploads HTML and coverage reports as artifacts

Badge example (replace with your username):

markdown
Copy code
![Tests](https://github.com/<your-username>/graviton-sdet-lab/actions/workflows/ci.yml/badge.svg)

## 🧭 Architecture Overview

```mermaid
graph TD
    A[CLI Orchestrator<br>src/orchestrator/cli.py] --> B[Pytest Runner]
    B -->|Sanity / Regression| C[System Probes]
    C -->|CPU| D[sysprobe/cpu.py]
    C -->|Network| E[netprobe/ping.py & http_probe.py]
    C -->|Storage| F[storageprobe/io_probe.py]
    B --> G[Reports]
    G -->|HTML + Coverage| H[artifacts/report.html]
    H --> I[GitHub Actions<br>Artifact Upload]

🧠 Why It Matters

Demonstrates framework design, test layering, and CI/CD integration

Reflects Linux + automation experience relevant to Amazon SDE/SDET roles

Extensible — thresholds, config-driven execution, Docker reproducibility

🛠️ Tech Stack

Python | pytest | PyYAML | Docker | GitHub Actions | Linux (WSL2)

@contact
Suleiman Khasheboun
📧 suli.tempmail2022@gmail.com

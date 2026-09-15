# Linux Security & Telemetry Toolkit

A collection of lightweight Bash and Python security utilities built for log parsing, network reconnaissance, system telemetry, and host integrity monitoring on Linux systems.

---

## ⚠️ Ethical Use & Legal Disclaimer

**Authorized Use Only:** The tools contained within this repository are designed strictly for educational purposes, defensive auditing, and authorized security testing within controlled lab environments (such as local virtual machines). Unauthorized scanning or probing of networks or systems without explicit prior permission is illegal and unethical. The author assumes no liability for misuse.

---

## 📁 Repository Architecture

```text
linux-security-toolkit/
│
├── README.md
├── .gitignore
│
├── src/
│   ├── file_integrity.py
│   ├── generate_blacklist.sh
│   ├── port_scanner.py
│   ├── py_scanner.py
│   └── ssh_analyser.sh
│
├── prototypes/
│   ├── fim_v1.py
│   ├── fim_v2.py
│   ├── ports_scanner_v1.py
│   ├── ports_scanner_v2.py
│   ├── ports_scanner_v3.py
│   └── ssh_analyser_v1.sh
│
├── docs/
│   └── design-decisions.md
│
└── tests/
    └── test_file_integrity.py
```

---

## 🛠️ Included Tools

| Utility | Language | Purpose | Key Technical Mechanics |
| :--- | :--- | :--- | :--- |
| `ssh_analyser.sh` | Bash | Filters failed login attempts dynamically based on a user-defined threshold. | Parameter expansion `${1:-1}`, `awk -v` variable passing |
| `generate_blacklist.sh` | Bash | Isolates IP addresses exceeding a failure threshold and exports a candidate review list. | File redirection `>`, stdout pipelines, root check (`$EUID`) |
| `port_scanner.py` / `py_scanner.py` | Python 3 | Advanced multithreaded TCP port scanners with CLI arguments and banner grabbing. | `argparse`, `ThreadPoolExecutor`, `socket` |
| `file_integrity.py` | Python 3 | Advanced File Integrity Monitor (FIM) tracking modifications, deletions, and added files. | `hashlib.sha256`, `os.walk`, `argparse`, JSON baseline serialization |

---

## 🚀 Installation & Setup

Clone the repository and set execution permissions inside your lab environment:

```bash
git clone [https://github.com/CyberS-Coder/linux-security-toolkit.git](https://github.com/CyberS-Coder/linux-security-toolkit.git)
cd linux-security-toolkit
chmod +x src/*.sh src/*.py
```

---

## 💻 Usage & Sample Outputs

### 1. SSH Log Analysis (Bash)
```bash
sudo ./src/ssh_analyser.sh 5
```
**Sample Output:**
```text
Analyzing systemd journal logs for failed SSH authentication attempts...
Threshold filter set to: >= 5 failures

Failed Count | Source IP Address
--------------------------------
14           | 192.168.1.105
8            | 10.0.0.42
```

### 2. Multithreaded Port Scanner (Python CLI)
```bash
python3 src/port_scanner.py --target 127.0.0.1 --ports 1-1024 --workers 50
```
**Sample Output:**
```text
Scanning target 127.0.0.1 (127.0.0.1) on ports 1-1024...
Port 22    OPEN | Service Banner: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6
Port 80    OPEN | Service Banner: HTTP/1.1 200 OK
Scan complete. Checked 1024 ports across 50 workers.
```

### 3. File Integrity Monitoring (Python CLI)
* **Generate initial baseline:**
  ```bash
  python3 src/file_integrity.py --target /etc/ssh --baseline baseline.json --init
  ```
* **Verify system file integrity:**
  ```bash
  python3 src/file_integrity.py --target /etc/ssh --baseline baseline.json --check
  ```
**Sample Output:**
```text
Verifying integrity of target path: /etc/ssh
OK: /etc/ssh/sshd_config
ALERT!: MODIFIED FILE -> /etc/ssh/ssh_config
ALERT!: NEW UNTRACKED FILE ADDED -> /etc/ssh/backdoor.key
ALERT!: MISSING FILE -> /etc/ssh/moduli
```

---

## 🛡️ Threat Model & Security Considerations

### File Integrity Monitoring (FIM)
* **Baseline Security:** SHA-256 cryptographic hashing effectively detects accidental or unauthorized file modifications. However, if an attacker achieves root privileges (`UID 0`), they can tamper with both the monitored files and the local baseline JSON file.
* **Mitigation:** In production environments, baselines should be stored on read-only media, exported to a remote SIEM server, or cryptographically signed.

### Network Reconnaissance
* **False Positives vs. Vulnerabilities:** Finding an open port or retrieving a banner string confirms an active listening service, but does **not** prove a vulnerability or misconfiguration exists.
* **Evidence vs. Conclusion:** IP addresses exhibiting excessive authentication failures are flagged as **suspicious candidates for review** rather than definitively malicious, accounting for automated retries or user input errors.

---

## 📈 Engineering Evolution

To demonstrate iterative problem-solving and software maintenance, early prototypes are archived in `prototypes/`. 
* **Phase 1:** Built baseline functional scripts using procedural logic and interactive prompts.
* **Phase 2:** Upgraded utilities to support concurrency (`ThreadPoolExecutor`), recursive traversal (`os.walk`), path-sanitized state isolation, and standardized CLI interaction (`argparse`).
* **Phase 3:** Added automated test coverage (`tests/test_file_integrity.py`) and CI integration via GitHub Actions.

---

## 👨‍💻 Author

* **GitHub Profile:** [@CyberS-Coder](https://github.com/CyberS-Coder)
* **Focus:** Cybersecurity, Linux Systems Administration, and Security Automation.

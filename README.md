# Linux Security & Telemetry Toolkit

A collection of lightweight Bash and Python security utilities built for log parsing, network reconnaissance, and threat mitigation on Linux systems.

This repository demonstrates practical systems administration, text-processing pipelines, network socket programming, and concurrency optimization.

---

## 🛠️ Included Tools

| Utility | Language | Purpose | Key Technical Mechanics |
| :--- | :--- | :--- | :--- |
| `ssh_analyser.sh` | Bash | Parses `systemd` journal logs to extract and sort failed SSH login attempts. | `journalctl`, `awk`, `uniq -c`, `sort -nr` |
| `ssh_analyser_v2.sh` | Bash | Filters failed login attempts dynamically based on a user-defined threshold. | Parameter expansion `${1:-1}`, `awk -v` variable passing |
| `generate_blacklist.sh` | Bash | Isolates malicious IP addresses exceeding a failure threshold and exports a clean blocklist. | File redirection `>`, stdout pipelines, root check (`$EUID`) |
| `py_scanner.py` | Python 3 | Sequential TCP port scanner with domain resolution and service banner grabbing. | `socket.AF_INET`, `socket.SOCK_STREAM`, `gethostbyname()`, `connect_ex()`, `recv()` |
| `py_scanner_v2.py` | Python 3 | High-speed **multithreaded** TCP port scanner utilizing a thread pool for concurrent port checks. | `concurrent.futures.ThreadPoolExecutor`, `executor.map()`, worker functions |

---

## 🚀 Installation & Setup

Clone the repository and set execution permissions:

```bash
git clone [https://github.com/CyberS-Coder/linux-security-toolkit.git](https://github.com/CyberS-Coder/linux-security-toolkit.git)
cd linux-security-toolkit
chmod +x *.sh py_scanner.py py_scanner_v2.py
💻 Usage & Examples
1. Basic SSH Log Analysis (Bash)
Bash
sudo ./ssh_analyser.sh
2. Threshold-Based SSH Analysis (Bash)
Bash
# Display IPs with 5 or more failed login attempts
sudo ./ssh_analyser_v2.sh 5
3. Generate Firewall Blacklist (Bash)
Bash
# Extract IPs with 3 or more failed attempts to blacklisted_ips.txt
sudo ./generate_blacklist.sh 3
4. Sequential Port Scanner (Python v1)
Bash
python3 py_scanner.py
5. Multithreaded High-Speed Port Scanner & Banner Grabber (Python v2)
Bash
python3 py_scanner_v2.py
Performance Gain: Utilizes ThreadPoolExecutor(max_workers=50) to scan hundreds of ports concurrently, reducing scan times from minutes to seconds.

🔬 Systems & Security Concepts Demonstrated
Telemetry & Log Analysis: Transforming unstructured systemd logs (journalctl) into actionable threat intelligence using Unix text-processing pipelines.

Network Concurrency: Leveraging Python's concurrent.futures to transform I/O-bound sequential bottlenecks into efficient multi-worker thread pools.

Network Socket Programming: Interfacing directly with the OS network stack via Python's socket library to execute TCP handshakes (SOCK_STREAM).

Service Fingerprinting: Banner grabbing via socket data retrieval (recv()) to identify running software versions on open ports.

👨‍💻 Author
GitHub: @CyberS-Coder

Focus: Cybersecurity, Linux Systems Administration, and Security Automation.

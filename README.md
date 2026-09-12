# Linux Security & Telemetry Toolkit

A collection of lightweight Bash and Python security utilities built for log parsing, network reconnaissance, and system telemetry on Linux systems.

---

## ⚠️ Ethical Use & Legal Disclaimer

**Authorized Use Only:** The tools contained within this repository are designed strictly for educational purposes, defensive auditing, and authorized security testing within controlled lab environments (such as local virtual machines). Unauthorized scanning or probing of networks or systems without explicit prior permission is illegal and unethical. The author assumes no liability for misuse.

---

## 🛠️ Included Tools

| Utility | Language | Purpose | Key Technical Mechanics |
| :--- | :--- | :--- | :--- |
| `ssh_analyser.sh` | Bash | Parses `systemd` journal logs to extract and sort failed SSH login attempts. | `journalctl`, `awk`, `uniq -c`, `sort -nr` |
| `ssh_analyser_v2.sh` | Bash | Filters failed login attempts dynamically based on a user-defined threshold and formats output. | Parameter expansion `${1:-1}`, `awk -v` variable passing |
| `generate_blacklist.sh` | Bash | Isolates malicious IP addresses exceeding a failure threshold and exports a clean blocklist. | File redirection `>`, stdout pipelines, root check (`$EUID`) |
| `ports_scanner.py` | Python 3 | Interactive TCP port scanner with input validation, domain resolution, and service banner grabbing. | `socket.AF_INET`, `socket.SOCK_STREAM`, `gethostbyname()`, `connect_ex()`, `recv()` |
| `ports_scanner_v2.py` | Python 3 | High-speed **multithreaded** TCP port scanner utilizing a thread pool for concurrent port checks. | `concurrent.futures.ThreadPoolExecutor`, `executor.map()`, input validation |

---

## 🚀 Installation & Setup

Clone the repository and set execution permissions inside your lab environment:

bash
git clone [https://github.com/CyberS-Coder/linux-security-toolkit.git](https://github.com/CyberS-Coder/linux-security-toolkit.git)
cd linux-security-toolkit
chmod +x *.sh *.py

💻 Usage & Examples1. Basic SSH Log Analysis (Bash)
sudo ./ssh_analyser.sh
2. Threshold-Based SSH Analysis (Bash)
#Display IPs with 5 or more failed login attempts
sudo ./ssh_analyser_v2.sh 5
3. Generate Firewall Blacklist (Bash)
# Extract IPs with 3 or more failed attempts to blacklisted_ips.txt
sudo ./generate_blacklist.sh 3
4. Interactive Port Scanner (Python v1)
python3 ports_scanner.py
5. Multithreaded High-Speed Port Scanner & Banner Grabber (Python v2)
python3 ports_scanner_v2.py
Performance Gain: Utilizes ThreadPoolExecutor(max_workers=50) to scan hundreds of ports concurrently, reducing scan times from minutes to seconds.

🔬 Systems & Security Concepts DemonstratedTelemetry & Log Analysis: 
Transforming unstructured systemd logs (journalctl) into structured log indicators using Unix text-processing pipelines.
Network Concurrency: Leveraging Python's concurrent.futures to transform I/O-bound sequential bottlenecks into efficient multi-worker thread pools.
Network Socket Programming: Interfacing directly with the OS network stack via Python's socket library to execute TCP handshakes (SOCK_STREAM) and handle socket timeouts.
Service Fingerprinting: Banner grabbing via socket data retrieval (recv()) to identify running software versions on open ports.
Defensive Input Validation: Enforcing strict range checks ($1-65535$) and exception handling to prevent runtime failures on malformed user input.

⚠️ Technical Limitations
Port Scanners vs. Vulnerabilities: Identifying an open port or retrieving a software banner (e.g., OpenSSH_8.9p1) indicates what service is running, but it does not prove the service is vulnerable or misconfigured.
Log Variability: SSH log structures and format strings (journalctl -u ssh) can vary across different Linux distributions and version updates, requiring regular parser maintenance.
Network Constraints: High-speed multithreading (max_workers=50) may trigger local firewall rate-limiting or network packet drops on constrained virtual interfaces.

💡 What I Learned
Building this toolkit provided foundational insight into how operating systems handle network I/O and log telemetry.
Transitioning from Sequential to Concurrent Execution: Realizing that network tools are I/O-bound (waiting on socket timeouts) made it clear why multithreading via ThreadPoolExecutor is essential for performance scaling.
The Importance of Defensive Programming: Adding input validation for port boundaries and resolving hostnames safely taught me how easily scripts break when exposed to unexpected user inputs or unavailable hosts.
Unix Pipe Power: Mastering the interplay between journalctl, awk, sort, and uniq demonstrated how powerful native Linux utilities are for lightweight system auditing without heavy external dependencies.

👨‍💻 AuthorGitHub Profile: @CyberS-Coder
Focus: Cybersecurity, Linux Systems Administration, and Security Automation.

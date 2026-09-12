# Linux Security & Telemetry Toolkit

A collection of lightweight Bash and Python security utilities built for log parsing, network reconnaissance, and threat mitigation on Linux systems.

This repository demonstrates practical systems administration, text-processing pipelines, network socket programming, and defensive security concepts.

---

## 🛠️ Included Tools

| Utility | Language | Purpose | Key Technical Mechanics |
| :--- | :--- | :--- | :--- |
| `ssh_analyser.sh` | Bash | Parses `systemd` journal logs to extract and sort failed SSH login attempts. | `journalctl`, `awk`, `uniq -c`, `sort -nr` |
| `ssh_analyser_v2.sh` | Bash | Filters failed login attempts dynamically based on a user-defined threshold. | Parameter expansion `${1:-1}`, `awk -v` variable passing |
| `generate_blacklist.sh` | Bash | Isolates malicious IP addresses exceeding a failure threshold and exports a clean blocklist. | File redirection `>`, stdout pipelines, root check (`$EUID`) |
| `py_scanner.py` | Python 3 | Performs TCP port scanning, domain resolution, and service banner grabbing. | `socket.AF_INET`, `socket.SOCK_STREAM`, `gethostbyname()`, `connect_ex()`, `recv()` |

---

## 🚀 Installation & Setup

Clone the repository and set execution permissions:

```bash
git clone [https://github.com/CyberS-Coder/linux-security-toolkit.git](https://github.com/CyberS-Coder/linux-security-toolkit.git)
cd linux-security-toolkit
chmod +x *.sh py_scanner.py

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
4. Interactive TCP Port Scanner & Banner Grabber (Python)
Bash
python3 py_scanner.py
Inputs: Target IP/Domain (e.g., 127.0.0.1 or scanme.nmap.org), start port, end port.

Output: Identifies open TCP ports and prints service version banners (e.g., OpenSSH_8.9p1).

🔬 Systems & Security Concepts Demonstrated
Telemetry & Log Analysis: Transforming unstructured systemd logs (journalctl) into actionable threat intelligence using Unix text-processing pipelines.

Access Control & Safety Checks: Enforcing execution safety by validating Effective User ID ($EUID == 0) before reading restricted logs.

Network Socket Programming: Interfacing directly with the OS network stack via Python's socket library to execute TCP handshakes (SOCK_STREAM).

Service Fingerprinting: Banner grabbing via socket data retrieval (recv()) to identify running software versions on open ports.

DNS Resolution & Error Handling: Resolving hostnames dynamically (gethostbyname()) and handling network exceptions (gaierror) gracefully.

👨‍💻 Author
GitHub: @CyberS-Coder

Focus: Cybersecurity, Linux Systems Administration, and Security Automation.

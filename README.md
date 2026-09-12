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

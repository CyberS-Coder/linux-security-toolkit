# linux-security-toolkit
## 🛠️ Included Tools

| Utility | Purpose | Key Technical Mechanics |
| :--- | :--- | :--- |
| `ssh_analyser.sh` | Parses `systemd` journal logs to extract, count, and sort failed SSH login attempts. | `journalctl`, `awk`, `uniq -c`, `sort -nr` |
| `ssh_analyser_v2.sh` | Filters failed login attempts dynamically based on a user-defined threshold. | Parameter expansion `${1:-1}`, `awk -v` variable passing |
| `generate_blacklist.sh` | Isolates malicious IP addresses exceeding a failure threshold and exports a clean IP blocklist for firewall ingestion. | File redirection `>`, stdout pipelines, root privilege verification (`$EUID`) |

---

## 🚀 Installation & Setup

Clone the repository and ensure the scripts have execution permissions:

```bash
git clone [https://github.com/CyberS-Coder/linux-security-toolkit.git](https://github.com/CyberS-Coder/linux-security-toolkit.git)
cd linux-security-toolkit
chmod +x *.sh

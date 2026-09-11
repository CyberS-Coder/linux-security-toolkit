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
💻 Usage & Examples
Note: These utilities require elevated privileges to access system authentication logs (journalctl). Execute them using sudo.

1. Basic SSH Log Analysis
Inspect all failed SSH login attempts across the system, sorted by frequency:

Bash
sudo ./ssh_analyser.sh
2. Threshold-Based SSH Analysis
Filter login failures by specifying a minimum attempt threshold as an argument (defaults to 1 if omitted):

Bash
# Display only IPs with 5 or more failed login attempts
sudo ./ssh_analyser_v2.sh 5
3. Generate Firewall Blacklist
Extract offending IP addresses that meet or exceed a threshold and write them directly to blacklisted_ips.txt:

Bash
# Generate a blacklist for IPs with 3 or more failed attempts
sudo ./generate_blacklist.sh 3
🔬 Systems & Security Concepts Demonstrated
Telemetry & Log Analysis: Transforming unstructured systemd logs (journalctl) into actionable threat intelligence.

Text Processing Pipelines: Chaining UNIX utilities (grep, awk, sort, uniq) using standard output/input pipes (|) to manipulate data efficiently.

Access Control & Defensive Checks: Enforcing execution safety by validating Effective User ID ($EUID == 0) before reading sensitive authentication records.

Input Sanitization & Parameter Expansion: Utilizing fallback expansion syntax (${1:-3}) to handle positional parameters safely and prevent runtime execution errors.

Automated Threat Mitigation: Isolating raw indicators of compromise (IP addresses) into structured text formats ready for firewall (iptables / ufw) ingestion.

👨‍💻 Author
GitHub: @CyberS-Coder

Focus: Cybersecurity, Linux Systems Administration, and Security Automation.

# Architecture & Technical Trade-Offs

This document outlines the core engineering decisions, technical trade-offs, and design rationale behind the Linux Security & Telemetry Toolkit.

## 1. Concurrency Model: `ThreadPoolExecutor` vs. `multiprocessing` / `asyncio`
* **Decision:** Selected Python's `concurrent.futures.ThreadPoolExecutor` for network scanning.
* **Rationale:** Port scanning is strictly **I/O-bound** (waiting on TCP network socket handshakes or timeouts). Threads share memory lightweightly without the memory overhead of spawning separate system processes (`multiprocessing`). While `asyncio` offers high performance, thread pools provide explicit concurrency control with minimal complexity using standard Python libraries.

## 2. Socket Mechanics: TCP Connect vs. Raw SYN Sockets
* **Decision:** Standard TCP socket connections (`socket.SOCK_STREAM`).
* **Rationale:** Raw SYN scanning ("stealth scanning") requires `RAW_SOCKET` permissions (root/sudo). Utilizing `connect_ex()` allows the port scanner to run cleanly in unprivileged user spaces while reliably detecting open ports across local and lab environments.

## 3. Threat Model: Baseline Isolation vs. Root Compromise
* **Decision:** SHA-256 local JSON baseline storage.
* **Rationale:** SHA-256 provides collision-resistant file change detection. However, if an attacker gains root access (`UID 0`), local baseline files can be modified alongside target files. In production settings, baselines must be cryptographically signed, stored on read-only media, or shipped off-host to a SIEM.

## 4. Telemetry Interpretation: Candidate Blocklists vs. "Malicious" IPs
* **Decision:** Labeling high-failure SSH IPs as "suspicious candidates for review."
* **Rationale:** Authentication failures can stem from legitimate user password errors or misconfigured software clients. Labeling IPs as "malicious" without contextual analysis represents bad security rigor; filtering by failure thresholds provides actionable intelligence for human review.

#!/usr/bin/env python3
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                # Attempt service banner grab
                try:
                    s.send(b"Head / HTTP/1.0\r\n\r\n")
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                except Exception:
                    banner = "No banner returned"
                return port, True, banner
    except Exception:
        pass
    return port, False, ""

def main():
    parser = argparse.ArgumentParser(description="Multithreaded TCP Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or hostname")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g. 1-1024)")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Number of concurrent threads")
    parser.add_argument("--timeout", type=float, default=1.0, help="Socket connection timeout in seconds")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"Error: Could not resolve hostname {args.target}")
        return

    start_port, end_port = map(int, args.ports.split("-"))
    print(f"Scanning target {args.target} ({target_ip}) on ports {start_port}-{end_port}...")

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [
            executor.submit(scan_port, target_ip, port, args.timeout)
            for port in range(start_port, end_port + 1)
        ]

        for future in futures:
            port, is_open, banner in future.result()
            if is_open:
                print(f"Port {port:<5} OPEN | Service Banner: {banner}")

if __name__ == "__main__":
    main()

import socket
from concurrent.futures import ThreadPoolExecutor

def port_scan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port number {port} is open.")

        # Try to grab the service banner
        try:
            # Set a slightly shorter timeout for reading data
            s.settimeout(1.0)

            # Some services require a newline prompt to speak, others speak immediately.
            # We attempt to receive up to 1024 bytes of data.
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            if banner:
                print(f" | Banner: {banner}")
            else:
                print() # Just print newline if open but no banner received
        except:
            print() # If timeout or decoding fails, just close cleanly

    s.close()


host_input = input("Enter the Target IP or domain name: ")

try:
    target = socket.gethostbyname(host_input)
    print(f"Resolved {host_input} to IP: {target}")
except:
    print(f"Error: Could not resolve hostname '{host_input}'")
    exit(1)

print(f"Scanning target IP of: {target}")

try:
    first_port = int(input("Enter start port (1-65535): "))
    last_port = int(input("Enter end port (1-65535): "))
except ValueError:
    print("Error: Port numbers must be valid integers.")
    exit(1)

# Validate port ranges
if not (1 <= first_port <= 65535) or not (1 <= last_port <= 65535):
    print("Error: Port numbers must be between 1 and 65535.")
    exit(1)

if first_port > last_port:
    print("Error: Start port cannot be greater than end port.")
    exit(1)

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(port_scan, range(first_port, last_port+1))

print("Scan complete")

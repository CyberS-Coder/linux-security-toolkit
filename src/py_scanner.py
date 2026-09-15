import socket

target = "127.0.0.1"
port = 22  # SSH service

# 1. Create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1.0)

# 2. Attempt connection
result = s.connect_ex((target, port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED (Error Code: {result})")

# 3. Release resources
s.close()

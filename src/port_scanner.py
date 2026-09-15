def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)

            if sock.connect_ex((host, port)) != 0:
                return port, False, ""

            banner = "No banner returned"

            try:
                sock.sendall(
                    b"HEAD / HTTP/1.0\r\n"
                    b"Host: localhost\r\n"
                    b"Connection: close\r\n\r\n"
                )
                banner_data = sock.recv(1024)
                banner = banner_data.decode("utf-8", errors="replace").strip()
            except (socket.timeout, OSError):
                pass

            return port, True, banner

    except (socket.timeout, OSError):
        return port, False, ""

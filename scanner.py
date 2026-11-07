import socket

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        return result == 0

if __name__ == "__main__":
    print("Port 8000:", check_port("127.0.0.1", 8000))
    print("Port 9999:", check_port("127.0.0.1", 9999))


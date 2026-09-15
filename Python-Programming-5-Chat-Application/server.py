import socket
import threading

HOST = "127.0.0.1"
PORT = 5000
clients = []
lock = threading.Lock()


def broadcast(message, sender=None):
    with lock:
        for client in clients[:]:
            if client is sender:
                continue
            try:
                client.sendall(message.encode("utf-8"))
            except OSError:
                clients.remove(client)
                client.close()


def handle_client(conn, address):
    name = None
    try:
        conn.sendall(b"Enter your name: ")
        name = conn.recv(1024).decode("utf-8").strip() or f"User-{address[1]}"
        with lock:
            clients.append(conn)
        broadcast(f"{name} joined the chat.\n", conn)
        conn.sendall(b"Connected! Type messages and press Enter.\n")

        while True:
            data = conn.recv(4096)
            if not data:
                break
            text = data.decode("utf-8").strip()
            if text:
                broadcast(f"{name}: {text}\n", conn)
    except (ConnectionResetError, OSError):
        pass
    finally:
        with lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()
        if name:
            broadcast(f"{name} disconnected.\n")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Chat server listening on {HOST}:{PORT}")
        while True:
            conn, address = server.accept()
            threading.Thread(target=handle_client, args=(conn, address), daemon=True).start()


if __name__ == "__main__":
    main()

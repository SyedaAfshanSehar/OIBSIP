import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(4096)
            if not message:
                print("Server disconnected.")
                break
            print(message.decode("utf-8"), end="")
        except OSError:
            break


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        prompt = sock.recv(1024).decode("utf-8")
        print(prompt, end="")
        name = input()
        sock.sendall(name.encode("utf-8"))

        threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()
        while True:
            try:
                text = input()
            except (EOFError, KeyboardInterrupt):
                break
            if text.lower() in {"/quit", "/exit"}:
                break
            if text.strip():
                try:
                    sock.sendall(text.encode("utf-8"))
                except OSError:
                    break


if __name__ == "__main__":
    main()

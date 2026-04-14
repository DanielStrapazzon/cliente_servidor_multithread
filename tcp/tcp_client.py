import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
NUM_REQUESTS = 50


def send_request(i):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    msg = f"Mensagem TCP {i}"
    client.send(msg.encode())

    response = client.recv(1024).decode()

    print(f"[TCP CLIENT] Req {i}: {response}")

    client.close()


threads = []

for i in range(NUM_REQUESTS):
    t = threading.Thread(target=send_request, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
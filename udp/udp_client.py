import socket
import threading

HOST = '127.0.0.1'
PORT = 5001
NUM_REQUESTS = 50


def send_request(i):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    msg = f"Mensagem UDP {i}"
    client.sendto(msg.encode(), (HOST, PORT))

    response, _ = client.recvfrom(1024)

    print(f"[UDP CLIENT] Req {i}: {response.decode()}")

    client.close()


threads = []

for i in range(NUM_REQUESTS):
    t = threading.Thread(target=send_request, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
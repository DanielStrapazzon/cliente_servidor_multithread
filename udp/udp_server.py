import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 5001


def handle_request(data, addr, server):
    msg = data.decode()

    print(f"[UDP] Processando {addr}: {msg}")

    time.sleep(2)

    response = f"Resposta para {msg}"
    server.sendto(response.encode(), addr)

    print(f"[UDP] Finalizado atendimento de {addr}")


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"[UDP] Servidor escutando em {HOST}:{PORT}")

while True:
    data, addr = server.recvfrom(1024)

    thread = threading.Thread(target=handle_request, args=(data, addr, server))
    thread.start()
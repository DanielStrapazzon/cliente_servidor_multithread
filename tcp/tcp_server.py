import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 5000


def handle_client(conn, addr):
    print(f"[TCP] Cliente conectado: {addr}")

    data = conn.recv(1024).decode()

    print(f"[TCP] Processando requisição de {addr}: {data}")

    time.sleep(2)

    response = f"Resposta para {data}"
    conn.send(response.encode())

    print(f"[TCP] Finalizado atendimento de {addr}")

    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[TCP] Servidor escutando em {HOST}:{PORT}")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
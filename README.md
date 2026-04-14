TCP

Terminal 1:
python tcp_server.py

Terminal 2:
python tcp_client.py

UDP

Terminal 1:
python udp_server.py

Terminal 2:
python udp_client.py


- Objetivo principal é mostrar que se fossem realizadas as requisições de forma sequencial, para execução de 50 requisições seriam necessários 1 minuto e 66 segundo para termino (50 requisições × 2 segundos = 100 segundos).

- Utilizando o conceito de multithreading de forma aplicada, todas estas requisições terminam em aproximadament 2 à 4 segundos.

- Concluindo ser algo extremamente mais rápido e eficiente.
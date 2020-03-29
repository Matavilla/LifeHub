import socket

# Use ipv4, DataGram socket
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sock.bind(('192.168.54.8', 5050))
ClientData = []
print("StartServer")
while True:
    MesData, MesAd = Sock.recvfrom(1024)
    print(MesAd[0], MesAd[1])
    if MesAd not in ClientData:
        ClientData.append(MesAd)  # Если такова клиента нету , то добавить
    for clients in ClientData:
        if clients == MesAd:
            continue  # Не отправлять данные клиенту который их прислал
        Sock.sendto(MesData, clients)

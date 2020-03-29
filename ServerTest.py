import socket

#socket_famile - AF_INET,socket_type - SOCK_DGRAM, protocol - 0 (by default)
ServSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = "127.0.0.1" #Return host name
Port = 65534
print(Host,Port)
ServSock.bind((Host,Port))
ServSock.listen(5)
ClientData = []
print("StartServer")
while True:
    CliSock, MesAd = ServSock.accept()
    print("Got a connection from %s" % str(MesAd))
    # if MesAd not in ClientData:
    #     ClientData.append(MesAd)  # Если такова клиента нету , то добавить
    # for clients in ClientData:
    #     if clients == MesAd:
    #         continue  # Не отправлять данные клиенту который их прислал
    #     Sock.sendto(MesData, clients)
    msg = 'Thank you for connecting'+ "\r\n"
    CliSock.send(msg.encode('ascii'))
    CliSock.close()
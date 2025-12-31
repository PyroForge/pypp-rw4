import socket
uns = []
HOST = '0.0.0.0'
PORT = 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        try:
            conn, addr = s.accept()

            with conn:
                data = conn.recv(1024)
                if data.decode() == "thebar":
                    data = conn.recv(1024)
                    data = data.decode("utf-8")
                    print(data)
                    data = data.split(" ")
                    x, y, un, lv = data
                    a = open(un + ".pos", "w")
                    a.write(str(data))
                    a.close()
                    a = False
                    for unn in uns:
                        if un == unn:
                            a = True
                        else:
                            pass
                    if a == False:
                        uns.append(un)
                        print(un)
                    if len(uns) > 9:
                        uns = []
                    for unn in uns:
                        a = open(unn + ".pos", "r")
                        q = a.read()
                        print(q)
                        conn.sendall(q.encode("utf-8"))
                        conn.recv(1024)
                    conn.sendall(b"done")
        except:
            print("error")


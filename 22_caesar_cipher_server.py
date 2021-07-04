import socket
import time

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Server listening on port:", port)
s.listen(1)

c, address = s.accept()

print("Connection from:", str(address))

c.send("Jlkqv Mvqelk".encode())
time.sleep(1)
c.send("QEXKH VLR XKFQXYLOD".encode())
time.sleep(1)
c.send("f zlria dl clo pljb QXZLP".encode())
c.close()

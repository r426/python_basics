import socket

s = socket.socket()

s.connect(("localhost", 4000))

msg = s.recv(1024)

while msg:
    original_message = msg.decode()
    separator = ""
    print("Received: ", original_message)
    letters = [
        i if ord(i) == 32 else chr(ord(i) + 3) if 97 <= ord(i) <= 119 or 65 <= ord(i) <= 87 else chr(ord(i) - 23) for
        i in original_message]
    translation = separator.join(letters)
    print("Translated: ", translation)
    msg = s.recv(1024)

s.close()

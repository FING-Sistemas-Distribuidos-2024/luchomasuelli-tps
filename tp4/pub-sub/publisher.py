import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:3001")
print("Server started")
count = 0

topic = b'hola'

while True:
    count += 1
    message = "Mensaje %s" % count

    #socket.send_string(message)
    socket.send_multipart([topic, message.encode("utf8")])
    print("Sent: %s" % message)
    time.sleep(1)

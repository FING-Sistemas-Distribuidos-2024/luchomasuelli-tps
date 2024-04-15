import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
print("Server started")
count = 0

while True:
    count += 1
    message = "Mensaje %s" % count

    socket.send_string(message)
    print("Sent: %s" % message)
    time.sleep(1)

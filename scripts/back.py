import time
from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 9000
client = SimpleUDPClient(ip, port)

while True:
    client.send_message("/input/Vertical", -1.0)
    time.sleep(0.05)
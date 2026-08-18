import time
from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 9000
client = SimpleUDPClient(ip, port)

while True:
    client.send_message("/input/Vertical", 1.0) # 前進
    client.send_message("/input/Run", 1)         # ダッシュON
    time.sleep(0.05)
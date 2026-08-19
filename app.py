import subprocess
import webbrowser
from flask import Flask, render_template, jsonify
# python-osc からクライアントをインポート
from pythonosc.udp_client import SimpleUDPClient

app = Flask(__name__)

current_process = None

osc_client = SimpleUDPClient("127.0.0.1", 9000)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global current_process
    if current_process is None:
        print("【開始】歩行処理を開始")
        current_process = subprocess.Popen(["python", "scripts/run.py"])
    return jsonify({"status": "started"})

@app.route('/dash', methods=['POST'])
def dash():
    global current_process
    if current_process is None:
        print("【開始】ダッシュ処理を開始")
        current_process = subprocess.Popen(["python", "scripts/dash.py"])
    return jsonify({"status": "started"})

@app.route('/back', methods=['POST'])
def back():
    global current_process
    if current_process is None:
        print("【開始】バック処理を開始")
        current_process = subprocess.Popen(["python", "scripts/back.py"])
    return jsonify({"status": "started"})

@app.route('/stop', methods=['POST'])
def stop():
    global current_process
    if current_process is not None:
        print("【停止】移動処理を強制終了")
        current_process.terminate()  # プロセスを終了
        current_process.wait()       # 完全に終了するまで待つ
        current_process = None

    for _ in range(3):
        osc_client.send_message("/input/Vertical", 0.0)
        osc_client.send_message("/input/Run", 0)  # ダッシュ入力も解除
    
    print("【送信】停止信号 (Vertical: 0.0 / Run: 0) を送信しました")
    return jsonify({"status": "stopped"})

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run(port=5000)
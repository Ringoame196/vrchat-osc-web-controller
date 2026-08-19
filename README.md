# VRChat OSC Web Controller (vrc-web-walker)

Webブラウザ上のボタン操作によって、VRChat内のアバターを移動（歩行・ダッシュ）させるためのOSCコントローラーツールです。

Python (Flask) でWebサーバーを起動し、ブラウザからの操作を受け取って `python-osc` 経由でVRChatに信号を送信します。

## 📌 前提条件

本ツールの使用には **Python (3.x 以上)** のインストールが必要です。  
未インストールの場合は、[Python公式サイト](https://www.python.org/) からダウンロードしてインストールを行ってください。  
*(※Windowsでのインストール時、「Add python.exe to PATH」にチェックを入れることを推奨します)*


---

## 📁 フォルダ構成

```text
.
├── app.py              # メインWebサーバー（Flask）
├── requirements.txt    # 必要なPythonライブラリ一覧
├── setup.bat           # ワンクリックで環境構築するWindows用バッチ
├── run.bat             # 起動用のWindows用バッチ
│
├── scripts/            # OSC実行スクリプト
│   ├── run.py          # 前進（歩行）処理
│   ├── dash.py         # ダッシュ処理
    └── back.py         # バック処理
│
├── static/             # 静的ファイル
│   ├── css/
│   │   └── index.css   # スタイルシート
│   └── js/
│       └── main.js     # JavaScript（操作イベント・通信処理）
│
└── templates/          # HTMLテンプレート
    └── index.html      # 操作画面
```

---

## 🚀 使い方

### 1. 準備・インストール

以下のいずれかの方法で必要なライブラリをインストールします。

* **Windowsの場合（おすすめ）**:  
  `setup.bat` をダブルクリックするだけで自動インストールされます。

### 2. VRChatの設定を確認

1. VRChatを起動し、インゲームのアクションメニュー（円形メニュー）を開きます。
2. **Options** > **OSC** > **Enabled** にして、OSC機能を有効化します。

---

### 3. アプリケーションの起動

以下のコマンドを実行してWebサーバーを立ち上げます。

```bash
python app.py
```

起動すると、自動的にブラウザが開いて操作画面（ `http://127.0.0.1:5000` ）が表示されます。

---

## 🎮 操作方法

* **歩く（直進）ボタン**: 押している間だけアバターが前進します。
* **ダッシュボタン**: 押している間だけアバターがダッシュ前進します。
* **ボタンを離す / フォーカス外れ**: 自動的に移動が停止（0.0送信）します。

---

## 🛠️ 使用技術・ライブラリ

* **Python 3.x**
* **Flask** (Web API / サーバー)
* **python-osc** (VRChatとのUDP通信)
* **HTML / CSS / JavaScript** (UI・イベント処理)

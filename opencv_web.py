# -*- coding: utf-8 -*-
import cv2
from flask import Flask, Response, render_template, jsonify
from send_gazo import save_image, send_gazo
import threading

# Webカメラ
DEVICE_ID = 2
WIDTH = 1920
HEIGHT = 1080
FPS = 30

app = Flask(__name__)

# カメラ初期化
camera = cv2.VideoCapture(DEVICE_ID)

# カメラのフォーマット・解像度・FPSの設定
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
camera.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
camera.set(cv2.CAP_PROP_FPS, FPS)

# グローバル変数
current_frame = None

# バックグラウンドでカメラ画像を更新
def update_camera():
    global current_frame
    while True:
        success, frame = camera.read()
        if success:
            current_frame = frame

# スレッドを起動
camera_thread = threading.Thread(target=update_camera)
camera_thread.start()

# 画像をキャプチャして保存する関数
def capture_and_save(flag):
    success, frame = camera.read()
    if success:
        frame_name = save_image(frame)
        messages = {
            1: '配達員が来ました。',
            2: '配達員以外の誰かが来ました。',
            3: '現在の状況を撮影しました。'
        }
        send_gazo(frame_name, messages.get(flag, '不明な状況'))

@app.route('/')
def index():
    """メインページを表示"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """ビデオフレームをフィードとして提供"""
    def generate_frames():
        while True:
            success, frame = camera.read()
            if success:
                ret, jpeg = cv2.imencode('.jpg', frame)
                if ret:
                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shoot', methods=['GET', 'POST'])
def save_delivery_image():
    """配達員の画像を保存"""
    capture_and_save(1)

    return jsonify({"message": "画像を保存しました"})

@app.route('/shoot_other',methods=['GET', 'POST'])
def save_other_image():
    """配達員以外の画像を保存"""
    capture_and_save(2)

    return jsonify({"message": "画像を保存しました"})

@app.route('/execute', methods=['POST'])
def save_current_image():
    """現在の状況の画像を保存"""
    capture_and_save(3)

    return "現在の状況を撮影しました。"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)

# -*- coding: utf-8 -*-
import cv2
import requests
import key
import datetime

# Webカメラ
DEVICE_ID = 2
WIDTH = 1920
HEIGHT = 1080
FPS = 30

def save_image(fr):
    now = datetime.datetime.now()
    filename = './images/' + now.strftime('%Y%m%d_%H%M%S') + '.jpg'
    cv2.imwrite(filename, fr)
    return filename

def send_gazo(fn,ms):
    url = "https://notify-api.line.me/api/notify"
    token = key.TK
    headers = {"Authorization" : "Bearer "+ token}

    payload = {"message" :  ms}
    #imagesフォルダの中のgazo.jpg
    files = {"imageFile":open(fn,'rb')}
    #rbはバイナリファイルを読み込む
    requests.post(url ,headers = headers ,params=payload,files=files)

def main():
    camera = cv2.VideoCapture(DEVICE_ID)  # デフォルトカメラを使用

    # フォーマット・解像度・FPSの設定
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    #camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    camera.set(cv2.CAP_PROP_FPS, FPS)
    
    _, frame = camera.read()
    filename = save_image(frame)
    camera.release()
    send_gazo(filename,'これはテストです。')


if __name__ == '__main__':
    main()
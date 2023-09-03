# -*- coding: utf-8 -*-
import speech_recognition as sr

def recognize_speech_from_mic():
    # 音声認識オブジェクトの初期化
    recognizer = sr.Recognizer()

    # マイクからの入力を使用
    with sr.Microphone() as source:
        #print("話してください...")
        audio_data = recognizer.listen(source)
        #print("認識中...")

    try:
        # Googleの音声認識APIを使って認識
        text = recognizer.recognize_google(audio_data, language='ja-JP')
        return text

    except sr.UnknownValueError:
        return False
    except sr.RequestError as e:
        return False

def main():
    recognized_text = recognize_speech_from_mic()
    print(recognized_text)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import StringVar
from key_open import key_open
from voice_to_text import recognize_speech_from_mic
from cipher import verify_phrase_with_gpt3
import time

def cipher_screen():
    
    def input_cipher():
        text = recognize_speech_from_mic()
        if text:
            input_text.set(text)
            if verify_phrase_with_gpt3(text) == 'はい':
                key_open()
                result.set('OPEN')
            else:
                result.set('合言葉が違います。')

        else:
            input_text.set('音声を確認できませんでした。')
            result.set('FAILED')
        root.after(3000, lambda: root.destroy())
	
    root = tk.Tk()
    root.title('合言葉')
    root.geometry("1000x300+460+390")

    input_text = StringVar()
    input_text.set('')
    result = StringVar()
    result.set('')

    label1 = tk.Label(root, text='合言葉は？', font=('',30))   #wordの中身をlabelで表示
    label2 = tk.Label(root, textvariable=input_text, font=('',30))   #wordの中身をlabelで表示
    label3 = tk.Label(root, textvariable=result, font=('',30))   #wordの中身をlabelで表示
    label1.pack(anchor='center',expand=1)
    label2.pack(anchor='center',expand=1)
    label3.pack(anchor='center',expand=1)

    root.after(100, input_cipher)

    #30秒後にウインドウを閉じる
    root.after(30000, lambda: root.destroy())
    root.mainloop()

def main():
	cipher_screen()

if __name__ == '__main__':
	main()
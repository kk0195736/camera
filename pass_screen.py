# -*- coding: utf-8 -*-
import tkinter as tk
from key_open import key_open
import threading
import key

def pass_screen():
    pass_input = []
    
    def key_handler(e):
        pass_input.append(e.char)
        print(pass_input)
        if len(pass_input) == 1:
            label2['text'] = '＊            '
        elif len(pass_input) == 2:
            label2['text'] = '＊   ＊        '
        elif len(pass_input) == 3:
            label2['text'] = '＊   ＊   ＊    '
        elif len(pass_input) == 4:
            label2['text'] = '＊   ＊   ＊   ＊'
            if pass_input == list(key.PW):
                label3['text'] = 'OPEN'
                thread1 = threading.Thread(target=key_open)
                thread1.start()
                root.after(3000, lambda: root.destroy())
            else:
                label3['text'] = 'FAILED'
                root.after(1000, lambda: root.destroy())
        else:
            pass
	
    root = tk.Tk()
    root.title('暗証番号')
    root.geometry("1000x300+460+390")
    label1 = tk.Label(root, text='パスワードを入力してください。', font=('',30))   #wordの中身をlabelで表示
    label2 = tk.Label(root, text='             ', font=('',30))   #wordの中身をlabelで表示
    label3 = tk.Label(root, text='', font=('',30))   #wordの中身をlabelで表示
    label1.pack(anchor='center',expand=1)
    label2.pack(anchor='center',expand=1)
    label3.pack(anchor='center',expand=1)

    root.bind("<KeyPress>", key_handler)

    #30秒後にウインドウを閉じる
    root.after(30000, lambda: root.destroy())
    root.mainloop()

def main():
	pass_screen()

if __name__ == '__main__':
	main()
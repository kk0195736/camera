# -*- coding: utf-8 -*-
import tkinter as tk
import subprocess
import requests
import threading
from pass_screen import pass_screen
from display_message import display_message

def standby_screen():
    
    def key_handler(e):
        if e.char == '1':
            url = "http://localhost:8080/shoot"
            
            thread1 = threading.Thread(target=display_message, args=('メッセージ','只今呼び出し中です。少々お待ちください。'))
            thread1.start()

            subprocess.Popen(['python3','./BGM/child1.py'])

            requests.get(url)
        
        elif e.char == '2':
            url = "http://localhost:8080/shoot_other"
            
            thread2 = threading.Thread(target=display_message, args=('メッセージ','只今呼び出し中です。少々お待ちください。'))
            thread2.start()
            
            subprocess.Popen(['python3','./BGM/child2.py'])

            requests.get(url)

        elif e.char == '.':
            pass_screen()

        else:
            pass
	
    root = tk.Tk()
    root.title('インターホン')
    root.geometry("1000x300+460+390")
    label1 = tk.Label(root, text='配達員の方は「１」を押してください。', font=('',30))   #wordの中身をlabelで表示
    label2 = tk.Label(root, text='それ以外の方は「２」を押してください。', font=('',30))   #wordの中身をlabelで表示
    label1.pack(anchor='center',expand=1)
    label2.pack(anchor='center',expand=1)

    root.bind("<KeyPress>", key_handler)

    root.mainloop()

def main():
	standby_screen()

if __name__ == '__main__':
	main()
# -*- coding: utf-8 -*-
import tkinter as tk

def display_message(title,txt):
    root = tk.Tk()
    root.title(title)
    root.geometry("1000x200+460+440")
    label = tk.Label(root, text=txt, font=('',30))   #wordの中身をlabelで表示
    label.pack(anchor='center',expand=1)
    #5秒後にウインドウを閉じる
    root.after(5000, lambda: root.destroy())
    root.mainloop()

def main():
	display_message('メッセージ', '只今呼び出し中です。少々お待ちください。')

if __name__ == '__main__':
	main()
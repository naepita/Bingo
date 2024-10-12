import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title(u"BINGO!")
root.geometry("400x300")

#1~75のランダムな配列を作成 
num_list = random.sample(range(1, 76), 75)
index = tk.IntVar()
index.set(0)
log_list = []

#スタートボタンが押された時の処理
def start():
    #現在のインデックスを所得
    current_index = index.get()

    if current_index < 75:
        #数字と履歴を書き換える
        num_log.insert(tk.END, num_list[current_index])
        bingo_num.config(text=str(num_list[current_index]))

        #インデックス番号を1増やす
        index.set(current_index + 1)

    #すべての表示が終わったらメッセージを表示する
    else:
        message()



#リセットボタンが押された時の処理
def reset():
    #インデックスを初期化
    index.set(0)

    #履歴を削除
    num_log.delete(0, tk.END)

    #ランダムな配列を作り直す
    global num_list 
    num_list = random.sample(range(1, 76), 75)

    #表示を元に戻す
    bingo_num.config(text="?")

def message():
    messagebox.showwarning("警告", "すべての表示が完了しました。\nリセットしてください。")

#フレームを作成    
frame = tk.Frame(root, bg="red")
frame.place(relx=0.0, rely=0.0, relheight=0.8, relwidth=1.0)
buttons_frame = tk.Frame(root, bg="blue")
buttons_frame.place(relx=0.0, rely=0.8, relheight=0.2, relwidth=1.0)

#ゲームを開始するボタンを作成
start_button = tk.Button(buttons_frame, text ="スタート", font=("Arial", 20) ,command=start)
start_button.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.5)

#ゲームをリセットするボタンを作成
reset_button = tk.Button(buttons_frame, text="リセット", font=("Arial", 20), command=reset)
reset_button.place(relx=0.5, rely=0.0, relheight=1.0, relwidth=0.5)

#数字を表示するラベルを作成
num_label = tk.Label(frame, text="Bingo number", font=("Arial", 14), relief="raised", borderwidth=1)
num_label.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=0.8)
bingo_num = tk.Label(frame, text="?", font=("Arial", 128), bg="lightblue")
bingo_num.place(relx=0.0, rely=0.1, relheight=0.9, relwidth=0.8)


#数字の履歴を表示するリストボックスを作成
log_label = tk.Label(frame, text="履歴", font=("Aeial", 14), relief="raised", borderwidth=1)
log_label.place(relx=0.8, rely=0.0, relheight=0.1, relwidth=0.2)
scrollbar = tk.Scrollbar(frame, bg="blue")
num_log = tk.Listbox(frame, font=("Arial", 14), yscrollcommand=scrollbar.set)
num_log.place(relx=0.8, rely=0.1, relheight=0.9, relwidth=0.15)
scrollbar.place(relx=0.95, rely=0.1, relheight=0.9, relwidth=0.05)
scrollbar.config(command=num_log.yview)

root.mainloop()





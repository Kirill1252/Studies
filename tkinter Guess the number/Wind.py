import random
import tkinter as tk
from tkinter import messagebox

a = random.randint(1, 10)


def enty_func():
    global a
    numbers = int(inp_entry.get())
    print(f"{a} число")
    if a > numbers:
        label2.configure(text="Загаданное число больше!")

    elif a < numbers:
        label2.configure(text=f"Загаданное число меньше...")

    elif a == numbers:
        victory()

    else:
        print("Приходите попозже")


def comparison():
    click()
    enty_func()


count = 0


def click():
    global count
    while count < 3:
        count += 1
        print(f" Попытка №{count}")

        if count < 3:
            label3.configure(text=f"У вас 3-и попытки. Потытка №{count}")
        elif count == 3:
            no_try()
        else:
            print("end")
        break


def error():
    try:
        comparison()

    except ValueError:
        label3.configure(text="Введите число от 1 до 10!")


def no_try():
    m_box = tk.messagebox.showinfo("Конец", "Попыток больше нет !")
    win.destroy()


def victory():
    m_box = tk.messagebox.showinfo("ПОЗДРАВЛЯЮ", "ВЫ УГАДАЛИ!!!")
    win.destroy()


win = tk.Tk()
win.title("Давай сыграем в игру")
win.geometry("350x220+550+200")
win.resizable(False, False)
photo = tk.PhotoImage(file="icon/average.png")
win.iconphoto(False, photo)
win.config(bg='#070909')
label1 = tk.Label(win, text='Угадай число  от 1 да 10',
                  bg='#070909',
                  fg='#FDF5E6',
                  font=('Arial', '15')
                  )
label2 = tk.Label(win, text="Готов испытать удачу???",
                  bg='#070909',
                  fg='#FDF5E6',
                  font=('Arial', '15')
                  )
label3 = tk.Label(win, text="У вас 3-и попытки",
                  bg='#070909',
                  fg='#FDF5E6',
                  font=('Arial', '15')
                  )
inp_entry = tk.Entry(win, font=('Arial', '20'),
                     width=10,
                     justify=tk.CENTER,

                     )
btn1 = tk.Button(win, text='Начать ИГРУ',
                 command=error,
                 padx=70,
                 pady=30,
                 anchor="s")

label1.pack()
inp_entry.pack()
label2.pack()
label3.pack()
btn1.pack()

win.mainloop()

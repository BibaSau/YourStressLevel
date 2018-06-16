def output(event):
        u = ent.get()
        if u == "10":
                tex.delete(1.0, END)
                tex.insert(END, "У Вас повышенный уровень стресса. Расслабьтесть. Экзамены-это только проверка Ваших знаний. Медитируйте. Постарайтесь избегать стрессовых ситуаций")
        elif u == "9":
                tex.delete(1.0, END)
                tex.insert(END, "У Вас повышенный уровень стресса. Расслабьтесть. Экзамены-это только проверка Ваших знаний. Медитируйте. Постарайтесь избегать стрессовых ситуаций")
        elif u == "8":
                tex.delete(1.0, END)
                tex.insert(END, "У Вас повышенный уровень стресса. Расслабьтесть. Экзамены-это только проверка Ваших знаний. Медитируйте. Постарайтесь избегать стрессовых ситуаций")
        elif u == "7":
                tex.delete(1.0, END)
                tex.insert(END, "Средний уровень стресса. Чаще пейте воду и выходте на улицу ради освежения Ваших мозгов")
        elif u == "6":
                tex.delete(1.0, END)
                tex.insert(END, "Средний уровень стресса. Чаще пейте воду и выходте на улицу ради освежения Ваших мозгов")
        elif u == "5":
                tex.delete(1.0, END)
                tex.insert(END, "Средний уровень стресса. Чаще пейте воду и выходте на улицу ради освежения Ваших мозгов")
        elif u == "4":
                tex.delete(1.0, END)
                tex.insert(END, "Поздравляю! Низкий уровень стресса. Используйте это для подготовки к экзаменам")
        elif u == "3":
                tex.delete(1.0, END)
                tex.insert(END, "Поздравляю! Низкий уровень стресса. Используйте это для подготовки к экзаменам")
        elif u == "2":
                tex.delete(1.0, END)
                tex.insert(END, "Поздравляю! Низкий уровень стресса. Используйте это для подготовки к экзаменам")
        elif u == "1":
                tex.delete(1.0, END)
                tex.insert(END, "Поздравляю! Низкий уровень стресса. Используйте это для подготовки к экзаменам")
        elif u == "0":
                tex.delete(1.0, END)
                tex.insert(END, "Поздравляю! Низкий уровень стресса. Используйте это для подготовки к экзаменам")
        else:
                tex.delete(1.0, END)
                tex.insert(END, "Вы уверены,что ввели цифру от 1 до 10?")
                

from tkinter import *     
          
root = Tk()
root.title("Твой уровень стресса")
root.minsize(800,600)
root.resizable(width = False, height = False)

label1 = Label(root, text = "Привет! Давай проверим твой уровень стресса!", font = "Arial 18", fg = "red", bg="white").grid(row = 1)
label2 = Label(root, text = "1.Подолгу ли ты переживаешь из-за неприятностей?", font = "Arial 18").grid(row = 2)
label3 = Label(root, text = "2.Думаешь ли ты о своих проблемах даже в свободное время?", font = "Arial 18").grid(row = 3)
label4 = Label(root, text = "3.Можно ли сказать, что ты вечно спешишь?", font = "Arial 18").grid(row = 4)
label5 = Label(root, text = "4.Бывает, что во время разговора мысли витают где-то далеко?", font = "Arial 18").grid(row = 5)
label6 = Label(root, text = "5.Кажется ли тебе, что люди говорят о пустых и скучных вещах?", font = "Arial 18").grid(row = 6)
label7 = Label(root, text = "6.Приходится тебе делать несколько вещей одновременно?", font = "Arial 18").grid(row = 7)
label8 = Label(root, text = "7.Нервничаешь ли ты стоя в очереди?", font = "Arial 18").grid(row = 8)
label9 = Label(root, text = "8.Долго ли ты колеблешься перед принятием важного решения?", font = "Arial 18").grid(row = 9)
label10 = Label(root, text = "9.Вы говорите торопливо?", font = "Arial 18").grid(row = 10)
label11 = Label(root, text = "10.Последнее время сонливы даже если спали 8 часов?", font = "Arial 18").grid(row = 11)
label12 = Label(root, text = "Сколько раз Вы ответили ДА? Введите ниже и нажмите кнопку ОТВЕТИТЬ", font = "Arial 18").grid(row = 12)


ent = Entry(root, width = 20, bd = 20)
tex = Text(root, width=30, height=5, font="12", wrap=WORD)
but = Button(root, text = "ОТВЕТИТЬ", bg="yellow",fg="green", width = 20, height = 2)

ent.grid(row=13, column=0, padx=10)
but.grid(row=7, column=2)
tex.grid(row=1, column=2, padx=5, pady=20)
 
but.bind("<Button-1>", output)

root.mainloop() 

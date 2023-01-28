import tkinter

# Создаем окно
root = tkinter.Tk()
root.title("Мой Paint")

# Создаем переменные
brush_color = "black"

# Функция рисования
def paint(event):
    # Рисуем на canvas
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Создаем панель инструментов
toolbar_frame = tkinter.Frame(root, bg="gray")

# Создаем кнопки для панели инструментов
black_btn = tkinter.Button(toolbar_frame, text="Черный", width=6, command=lambda: set_color("black"))
black_btn.pack(side=tkinter.LEFT, padx=2, pady=2)

# Функция для установки цвета
def set_color(new_color):
    global brush_color
    brush_color = new_color

# Создаем полотно для рисования
canvas = tkinter.Canvas(root, bg="white", width=600, height=400)
canvas.pack(fill=tkinter.BOTH, expand=True, padx=6, pady=6)

# Назначаем функцию рисования на полотно
canvas.bind("<B1-Motion>", paint)

# Добавляем панель инструментов на окно
toolbar_frame.pack(side=tkinter.TOP, fill=tkinter.X)

# Запускаем окно
root.mainloop()
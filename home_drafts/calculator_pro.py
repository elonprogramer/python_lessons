from tkinter import *  
  
  
def clicked():  
    res = "Привет {}".format(txt.get())  
    lbl.configure(text=res)  
  
  
window = Tk()  
window.title("Калькулятор PRO")  
window.geometry('500x500')  
lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)  
lblt = Label(window, text="Как вас зовут?")  
lblt.grid(column=1, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=2, row=0)  
btn = Button(window, text="Клик!", command=clicked)  
btn.grid(column=3, row=0)  
window.mainloop()
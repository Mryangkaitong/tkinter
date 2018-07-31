import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')#这里是字母x不是乘号


var=tk.StringVar()

l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()


def print_selection():
    l.config(text='youn have selected'+var.get())
    

rl=tk.Radiobutton(window,text='Option A',
                  variable=var,value='A',
                  command=print_selection)

rl.pack()


r2=tk.Radiobutton(window,text='Option B',
                  variable=var,value='B',
                  command=print_selection)

r2.pack()

r3=tk.Radiobutton(window,text='Option C',
                  variable=var,value='C',
                  command=print_selection)

r3.pack()



window.mainloop()

import tkinter as tk

# must have this 
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('my window')
window.geometry('200x200')#这里是字母x不是乘号

'''
tk.Label(window,text=1).pack(side='top')
tk.Label(window,text=1).pack(side='bottom')
tk.Label(window,text=1).pack(side='right')
tk.Label(window,text=1).pack(side='left')
'''

'''
for i in range(4):
    for j in range(3):
        #tk.Label(window,text=2).grid(row=i,column=j,ipadx=10,ipady=10)
        tk.Label(window,text=2).grid(row=i,column=j,padx=10,pady=10)

'''


tk.Label(window,text=3).place(x=10,y=100,anchor='nw')

window.mainloop()




import tkinter as tk

# must have this 
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('my window')
window.geometry('200x200')#这里是字母x不是乘号



def hit_me():
    #tk.messagebox.showinfo(title='Hi',message='haahahah')
    #tk.messagebox.showwarning(title='Hi',message='warning')
    #tk.messagebox.showerror(title='Hi',message='Error')
    #print(tk.messagebox.askquestion(title='Hi',message='askquestion'))#return 'yes' or 'no'
    #print(tk.messagebox.askyesno(title='Hi',message='askyesno')) #return 'Ture' or 'False'
    print(tk.messagebox.askokcancel(title='Hi',message='askokcancel')) #return 'Ture' or 'False'
    
tk.Button(window,text='hit me',command=hit_me).pack()


window.mainloop()

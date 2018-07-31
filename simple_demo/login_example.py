import tkinter as tk
import pickle
# must have this 
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Welcome to Web')
window.geometry('450x300')#这里是字母x不是乘号


#image
canvas=tk.Canvas(window,height=200,width=500)
image_file=tk.PhotoImage(file='insert.gif')
image=canvas.create_image(200,0,anchor='nw',image=image_file)
canvas.pack(side='top')


#user information
tk.Label(window,text='User name:').place(x=50,y=150)
tk.Label(window,text='Password:').place(x=50,y=190)

var_usr_name=tk.StringVar()
var_usr_name.set('example@gmail')

var_usr_pwd=tk.StringVar()

entry_usr_pwd = tk.Entry(window,textvariable=var_usr_name)
entry_usr_pwd.place(x=160,y=150)

entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)


def usr_login():

    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()

    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)

    except FileNotFoundError:

        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)

    if usr_name in usrs_info:
        if usr_pwd==usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome' ,message='How are you ?'+usr_name)
        else:
            tk.messagebox.showerror(message='Error,you password is wrong,try again.')

    else:
        is_sign_up=tk.messagebox.askyesno('Welcome','You have not sign up yet.Sign up now?')

        if is_sign_up:
            
           sign_up()
           

def sign_up():

    def sign_to_save():
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
        nn=new_name.get()

        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr_info=pickle.load(usr_file)

            if np!=npf:
                tk.messagebox.showerror(message='Error,Password and confirm password must be the same !!!!')

            elif nn in exist_usr_info:
                tk.messagebox.showerror('Error','the user has already signed up!!!!')

            else:
                
                exist_usr_info[nn]=np
                with open('usrs_info.pickle','wb') as usr_file:
                    
                    pickle.dump(exist_usr_info,usr_file)

                tk.messagebox.showinfo(title='Welcome' ,message='You have successfully signed up ')
                window_sign_up.destroy()
    

    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up now')

    
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='User name:').place(x=10,y=10)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)

    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)
    

    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='Confirm password:').place(x=10,y=90)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)
    

    mfirm_sign_up=tk.Button(window_sign_up,text='Sign up',command=sign_to_save).place(x=150,y=130)

#login and sign up button

but_login=tk.Button(window,text='Login',command=usr_login)
but_login.place(x=170,y=230)

but_sign_up=tk.Button(window,text='Sign up',command=sign_up)
but_sign_up.place(x=270,y=230)

window.mainloop()




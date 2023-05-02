#sign up 1.0

from tkinter import *
from tkinter import messagebox
import ast 

root = Tk()
root.title('Sign up')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#DEF
def signup():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()
    
    if password==conform_password:
        try:
            
            file=open('datasheet.txt','r+')
            d=file.read()   
            r=ast.literal_eval(d)
            
            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))
            
            messagebox.showinfo('signup','sucessfully sign up')
        
        except:
            file=open('datasheet.txt','w')
            pp=str({'username':'password'})    
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid','Both Password should match')        




frame = Frame(root,width=350,height=390,bg="#fff")
frame.place(x=480,y=50)

heading = Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=125,y=3)

#-------------------------------------------------------------------------------------------------------------------------------------------
#FOR USERNAME
def on_enter(e):
    user.delete(0,'end')

def on_Leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')

user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_Leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#---------------------------------------------------------------------------------------------------------------------------------------------
#FOR PASSWORD
def on_enter(e):
    code.delete(0,'end')

def on_Leave(e):
    name=code.get()
    if name == '':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')


code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_Leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FOR CONFORM PASSWORD
def on_enter(e):
    conform_code.delete(0,'end')

def on_Leave(e):
    
    if conform_code.get() == '':
        conform_code.insert(0,'Conform Password')


conform_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'Conform Password')
conform_code.bind('<FocusIn>',on_enter)
conform_code.bind('<FocusOut>',on_Leave)        


Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

#--------------------------------------------------------------------------------------------------------------------------
#FOR DOWN
Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label= Label(frame,text='I have an account?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

signin = Button(frame,width=6,text='Sign In',bg='white',fg='#57a1f8',border=0,cursor= 'hand2')
signin.place(x=200,y=340)






root.mainloop()
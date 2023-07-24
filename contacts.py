from tkinter import*
import tkinter 
contacts=tkinter.Tk()
contacts.title("My contacts")
contacts.config(bg = 'SlateGray3')
name=tkinter.StringVar()
number=tkinter.StringVar()
l=Listbox(contacts,selectmode='browse')
l.insert(1,'Abhishek =9352536876')
l.insert(2,'ab=6375720199')
l.insert(3,'a=99988877323')
def add():
    
    
    n = name.get()
    m = number.get()
    print("Conatact added is :" + n)
    print("Contact number is :" +m)
    r=str(n + " = " + m)
    l.insert(4,r)
   


def show():
    i=l.get(l.curselection())
    m=Label(contacts,text=i)
    m.pack(side='left')
    l5=tkinter.Button(contacts,text=" Voice Call",font=("Arial Bold",10)).pack(side='left')
    l6=tkinter.Button(contacts,text="Video Call",font=("Arial Bold",10)).pack(side='left')

def click():
    l0=tkinter.Label(contacts,text="  ",font=("Arial Bold",20),bg="SlateGray3",fg="SlateGray3").pack()
    l1=tkinter.Label(contacts,text="name",font=("Arial Bold",20)).pack()
    e1=tkinter.Entry(contacts,textvariable=name,width=20).pack()
    l2=tkinter.Label(contacts,text="contact number",font=("Arial Bold",20)).pack()
    e2=tkinter.Entry(contacts,textvariable=number,width=20).pack()
        
    c1=tkinter.Button(contacts,text="Save",font=("Arial Bold",20),fg="Blue",bg="Black",command=add).pack()
def click1():
    l4=tkinter.Label(contacts,text="contact list",font=("Arial Bold",10)).place(x=200 ,y=180)
    l3=tkinter.Label(contacts,text=" ",font=("Arial Bold",20),bg="SlateGray3",fg="SlateGray3").pack()
    l.place(x=200,y=200)
  
c2=tkinter.Button(contacts,text="My contacts",font=("Arial Bold",20),fg="Blue",bg="Black",command=click1).pack()
c3=tkinter.Button(contacts,text="New contact",font=("Arial Bold",20),fg="Blue",bg="Black",command=click).pack()
c4=tkinter.Button(contacts,text="Select",font=("Arial Bold",20),fg="Blue",bg="Black",command=show).pack()
contacts.mainloop()

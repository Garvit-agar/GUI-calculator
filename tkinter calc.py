# importing tkinter
from tkinter import *

#creating global variable
a=""

#defining function for getting digits
def click(num):
    if "." in e.get() and num==".":
        pass
    else:
        e.insert(END, str(num))

#defining function for calculator operations
def calc(op):
    global a
    b=e.get()

    for i in range(len(b)):
        if b[i] == "0":
            continue
        else:
            b = b[i:]
            break

    a+=b
    if a!="":
        if a[-1] not in ["+","-","/","*"]:
            a=str(eval(a))
        else:
            a=a[:len(a)-1]
        if op=="+":
            a=a+"+"
        elif op=="-":
            a=a+"-"
        elif op=="X":
            a=a+"*"
        elif op=="/":
            a=a+"/"

        e.delete(0,END)

#function to evaluate final result
def ev(op):
    global a
    if a!="":
        if a[-1] in ["+", "-", "/", "*"] and e.get()!=".":
            if type(eval(e.get())) in [float,int] :
                x=a[:-1]
                y=e.get()
                if op=="%":
                    if a[-1] in ["+","-"]:
                        a+=str(eval(x+"*"+y+"/100"))
                    elif a[-1]=="*":
                        a+=y+"/100"
                    elif a[-1]=="/":
                        a+=y+"*100"
                else:
                    a+=y
                a = str(eval(a))
        else:
            a="0"
    else:
        a=e.get()
    e.delete(0,END)
    e.insert(0,a )
    a=""
    print(a)

#function for clear entry box and backspace
def clear(com):
    global a
    if com=="clear":
        a=""
        e.delete(0,END)
    elif com=="backspace":
        e.delete(len(e.get())-1,END)




# creating tkinter window
window = Tk()
window.title("CALCULATOR")
window.geometry("500x400")
window.config(bg="grey")

#creating string variables
ent= StringVar()

#creating entry field
e = Entry(window,
          width=50,
          borderwidth= 5,
          textvariable= ent)

#creating frame for buttons
f=Frame(window,
        height=200,
        width=200,
        borderwidth=10,
        bg="lightgrey",
        padx=20,
        pady=20)

#defining function for buttons
def but(text,n):
    b = Button(f,
               text=text,
               fg="black",
               width=10,
               cursor="hand",
               activeforeground="green",
               pady=10,
               command= lambda : click(n))
    return b

def ex(text,op):
    b = Button(f,
               text=text,
               fg="black",
               width=10,
               cursor="hand",
               activeforeground="green",
               pady=10,
               command=lambda :calc(op))
    return b

def all(text,op):
    b = Button(f,
               text=text,
               fg="black",
               width=10,
               cursor="hand",
               activeforeground="green",
               pady=10,
               command=lambda :ev(op))
    return b

def back(text,com):
    b = Button(f,
               text=text,
               fg="black",
               width=10,
               cursor="hand",
               activeforeground="green",
               pady=10,
               command=lambda :clear(com))
    return b


#placing widgets in sceen
e.pack()
f.pack()

b1=back("AC","clear").grid(row=0,column=0,padx=5,pady=10)
b2=back("<--","backspace").grid(row=0,column=1,padx=5,pady=10)
b3=all("%","%").grid(row=0,column=2,padx=5,pady=10)
b4=ex("/","/").grid(row=0,column=3,padx=5,pady=10)
b5=but("7",7).grid(row=1,column=0,padx=5,pady=10)
b6=but("8",8).grid(row=1,column=1,padx=5,pady=10)
b7=but("9",9).grid(row=1,column=2,padx=5,pady=10)
b8=ex("X","X").grid(row=1,column=3,padx=5,pady=10)
b9=but("4",4).grid(row=2,column=0,padx=5,pady=10)
b10=but("5",5).grid(row=2,column=1,padx=5,pady=10)
b11=but("6",6).grid(row=2,column=2,padx=5,pady=10)
b12=ex("-","-").grid(row=2,column=3,padx=5,pady=10)
b13=but("1",1).grid(row=3,column=0,padx=5,pady=10)
b14=but("2",2).grid(row=3,column=1,padx=5,pady=10)
b15=but("3",3).grid(row=3,column=2,padx=5,pady=10)
b16=ex("+","+").grid(row=3,column=3,padx=5,pady=10)
b17=but("00","00").grid(row=4,column=0,padx=5,pady=10)
b18=but("0",0).grid(row=4,column=1,padx=5,pady=10)
b19=but(".",".").grid(row=4,column=2,padx=5,pady=10)
b20=all("=","=").grid(row=4,column=3,padx=5,pady=10)

#making window visible
window.mainloop()


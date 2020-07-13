from tkinter import*
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=30,borderwidth=5,bg="pink",fg="black")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def buttonclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def badd():
    firstnumber=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(firstnumber)
    e.delete(0,END)

def bmultiply():
    firstnumber=e.get()
    global fnum
    global math
    math="multiply"
    fnum=int(firstnumber)
    e.delete(0,END)

def bsubtract():
    firstnumber=e.get()
    global fnum
    global math
    math="subtraction"
    fnum=int(firstnumber)
    e.delete(0,END)

def bdivide():
    firstnumber=e.get()
    global fnum
    global math
    math="divide"
    fnum=int(firstnumber)
    e.delete(0,END)

    
def bclear():
    e.delete(0,END)

def bequal():
    if math=="addition":
        secondnumber=e.get()
        e.delete(0,END)
        e.insert(0,int(secondnumber)+fnum)
    if math=="subtraction":
        secondnumber=e.get()
        e.delete(0,END)
        e.insert(0,fnum-int(secondnumber))
    if math=="multiply":
        secondnumber=e.get()
        e.delete(0,END)
        e.insert(0,int(secondnumber)*fnum)
    if math=="divide":
        secondnumber=e.get()
        secondnumber=float(secondnumber)
        e.delete(0,END)
        e.insert(0,fnum/int(secondnumber))
            
         

    

button1=Button(root,text="1",padx=40,pady=20,command=lambda: buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: buttonclick(3))

button4=Button(root,text="4",padx=40,pady=20,command=lambda: buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda: buttonclick(6))

button7=Button(root,text="7",padx=40,pady=20,command=lambda: buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: buttonclick(9))

button0=Button(root,text="0",padx=40,pady=20,command=lambda: buttonclick(0))

buttonadd=Button(root,text="+",padx=39,pady=20,command=badd)
buttonclear=Button(root,text="clear",padx=77,pady=20,command=bclear)
buttonequal=Button(root,text="=",padx=86,pady=20,command=bequal)

buttonmultiply=Button(root,text="*",padx=40,pady=20,command=bmultiply)
buttondivide=Button(root,text="/",padx=40,pady=20,command=bdivide)
buttonsubtract=Button(root,text="-",padx=40,pady=20,command=bsubtract)
buttonexit=Button(root, text="Exit Program",command=root.quit)
buttonexit.grid(row=7,column=0,columnspan=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

buttonadd.grid(row=5,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)
buttonequal.grid(row=5,column=1,columnspan=2)

buttonmultiply.grid(row=6,column=0)
buttonsubtract.grid(row=6,column=1)
buttondivide.grid(row=6,column=2)

root.mainloop()

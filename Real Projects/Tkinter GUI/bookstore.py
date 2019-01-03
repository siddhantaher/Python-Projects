from Tkinter import *
# window createtd by initiaiizng
window= Tk()

def km_to_miles():
    miles=e1_value.get()*10
    t1.insert(END,miles)


b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0,rowspan=1)

e1_value= StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

# main code goes in between these two lines
window.mainloop()
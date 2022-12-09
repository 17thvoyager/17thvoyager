from tkinter import *
import parser
root=Tk()
root.title("calculator")

i=0
def fun_get(num):
    global i
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,END)

def fun_operators(operator):

    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else: 
        clear_all()

def Answer():
    entire_string=display.get()
    try:
        variable=parser.expr(entire_string).compile()
        result=eval(variable)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"error")

display=Entry(root)
display.grid(row=1,columnspan=6)

Button(root,text="AC",command=lambda:clear_all()).grid(row=1,column=0)
Button(root,text="^2",command=lambda:fun_operators("**2")).grid(row=1,column=1)
Button(root,text=" +",command=lambda:fun_operators("+")).grid(row=1,column=2)
Button(root,text=" -",command=lambda:fun_operators("-")).grid(row=1,column=3)
Button(root,text=" *",command=lambda:fun_operators("*")).grid(row=1,column=4)

Button(root,text=" 1",command=lambda:fun_get(1)).grid(row=2,column=0)
Button(root,text=" 2",command=lambda:fun_get(2)).grid(row=2,column=1)
Button(root,text=" 3",command=lambda:fun_get(3)).grid(row=2,column=2)
Button(root,text=" 4",command=lambda:fun_get(4)).grid(row=2,column=3)
Button(root,text=" 5",command=lambda:fun_get(5)).grid(row=2,column=4)

Button(root,text=" 6",command=lambda:fun_get(6)).grid(row=3,column=0)
Button(root,text=" 7",command=lambda:fun_get(7)).grid(row=3,column=1)
Button(root,text=" 8",command=lambda:fun_get(8)).grid(row=3,column=2)
Button(root,text=" 9",command=lambda:fun_get(9)).grid(row=3,column=3)
Button(root,text=" 0",command=lambda:fun_get(0)).grid(row=3,column=4)

Button(root,text=" 00",command=lambda:fun_get(00)).grid(row=4,column=0)
Button(root,text=" .",command=lambda:fun_operators(".")).grid(row=4,column=1)
Button(root,text=" /",command=lambda:fun_operators("/")).grid(row=4,column=2)
Button(root,text=" (",command=lambda:fun_operators("(")).grid(row=4,column=3)
Button(root,text=" )",command=lambda:fun_operators(")")).grid(row=4,column=4)

Button(root,text=" pi",command=lambda:fun_operators("3.14" )).grid(row=5,column=0)
Button(root,text=" x!",command=lambda:fun_operators("x!")).grid(row=5,column=1)
Button(root,text=" %",command=lambda:fun_operators("%")).grid(row=5,column=2)
Button(root,text=" =",command=lambda:Answer()).grid(row=5,column=4)
Button(root,text="->",command=lambda:undo()).grid(row=5,column=3)


display.grid(row=0,columnspan=6)


root.mainloop()

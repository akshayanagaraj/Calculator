import tkinter
import postfixeval
global x
x=0
def dispone():
	global x
	a.insert(x,"1")
	x=x+1
def disptwo():
	global x
	a.insert(x,"2")
	x=x+1
def dispthree():
	global x
	a.insert(x,"3")
	x=x+1
def dispzero():
	global x
	a.insert(x,"0")
	x=x+1
def dispmul():
	global x
	a.insert(x,"*")
	x=x+1
def dispfour():
	global x
	a.insert(x,"4")
	x=x+1
def dispfive():
	global x
	a.insert(x,"5")
	x=x+1
def dispsix():
	global x
	a.insert(x,"6")
	x=x+1
def dispseven():
	global x
	a.insert(x,"7")
	x=x+1
def dispeight():
	global x
	a.insert(x,"8")
	x=x+1
def dispnine():
	global x
	a.insert(x,"9")
	x=x+1
def dispplus():
	global x
	a.insert(x,"+")
	x=x+1
def dispdiv():
	global x
	a.insert(x,"/")
	x=x+1
def dispminus():
	global x
	a.insert(x,"-")
	x=x+1
def dispopen():
	global x
	a.insert(x,"(")
	x=x+1
def dispclose():
	global x
	a.insert(x,")")
	x=x+1
def count(w):
	y=0
	while(w>0):
		w=w//10
		y+=1
	return y

def answer():
	global x
	try:
		ans=postfixeval.posteval(a.get())
		a.delete(0,'end')
		a.insert(0,ans)
		x=count(ans)
	except:
		a.delete(0,'end')
		a.insert(0,'Malformed Expression')
def clear():
	global x
	a.delete(0,'end')
	x=0

top=tkinter.Tk()
top.title("calculator")
a=tkinter.Entry(top)
a.grid(row=0,columnspan=5)
one=tkinter.Button(top,text="1",command=dispone)
one.grid(row=1,column=0)
two=tkinter.Button(top,text="2",command=disptwo)
two.grid(row=1,column=1)
three=tkinter.Button(top,text="3",command=dispthree)
three.grid(row=1,column=2)
zero=tkinter.Button(top,text="0",command=dispzero)
zero.grid(row=1,column=3)
mul=tkinter.Button(top,text="*",command=dispmul)
mul.grid(row=1,column=4)
four=tkinter.Button(top,text="4",command=dispfour)
four.grid(row=2,column=0)
five=tkinter.Button(top,text="5",command=dispfive)
five.grid(row=2,column=1)
six=tkinter.Button(top,text="6",command=dispsix)
six.grid(row=2,column=2)
plus=tkinter.Button(top,text="+",command=dispplus)
plus.grid(row=2,column=3)
div=tkinter.Button(top,text="/",command=dispdiv)
div.grid(row=2,column=4)
seven=tkinter.Button(top,text="7",command=dispseven)
seven.grid(row=3,column=0)
eight=tkinter.Button(top,text="8",command=dispeight)
eight.grid(row=3,column=1)
nine=tkinter.Button(top,text="9",command=dispnine)
nine.grid(row=3,column=2)
minus=tkinter.Button(top,text="-",command=dispminus)
minus.grid(row=3,column=3)
equal=tkinter.Button(top,text="=",command=answer)
equal.grid(row=3,column=4)
opene=tkinter.Button(top,text="(",command=dispopen)
opene.grid(row=4,column=0)
close=tkinter.Button(top,text=")",command=dispclose)
close.grid(row=4,column=1)
clear=tkinter.Button(top,text="CLear",command=clear)
clear.grid(row=4,column=2,columnspan=3)
top.mainloop()
# importing necessary packages
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from math import sqrt,factorial,gamma,log,pi,e,sin,cos,tan,asin,acos,atan
from numpy import cbrt
       
# making function for creating scientific calculator tab        
def scientific():
    # defining the function to perform all arithmatical operations
    def check(event):
        text=event.widget.cget("text")
        if(text=="÷"):
            text="/"
        if(text=="x"):
            text="*"
        if(text=="sqrt"):
            text="sqrt"
        if(text=="cbrt"):
            text="cbrt"
        if(text=="ln"):
            text="log"
        if(text=="^"):
            text="**"
        if(text=="π"):
            text="pi"
        if(text=="e"):
            text="e"
        if(text=="1/x"):
            text="1/"
        if(text=="x!"):
            text="factorial"
        if(text=="Γ"):
            text="gamma"
        if(text in ['sin','cos','tan','asin','acos','atan']):
            text=f"{text}"
        if(text=="="):
            if(val.get().isdigit()):
                value=int(val.get())
            else:
                try:
                    value=eval(scr.get())
                except Exception as e:
                    value="ERROR"
            val.set(value)
            scr.update()    
        elif(text=="C"):
            val.set("")
            scr.update()
        elif(text=="DEL"):
            val.set(val.get()[0:(len(val.get())-1)])
            scr.update()
        else:
            val.set(val.get()+text)
            scr.update()
    # creating scientific calculator page
    global nb
    pg=ttk.Notebook(nb)
    # creating the results dialog    
    val=StringVar()
    val.set("")
    scr=Entry(pg,text="",textvar=val)
    scr.grid(row=0,columnspan=50,ipadx=207,ipady=3,sticky=EW)
    # creating the number and operation buttons
    c=0
    for i in range(3,6):
        for j in range(3,6):
            b=tk.Button(pg,text=str(c),height=3,width=12,font=("bold",10))
            b.grid(row=i,column=j-3,sticky=EW)
            b.bind("<Button-1>",check)
            c+=1
    b=tk.Button(pg,text=str(9),height=3,width=12,font=("bold",10))
    b.grid(row=6,column=0,sticky=EW)
    b.bind("<Button-1>",check)
    ops=['*','/','+','-'] # basic arithmatical operators
    opss=["x","÷","+","-"] # symbols of basic arithmatical operators
    funs=['sqrt','cbrt','^'] # special functions
    sym=['π','e'] # pi and Euler's number
    trig=['sin','cos','tan'] # Trigonometric functions
    itrig=['asin','acos','atan'] # inverse trigonometric functions
    # adding and packing the operators
    for i in range(len(ops)):
        b=tk.Button(pg,text=opss[i],height=3,width=12,font=("Lucida",10,"bold"))
        b.grid(row=i+3,column=3,sticky=EW)
        b.bind("<Button-1>",check)
    # adding and packing decimal point button
    b=tk.Button(pg,text=".",height=3,width=12,font=("Lucida",10,"bold"))
    b.grid(row=6,column=1,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing clears the result
    b=tk.Button(pg,text="C",height=3,width=12,font=("bold",10))
    b.grid(row=6,column=2,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing equals button
    b=tk.Button(pg,text="=",height=3,width=12,font=("bold",10))
    b.grid(row=7,column=0,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing special functions
    for i in range(len(funs)):
        if(funs[i]=='**'):
            b=tk.Button(pg,text='^',height=3,width=12,font=("bold",10))
            b.grid(row=7,column=i+1,sticky=EW)
            b.bind("<Button-1>",check)
        else:
            b=tk.Button(pg,text=funs[i],height=3,width=12,font=("bold",10))
            b.grid(row=7,column=i+1,sticky=EW)
            b.bind("<Button-1>",check)
    # adding and packing pi and Euler's number
    for i in range(len(sym)):
        b=tk.Button(pg,text=sym[i],height=3,width=12,font=("bold",10))
        b.grid(row=8,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    # adding and packing natural log button
    b=tk.Button(pg,text="ln",height=3,width=12,font=("bold",10))
    b.grid(row=8,column=2,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing factorial button
    b=tk.Button(pg,text='x!',height=3,width=12,font=("bold",10))
    b.grid(row=8,column=3,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing gamma function
    b=tk.Button(pg,text="Γ",height=3,width=12,font=("bold",10))
    b.grid(row=11,column=3,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing the reciprocal button
    b=tk.Button(pg,text="1/x",height=3,width=12,font=("bold",10))
    b.grid(row=9,column=0,sticky=EW)
    b.bind("<Button-1>",check)
    #adding and packing the trig. and inverse-trig. functions
    for i in range(len(trig)):
        b=tk.Button(pg,text=trig[i],height=3,width=12,font=("bold",10))
        b.grid(row=9,column=i+1,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(len(itrig)):
        b=tk.Button(pg,text=itrig[i],height=3,width=12,font=("bold",10))
        b.grid(row=10,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    # adding and packing modulus operator
    b=tk.Button(pg,text="%",height=3,width=12,font=("bold",10))
    b.grid(row=10,column=3,sticky=EW)
    b.bind("<Button-1>",check)
    # adding and packing brackets
    brk=['(',')']
    for i in range(len(brk)):
        b=tk.Button(pg,text=brk[i],height=3,width=12,font=("bold",10))
        b.grid(row=11,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    # adding and packing the DEL button
    b=tk.Button(pg,text="DEL",height=3,width=12,font=("bold",10))
    b.grid(row=11,column=2,sticky=EW)
    b.bind("<Button-1>",check)
    return(pg)

# making function for creating temperature converter tab 
def temp():
    # creating temperature converter page
    global nb
    pg=ttk.Notebook(nb)
    # creating results dialog
    val=StringVar()
    val.set("")
    scr=Entry(pg,text="",textvar=val)
    scr.grid(row=0,columnspan=20,ipadx=207,ipady=3,sticky=EW)
    # enabling the functions to convert temperature
    def check(event):
        text=event.widget.cget("text")
        if(text=="CEL to FAR"):
            try:
                value=str(float(scr.get())*1.8+32)
            except Exception as e:
                value="ERROR"
        if(text=="CEL to KEL"):
            try:
                value=str(float(scr.get())+273.15)
            except Exception as e:
                value="ERROR"
        if(text=="FAR to CEL"):
            try:
                value=str((float(scr.get())*5-160)/9)
            except Exception as e:
                value="ERROR"
        if(text=="FAR to KEL"):
            try:
                value=str(((float(scr.get())*5-160)/9)+273.15)
            except Exception as e:
                value="ERROR"
        if(text=="KEL to CEL"):
            try:
                value=str(float(scr.get())-273.15)
            except Exception as e:
                value="ERROR"
        if(text=="KEL to FAR"):
            try:
                value=str((float(scr.get())-273.15)*1.8+32)
            except Exception as e:
                value="ERROR"
        if(text=="C"):
            value=""
        if(text=="DEL"):
            value=scr.get()[0:(len(scr.get())-1)] 
        val.set(value)
        scr.update()
    # adding packing the different buttons
    tl=[["CEL to FAR","CEL to KEL","FAR to CEL","FAR to KEL"],["KEL to CEL","KEL to FAR","C","DEL"]]
    for i in range(0,4):
        b=tk.Button(pg,text=tl[0][i],width=12,font=("bold",10))
        b.grid(row=1,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(0,4):
        b=tk.Button(pg,text=tl[1][i],width=12,font=("bold",10))
        b.grid(row=2,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    return(pg)

# making function for creating length converter tab
def length():
    # creating length converter page
    global nb
    pg=ttk.Notebook(nb)
    # creating results dialog
    val=StringVar()
    val.set("")
    scr=Entry(pg,text="",textvar=val)
    scr.grid(row=0,columnspan=20,ipadx=207,ipady=3,sticky=EW)
    # enabling the functions to convert length
    def check(event):
        text=event.widget.cget("text")
        if(text=="m to in"):
            try:
                value=str(float(scr.get())*39.37)
            except Exception as e:
                value="ERROR"
        if(text=="m to ft"):
            try:
                value=str(float(scr.get())*3.28)
            except Exception as e:
                value="ERROR"
        if(text=="m to mi"):
            try:
                value=str(float(scr.get())/1609.34)
            except Exception as e:
                value="ERROR"
        if(text=="in to m"):
            try:
                value=str(float(scr.get())/39.37)
            except Exception as e:
                value="ERROR"
        if(text=="in to ft"):
            try:
                value=str(float(scr.get())/12)
            except Exception as e:
                value="ERROR"
        if(text=="in to mi"):
            try:
                value=str(float(scr.get())/63360)
            except Exception as e:
                value="ERROR"
        if(text=="ft to m"):
            try:
                value=str(float(scr.get())/3.281)
            except Exception as e:
                value="ERROR"
        if(text=="ft to in"):
            try:
                value=str(float(scr.get())*12)
            except Exception as e:
                value="ERROR"
        if(text=="ft to mi"):
            try:
                value=str(float(scr.get())/5280)
            except Exception as e:
                value="ERROR"
        if(text=="mi to m"):
            try:
                value=str(float(scr.get())*1609.34)
            except Exception as e:
                value="ERROR"
        if(text=="mi to in"):
            try:
                value=str(float(scr.get())*63360)
            except Exception as e:
                value="ERROR"
        if(text=="mi to ft"):
            try:
                value=str(float(scr.get())*5280)
            except Exception as e:
                value="ERROR"
        if(text=="C"):
            value=""
        if(text=="DEL"):
            value=scr.get()[0:(len(scr.get())-1)]
        val.set(value)
        scr.update()
    # adding and packing the different buttons
    ll=[["m to in","m to ft","m to mi","in to m"],["in to ft","in to mi","ft to m","ft to in"],
        ["ft to mi","mi to m","mi to in","mi to ft"],["C","DEL"]]
    for i in range(4):
        b=tk.Button(pg,text=ll[0][i],width=12,font=("bold",10))
        b.grid(row=1,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(4):
        b=tk.Button(pg,text=ll[1][i],width=12,font=("bold",10))
        b.grid(row=2,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(4):
        b=tk.Button(pg,text=ll[2][i],width=12,font=("bold",10))
        b.grid(row=3,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(2):
        b=tk.Button(pg,text=ll[3][i],width=12,font=("bold",10))
        b.grid(row=4,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    return(pg)

def mass():
    # creating mass converter page
    global nb
    pg=ttk.Notebook(nb)
    # creating results dialog
    val=StringVar()
    val.set("")
    scr=Entry(pg,text="",textvar=val)
    scr.grid(row=0,columnspan=20,ipadx=207,ipady=3,sticky=EW)
    # enabling the functions to convert mass/weight
    def check(event):
        text=event.widget.cget("text")
        if(text=="kg to oz"):
            try:
                value=str(float(scr.get())*35.27)
            except Exception as e:
                value="ERROR"
        if(text=="kg to lb"):
            try:
                value=str(float(scr.get())*2.204)
            except Exception as e:
                value="ERROR"
        if(text=="kg to mt"):
            try:
                value=str(float(scr.get())/1000)
            except Exception as e:
                value="ERROR"
        if(text=="lb to kg"):
            try:
                value=str(float(scr.get())/2.204)
            except Exception as e:
                value="ERROR"
        if(text=="lb to oz"):
            try:
                value=str(float(scr.get())*16)
            except Exception as e:
                value="ERROR"
        if(text=="lb to mt"):
            try:
                value=str(float(scr.get())/2204.62)
            except Exception as e:
                value="ERROR"
        if(text=="mt to kg"):
            try:
                value=str(float(scr.get())*1000)
            except Exception as e:
                value="ERROR"
        if(text=="mt to oz"):
            try:
                value=str(float(scr.get())*35273.96)
            except Exception as e:
                value="ERROR"
        if(text=="mt to lb"):
            try:
                value=str(float(scr.get())*2204.62)
            except Exception as e:
                value="ERROR"
        if(text=="oz to kg"):
            try:
                value=str(float(scr.get())/35.27)
            except Exception as e:
                value="ERROR"
        if(text=="oz to lb"):
            try:
                value=str(float(scr.get())/16)
            except Exception as e:
                value="ERROR"
        if(text=="oz to mt"):
            try:
                value=str(float(scr.get())/35273.96)
            except Exception as e:
                value="ERROR"
        if(text=="C"):
            value=""
        if(text=="DEL"):
            value=scr.get()[0:(len(scr.get())-1)]
        val.set(value)
        scr.update
    # adding and packing the different buttons
    ml=[["kg to oz","kg to lb","kg to mt","lb to kg"],["lb to oz","lb to mt","mt to kg","mt to oz"],
        ["mt to lb","oz to kg","oz to lb","oz to mt"],["C","DEL"]]
    for i in range(4):
        b=tk.Button(pg,text=ml[0][i],width=12,font=("bold",10))
        b.grid(row=1,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(4):
        b=tk.Button(pg,text=ml[1][i],width=12,font=("bold",10))
        b.grid(row=2,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(4):
        b=tk.Button(pg,text=ml[2][i],width=12,font=("bold",10))
        b.grid(row=3,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(2):
        b=tk.Button(pg,text=ml[3][i],width=12,font=("bold",10))
        b.grid(row=4,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    return(pg)

def curr():
    # creating currency converter page
    global nb
    pg=ttk.Notebook(nb)
    # creating results dialog
    val=StringVar()
    val.set("")
    scr=Entry(pg,text="",textvar=val)
    scr.grid(row=0,columnspan=20,ipadx=207,ipady=3,sticky=EW)
    # enabling the functions to convert currency
    def check(event):
        text=event.widget.cget("text")
        if(text=="₹ to $"):
            try:
                value=str(float(scr.get())/74.63)
            except Exception as e:
                value="ERROR"
        if(text=="₹ to £"):
            try:
                value=str(float(scr.get())/103.09)
            except Exception as e:
                value="ERROR"
        if(text=="$ to ₹"):
            try:
                value=str(float(scr.get())*74.63)
            except Exception as e:
                value="ERROR"
        if(text=="$ to £"):
            try:
                value=str(float(scr.get())/1.39)
            except Exception as e:
                value="ERROR"
        if(text=="£ to ₹"):
            try:
                value=str(float(scr.get())*103.13)
            except Exception as e:
                value="ERROR"
        if(text=="£ to $"):
            try:
                value=str(float(scr.get())*1.39)
            except Exception as e:
                value="ERROR"
        if(text=="C"):
            value=""
        if(text=="DEL"):
            value=scr.get()[0:(len(scr.get())-1)]
        val.set(value)
        scr.update
    # adding and packing the different buttons    
    cl=[["₹ to $","₹ to £","$ to ₹","$ to £"],["£ to ₹","£ to $","C","DEL"]]
    for i in range(4):
        b=tk.Button(pg,text=cl[0][i],width=12,font=("bold",10))
        b.grid(row=1,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    for i in range(4):
        b=tk.Button(pg,text=cl[1][i],width=12,font=("bold",10))
        b.grid(row=2,column=i,sticky=EW)
        b.bind("<Button-1>",check)
    return(pg)
        
# configuring GUI Window
win=tk.Tk()
win.maxsize(432,586)
win.title("CALCULATOR")
win.configure(background="dimgrey")

# a simple help menu button for guidance to new users
def Help():
    showinfo("Guide",'''>> In Scientific Calculator, for functions like sqrt, cbrt, factorial etc. click the required button and then enter the number within brackets like cbrt(x).[For finding reciprocal, click 1/x and then enter the number.] Donot enter the number first and the function later. [Note: All trig. functions are in radian.]
\n>> For temperature converter, enter the required temperature value and click the button corresponding to the desired temperature conversion [Note: You must enter a value for a successful conversion].
\n>> For length converter, enter the required length value and click the button corresponding to the desired length conversion [Note: You must enter a value for a successful conversion].
\n>> For mass/weight converter, enter the required mass/weight value and click the button corresponding to the desired mass/weight conversion [Note: You must enter a value for a successful conversion].
\n>> For currency converter, enter the required currency value and click the button corresponding to the desired currency conversion [Note: You must enter a value for a successful conversion] [Note: Currencies are subject to change. These exchange rates are as per July 14, 2021].
\n(Note:- For any of the different calculators/converters donot enter value like '05','019' etc. otherwise 'ERROR' will be shown)
\n>> Sorry for any inconveniences''')
helpmenu=Menu(win)
helpmenu.add_command(label="Help",command=Help)
win.config(menu=helpmenu)

# creating a tkinter ttk notebook
nb=ttk.Notebook(win)
nb.grid()

# enabling the scientific calculator
page1=scientific()
page1.focus_set()
nb.add(page1,text="Calculator")
# enabling the temperature converter
page2=temp()
page2.focus_set()
nb.add(page2,text="Temperature")
# enabling the length converter
page3=length()
page3.focus_set()
nb.add(page3,text="Length")
# enabling the mass/weight converter
page4=mass()
page4.focus_set()
nb.add(page4,text="Mass/Weight")
# enabling the currency converter
page5=curr()
page5.focus_set()
nb.add(page5,text="Currency")

# enabling the GUI
win.mainloop()

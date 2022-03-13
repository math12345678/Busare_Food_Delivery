import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk

window=tk.Tk()
window.resizable(0,0)
window.geometry("780x800")
window.config(bg="#bde5ed")
window.title("Busare")

font1=font.Font(family="Times New Roman",size=35,weight='bold')#Created the font
font2=font.Font(family="Courier New",size=17)

title=tk.Label(window, text="Busare",font=font1, bg="#bde5ed")#Created the title
title.place(x=300,y=25)

image=Image.open("Busare.jpg")#Loads the image in RAM
image=image.resize((60,60))
photo=ImageTk.PhotoImage(image)#Converts the image into the Tkinter image format
image_label=tk.Label(window,image=photo)
image_label.place(x=425,y=20)

qimage=Image.open("cheesepizza.jpg")#Loads the image in RAM
qimage=qimage.resize((60,60))
qphoto=ImageTk.PhotoImage(qimage)#Converts the image into the Tkinter image format
qimage_label=tk.Label(window,image=qphoto)
qimage_label.place(x=525,y=125)

wimage=Image.open("Chicken pizza.jpg")#Loads the image in RAM
wimage=wimage.resize((60,60))
wphoto=ImageTk.PhotoImage(wimage)#Converts the image into the Tkinter image format
wimage_label=tk.Label(window,image=wphoto)
wimage_label.place(x=525,y=225)

eimage=Image.open("Handmade Pizza.jpg")#Loads the image in RAM
eimage=eimage.resize((60,60))
ephoto=ImageTk.PhotoImage(eimage)#Converts the image into the Tkinter image format
eimage_label=tk.Label(window,image=ephoto)
eimage_label.place(x=525,y=425)

rimage=Image.open("ketchuppackets-1000x600.jpg")#Loads the image in RAM
rimage=rimage.resize((60,60))
rphoto=ImageTk.PhotoImage(rimage)#Converts the image into the Tkinter image format
rimage_label=tk.Label(window,image=rphoto)
rimage_label.place(x=525,y=625)

timage=Image.open("Veggie Pizza.jpg")#Loads the image in RAM
timage=timage.resize((60,60))
tphoto=ImageTk.PhotoImage(timage)#Converts the image into the Tkinter image format
timage_label=tk.Label(window,image=tphoto)
timage_label.place(x=525,y=325)

yimage=Image.open("100_3479.jpg")#Loads the image in RAM
yimage=yimage.resize((60,60))
yphoto=ImageTk.PhotoImage(yimage)#Converts the image into the Tkinter image format
yimage_label=tk.Label(window,image=yphoto)
yimage_label.place(x=525,y=525)

tagline=tk.Label(window,text="Your food will be there, with Busare",bg="#bde5ed")
tagline.place(x=285,y=100)

total=0
item=0
counts1=0
counts2=0
counts3=0
counts4=0
counts5=0
counts6=0
   
def count1():
    global total 
    global item 
    total=total+5
    item=item+1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    global counts1
    counts1=counts1+1
    c1["text"]="Item(s): "+str(counts1)
    
def count2():
    global total 
    global item 
    total=total+6
    item=item+1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    global counts2
    counts2=counts2+1
    c2["text"]="Item(s): "+str(counts2)

def count3():
    global total 
    global item 
    total=total+7
    item=item+1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    global counts3
    counts3=counts3+1
    c3["text"]="Item(s): "+str(counts3)

def count4():
    global total 
    global item 
    total=total+8
    item=item+1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    global counts4
    counts4=counts4+1
    c4["text"]="Item(s): "+str(counts4)
    
def count5():
    global total 
    global item 
    total=total+7
    item=item+1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    global counts5
    counts5=counts5+1
    c5["text"]="Item(s): "+str(counts5)
    
def count6():
    global total 
    global item 
    total=total+0.5
    item=item+1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    global counts6
    counts6=counts6+1
    c6["text"]="Item(s): "+str(counts6)    

def bill():
    global total
    tax=total*8/100
    total=tax+total
    if total>0:
        messagebox.showinfo("Bill","$"+str(total))
    else:
        messagebox.showinfo("Bill","$0")
    
def clear():
    global total
    global item
    global counts1
    global counts2
    global counts3
    global counts4
    global counts5
    global counts6
    total=0
    item=0
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    counts1=0
    counts2=0
    counts3=0
    counts4=0
    counts5=0
    counts6=0
    c1["text"]="Item(s): "+str(counts1)
    c2["text"]="Item(s): "+str(counts2)
    c3["text"]="Item(s): "+str(counts3)
    c4["text"]="Item(s): "+str(counts4)
    c5["text"]="Item(s): "+str(counts5)
    c6["text"]="Item(s): "+str(counts6)
    
def rem1():
    global item
    global total
    global counts1
    item=item-1
    total=total-5
    counts1=counts1-1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    c1["text"]="Item(s): "+str(counts1)
    
def rem2():
    global item
    global total
    global counts2
    item=item-1
    total=total-6
    counts2=counts2-1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    c2["text"]="Item(s): "+str(counts2)
    
def rem3():
    global item
    global total
    global counts3
    item=item-1
    total=total-7
    counts3=counts3-1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    c3["text"]="Item(s): "+str(counts3)
    
def rem4():
    global item
    global total
    global counts4
    item=item-1
    total=total-8
    counts4=counts4-1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    c4["text"]="Item(s): "+str(counts4)
    
def rem5():
    global item
    global total
    global counts5
    item=item-1
    total=total-7
    counts5=counts5-1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    c5["text"]="Item(s): "+str(counts5)
    
def rem6():
    global item
    global total
    global counts6
    item=item-1
    total=total-0.5
    counts6=counts6-1
    items["text"]="Total Item(s): "+str(item)
    amount["text"]="Total Amount: $"+str(total)
    c6["text"]="Item(s): "+str(counts6)

cheese=tk.Label(window,text="Cheese Pizza: $5.00ea",font=font2,bg="#bde5ed")
cheese.place(x=150,y=150)

chicken=tk.Label(window,text="Chicken Pizza: $6.00ea",font=font2,bg="#bde5ed")
chicken.place(x=150,y=250)

veggie=tk.Label(window,text="Veggie Pizza: $7.00ea",font=font2,bg="#bde5ed")
veggie.place(x=150,y=350)

handmade=tk.Label(window,text="Handmade Chicken and Pineapple Pizza: $8.00ea",font=font2,bg="#bde5ed")
handmade.place(x=25,y=450)

pine=tk.Label(window,text="Chicken and Pineapple Pizza: $7.00ea",font=font2,bg="#bde5ed")
pine.place(x=75,y=550)

ketchup=tk.Label(window,text="Ketchup Packets: 50¢ea",font=font2,bg="#bde5ed")
ketchup.place(x=100,y=650)

chebut=tk.Button(window,text="Buy",width=6,height=1,highlightbackground="blue",command=count1)
chebut.place(x=600,y=145)

chibut=tk.Button(window,text="Buy",width=6,height=1,highlightbackground="blue",command=count2)
chibut.place(x=600,y=245)

vebut=tk.Button(window,text="Buy",width=6,height=1,highlightbackground="blue",command=count3)
vebut.place(x=600,y=345)

hanbut=tk.Button(window,text="Buy",width=6,height=1,highlightbackground="blue",command=count4)
hanbut.place(x=600,y=445)

pinbut=tk.Button(window,text="Buy",width=6,height=1,highlightbackground="blue",command=count5)
pinbut.place(x=600,y=545)

ketbut=tk.Button(window,text="Buy",width=6,height=1,highlightbackground="blue",command=count6)
ketbut.place(x=600,y=645)

checkout=tk.Button(window,text="Checkout",highlightbackground="blue",width=6,height=1,command=bill)
checkout.place(x=350,y=750)

clear=tk.Button(window,text="Clear",width=6,height=1,highlightbackground="blue",command=clear)
clear.place(x=600,y=45)

items=tk.Label(window,text="Total Item(s): 0",bg="#bde5ed")
items.place(x=25,y=750)

amount=tk.Label(window,text="Total Amount: $0",bg="#bde5ed")
amount.place(x=650,y=750)

c1=tk.Label(window,text="Item(s)",bg="#bde5ed")
c1.place(x=600,y=177)

c2=tk.Label(window,text="Item(s)",bg="#bde5ed")
c2.place(x=600,y=277)

c3=tk.Label(window,text="Item(s)",bg="#bde5ed")
c3.place(x=600,y=377)

c4=tk.Label(window,text="Item(s)",bg="#bde5ed")
c4.place(x=600,y=477)

c5=tk.Label(window,text="Item(s)",bg="#bde5ed")
c5.place(x=600,y=577)

c6=tk.Label(window,text="Item(s)",bg="#bde5ed")
c6.place(x=600,y=677)

cherem=tk.Button(window,text="Remove",highlightbackground="blue",width=6,height=1,command=rem1)
cherem.place(x=700,y=145)

cherem=tk.Button(window,text="Remove",highlightbackground="blue",width=6,height=1,command=rem2)
cherem.place(x=700,y=245)

cherem=tk.Button(window,text="Remove",highlightbackground="blue",width=6,height=1,command=rem3)
cherem.place(x=700,y=345)

cherem=tk.Button(window,text="Remove",highlightbackground="blue",width=6,height=1,command=rem4)
cherem.place(x=700,y=445)

cherem=tk.Button(window,text="Remove",highlightbackground="blue",width=6,height=1,command=rem5)
cherem.place(x=700,y=545)

cherem=tk.Button(window,text="Remove",highlightbackground="blue",width=6,height=1,command=rem6)
cherem.place(x=700,y=645)

window.mainloop()
from tkinter import *
from PyDictionary import PyDictionary
from PIL import Image, ImageTk
# importing the module
from englisttohindi.englisttohindi import EngtoHindi
dic=PyDictionary()

root=Tk()
root.geometry("700x500")
root.minsize(600,400)
root.configure(bg='cadetblue')
def dicti():
    meaning.config(text=dic.meaning(search.get())['Noun'][0])
    antonym.config(text=dic.antonym(search.get()))
    trans = EngtoHindi(str(search.get()))
    res = trans.convert
    result.set(res)
    

f=Frame(root)
f.pack()
Label(text="Skarsh Dictionary",font="constantia 24 ",fg="#299180").pack(pady=18)

f1=Frame(root)
f1.pack()
search=Entry(f1,font="constantia 19")
search.pack(side=LEFT,padx=20)
Button(f1,text="Search",font="constantia 14",relief=GROOVE,command=dicti).pack(padx=3,pady=6)
f2=Frame(root)
f2.pack(pady=12)
Label(f2,text="Meaning:-",font="timesnewroman 14 bold",fg="white",bg="#1c7569",borderwidth=1,relief=SUNKEN).pack(side=LEFT,fill=BOTH)
meaning = Label(f2, text="", font="timesnewroman 11")
meaning.pack()
f4=Frame(root)
f4.pack(pady=12)
Label(f4,text="Meaning in hindi:-",font="timesnewroman 14 bold",fg="white",bg="#1c7569",borderwidth=1,relief=SUNKEN).pack(side=LEFT)
Inhindi= Label(f4,text="",font="timesnewroman 20")
result=StringVar()
Label(f4, text="", textvariable=result,bg = "light grey",font="timesnewroman 21").pack(padx=12)

f3 = Frame(root)
f3.pack(pady=12)
Label(f3, text="Antonym:- ", font="timesnewroman 14 bold",fg="white",bg="#1c7569",borderwidth=1,relief=SUNKEN).pack(side=LEFT,fill=BOTH)
antonym = Label(f3, text=" ", font="timesnewroman 13")
antonym.pack()





  

root.mainloop()
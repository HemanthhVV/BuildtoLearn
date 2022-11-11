from tkinter import *
import nltk
import random
from nltk.corpus import wordnet

main=Tk()
main.title("definer")
Font_tuple = ("Comic Sans MS",15, "bold")
FONT = "Helvetica 14"
bc="#Ffbe26"
fg="#Ea1312"
tc="#000000"
wh="#Ffffff"
f1=Frame(main)
f1.pack(fill=BOTH,expand=TRUE)

def dic():
    word=e1.get()
    s=wordnet.synsets(word)
    n=random.randint(0,1)
    t1.insert(END,"Definition of the given word and type:"+"\n"+"\t"+ s[n].definition()+", '"+s[n].pos()+"'\n")
    e1.delete(0,END)
    
def dic1():
    type1=e1.get()
    arr=[]
    for i in wordnet.synsets(type1):
        for j in i.lemmas():
            arr.append(j.name())
    syn=set(arr)
    s=random.choice(list(syn))
    t1.insert(END,"A Synonymn of the given word is: "+"\n"+"\t"+s+"\n")
    e1.delete(0,END)
    
def dic2():
    type1=e1.get()
    arr=[]
    for i in wordnet.synsets(type1):
        for j in i.lemmas():
            if j.antonyms():
                arr.append(j.antonyms()[0].name())
    syn=set(arr)
    s=random.choice(list(syn))
    t1.insert(END,"A antonymn for the given word is: "+"\n"+"\t"+s+"\n")
    e1.delete(0,END)
    
l1=Label(f1,bg=bc,text="welcome to word_bot",fg=tc,pady=10,width=40,height=2,font=Font_tuple)
l1.pack(fill=BOTH,expand=TRUE)

t1=Text(f1,bg=fg,fg=tc,width=60,font=FONT)
t1.pack(fill=BOTH,expand=TRUE)

e1=Entry(f1,bg=wh,fg=tc,width=55)
e1.pack(side=LEFT,fill=BOTH,expand=TRUE)

send=Button(f1,text="definition",command=dic,width=10)
send.pack(side=RIGHT,fill=BOTH,expand=TRUE)

send1=Button(f1,text="synonymns",width=10,command=dic1)
send1.pack(side=RIGHT,fill=BOTH,expand=TRUE)

send2=Button(f1,text="antonymns",width=10,command=dic2)
send2.pack(side=RIGHT,fill=BOTH,expand=TRUE)


main.mainloop()

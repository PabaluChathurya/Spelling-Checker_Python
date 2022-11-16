import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry("700*400")
root.config(background="#dae6f6")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())
    
    cs=Lable(root,text="Correct text is :", font=("popping",20),bg="#dae6f6",fg="#964971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading = Label(root,text="Spelling Checker", font=("Trebuchet MS",30,"Bold"),bg='#dae6f6',fg='#364971')
heading.pack(pady(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppings",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()


button=Button(root,text="check",font=("arial",20,"bold",fg="white",bg="red",command_spelling))
button.pack()

spell=Lable(root,font=("poppins",20)bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)
root.mainloop()
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
root=Tk()
root.title("Rock Paper Scissor")
root.geometry("444x604")
root.config(bg="grey")

#images
rock = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor = ImageTk.PhotoImage(Image.open("scisssor.jpg"))

images= [rock, paper,scissor]

randNum= random.randint(0,2)
imgLabel= Label(root,image=images[randNum],bd=0)
imgLabel.pack(pady=20)
def spin():
    randNum= random.randint(0,2)
    imgLabel.config(image=images[randNum])
    if userChoise.get()=="Rock":
        userValue=0
    elif userChoise.get()=="Paper":
        userValue=1
    elif userChoise.get()=="Scissors":
        userValue=2
    #------------result decision---------
    if userValue==0: #rock
        if randNum==0:
            result.config(text="It's a tie! Spin again.",fg="grey")
            root.config(bg="grey")
        if randNum==1:
            result.config(text="Paper covers rock. You Loose!",fg="red")
            root.config(bg="red")
        if randNum==2:
            result.config(text="Rock beats scissors. You Win!",fg="green")
            root.config(bg="green")
    if userValue==1: #paper
        if randNum==1:
            result.config(text="It's a tie! Spin again.",fg="grey")
            root.config(bg="grey")
        if randNum==0:
            result.config(text="Paper covers rock. You Win!",fg="green")
            root.config(bg="green")
        if randNum==2:
            result.config(text="Scissors cuts paper. You Loose!",fg="red")
            root.config(bg="red")
    if userValue==2: #scissors
        if randNum==0: #rock
            result.config(text="Rock beats scissors. You Loose!",fg="red")
            root.config(bg="red")
        if randNum==1: #paper
            result.config(text="Scissors cuts paper. You Win!",fg="green")

            root.config(bg="green")
        if randNum==2:
            result.config(text="It's a tie! Spin again.",fg="grey")
            root.config(bg="grey")

Button(root,text="SPIN!",font="Helvetica 20 italic",command=spin).pack(pady=7,padx=12)

#choise
Label(root,text="Choose your pick:",font="Helvetica 12 italic",bg="grey").pack(pady=20)
userChoise= ttk.Combobox(root,value=("Rock","Paper","Scissors"),font="Helvetica 15 italic")
userChoise.current(0)
userChoise.pack(pady=15)

result=Label(root,text="",font="Helvetica 20 bold",bg="white")
result.pack(pady=10)
root.mainloop()









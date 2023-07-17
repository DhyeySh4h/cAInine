from tkinter import *
import numpy as np
from PIL import Image,ImageTk
import cv2
import pytesseract
def ocrcore(img):
    text=pytesseract.image_to_string(img)
    return text
def write_slogan():
    print("cAInine - Protecting Canines since 2021!")
def harmfulin(img):
    textlist = ocrcore(img).split(':')
    # if the ingredients are not empty
    if len(textlist) > 1:
        # The second part
        textlist = textlist[1]
        # We make a list that contains all ingredients
        textlist = textlist.split(' ')
        # we gather all dangerous ingredients into a list
        harmful = ['ONIONS', 'GARLIC', 'CHIVES', 'CHOCOLATE', 'MACADAMIA NUTS', 'CORN ON THE COB', 'AVOCADO',
                   'ARTIFICIAL SWEETENER ,XYLITOL',
                   'ALCOHOL', 'COOKED BONES', 'GRAPES AND RAISINS', 'GRAPES AND RAISINS', 'Apricot pits', 'Cherry pits',
                   'Candy', 'Candy', 'Gum', 'Hops',
                   'Moldy foods',
                   'Mushroom plants',
                   'Mustard seeds',
                   'onion powder',
                   'Peach pits',
                   'Potato leaves', 'stems (green parts)',
                   'Raisins',
                   'Rhubarb leaves',
                   'Salt',
                   'Tea (because it contains caffeine)',
                   'Tomato leaves', 'stems (green parts)',
                   'Yeast dough']
        # The list that contains all harmful ingredients now it's empty
        cAInine =[]
        # We loops over harmful ingredients
        for word in harmful:
            # We loops over our list of ingredient
            for ing in textlist:
                # We test if the ingredient is harmful
                if word.lower() in ing.lower():
                    # If yes then we add it into cAInine list
                    cAInine.append(word)
        txt=""
        for i in cAInine:
            txt+=i+","
        return txt
    else:
        return " "

        # We finally show the harmful ingredients

root=Tk()
root.geometry('670x600+200+30')
w=300
h=200
frame_1=Frame(root,width=670,height=700,bg='red').place(x=0,y=0)
root.config(bg="black")
#Label(root, text="Harmful ingredients", font=("times new roman", 30, "bold"), bg='black', fg='green').pack()

#f1=LabelFrame(root,bg='red',height=200,width=300)
#f1.pack()
L1=Label(frame_1,bg='red',width=w+100,height=h+100)
L1.place(x=10,y=160)
L2=Label(frame_1,bg='green',width=w,height=h)
L2.place(x=10,y=600)

L1.pack()
L2.pack()
cap=cv2.VideoCapture(0)
L2['text']=" "
button = Button(frame_1,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=LEFT)
slogan = Button(frame_1,
                   text="Hello",
                   command=write_slogan)
slogan.place(x=25, y=100)
slogan.pack(side=LEFT)
while True:
    img=cap.read()[1]
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=cv2.resize(img, (w+100, h+100))
    img=ImageTk.PhotoImage(Image.fromarray(img))
    L1['image']=img
    L2['text']+=harmfulin(cap.read()[1])
    root.update()
root.mainloop()

from tkinter import *
import numpy as np
from PIL import Image,ImageTk
import cv2
import pytesseract
def ocrcore(img):
    text=pytesseract.image_to_string(img)
    return text
def harmfule(img):
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
        # The list that contains all harmfull ingredients now it's empty
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

        # We finally show the harmful ingredients

root=Tk()
root.geometry('1200x800')
root.config(bg="black")
Label(root, text="Harmful ingredients", font=("times new roman", 30, "bold"), bg='black', fg='green').pack()

f1=LabelFrame(root,bg='red',height=200,width=300)
f1.pack()
L1=Label(f1,bg='red')
L1.place(x=10,y=150)
L2=Label(f1,bg='red')
L2.place(x=200,y=300)

L1.pack()
cap=cv2.VideoCapture(0)

while True:
    img=cap.read()[1]
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=ImageTk.PhotoImage(Image.fromarray(img))
    L1['image']=img
    L2['text'] = harmfule(cap.read()[1])



    #mainloop()
    root.update()
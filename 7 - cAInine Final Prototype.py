from tkinter import *
import numpy as np
from PIL import Image,ImageTk
import cv2
import pytesseract
harmful = ['ONIONS', 'GARLIC', 'CHIVES', 'CHOCOLATE', 'MACADAMIA NUTS', 'CORN ON THE COB', 'AVOCADO',
                   'ARTIFICIAL SWEETENER', 'COCOA', 'XYLITOL',
                   'ALCOHOL', 'COOKED BONES', 'GRAPES', 'RAISINS', 'GRAPES AND RAISINS', 'Apricot pits', 'Cherry pits',
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
def ocrcore(img):
    #extracting string from image
    text=pytesseract.image_to_string(img)
    return text

def harmfuling(img):
    textlist = ocrcore(img).split(':')
    # if the ingredients are not empty
    if len(textlist) > 1:
        # The second part
        textlist = textlist[1]
        # We make a list that contains all ingredients
        textlist = textlist.split(' ')
        # we gather all dangerous ingredients into a list

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
        L1 = Label(frame_1, bg='white', width=w + 100, height=h + 100)
        L1.place(x=10, y=160)
        L2 = Label(frame_1, bg='white', width=w, height=h)
        L2.place(x=10, y=600)

        L1.pack()
        L2.pack()
        #webcam capture
        cap = cv2.VideoCapture(0)
        L2['text'] = " "

        while True:
            img = cap.read()[1]
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (w + 100, h + 100))
            img = ImageTk.PhotoImage(Image.fromarray(img))
            L1['image'] = img
            L2['text'] += harmfuling(cap.read()[1])
            root.update()


root=Tk()
root.geometry('670x600+200+30')


def addharmful():
    def back1():
        global mylabel5
        mylabel2.destroy()
        addbutton.destroy()
        added.destroy()
        Button3.destroy()
        mylabel5.destroy()

    def button_command():
        txt = added.get()
        mylabel5 = Label(frame_1, text=txt)
        mylabel5.pack()
        harmful.append(txt)
        print(harmful)
    mylabel2=Label(frame_1, text="Please add one harmful ingredient:")
    mylabel2.pack()
    added=Entry(frame_1,width=20)
    added.pack()
    addbutton=Button(frame_1,text='Add Ingredient',command=button_command)
    addbutton.pack()
    Button3 = Button(root, text="back", command = back1)
    Button3.pack()
    root.mainloop()


def scan():
    L1 = Label(frame_1, bg='black', width=w+100 , height=h+100 )
    L1.place(x=10, y=160)
    def back2():
        L1.destroy()
        L2.destroy()
        Button4.destroy()
    Button4 = Button(frame_1, text="back", command=back2)

    Button4.pack()
    L2 = Label(frame_1, bg='blue',fg='white', width=w, height=h)
    L2.place(x=10, y=400)
    L1.pack()
    L2.pack()


    cap = cv2.VideoCapture(0)
    L2['text'] = " "


    while True:
        img = cap.read()[1]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (w + 100, h +100))
        img = ImageTk.PhotoImage(Image.fromarray(img))
        L1['image'] = img
        L2['text'] += harmfuling(cap.read()[1])
        root.update()
    root.mainloop()

def upload():


    def button_command2():
        def back2():
            L1.destroy()
            L2.destroy()
            addbutton4.destroy()
            added2.destroy()
        Button4 = Button(frame_1, text="back", command=back2)
        Button4.pack()
        txt = added2.get()


        img = cv2.imread(str(txt), cv2.IMREAD_GRAYSCALE)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img2 = cv2.resize(img, (w + 100, h + 100))
        img2 = ImageTk.PhotoImage(Image.fromarray(img2))
        L1 = Label(frame_1, bg='white', width=w + 100, height=h + 100)
        L1.place(x=10, y=160)
        L2 = Label(frame_1, bg='blue',fg='white', width=w, height=h)
        L2.place(x=10, y=600)

        L1.pack()
        L2.pack()

        L1['image']=img2

        L2['text'] = harmfuling(img)

        root.update()
        root.mainloop()

    added2 = Entry(frame_1, width=20)
    added2.pack()
    addbutton4 = Button(frame_1, text="Please enter the name of the image to scan and click here2", command=button_command2)
    addbutton4.pack()
    txt = added2.get()

    root.mainloop()


w=300
h=200
frame_1=Frame(root,width=670,height=700,bg='black').place(x=0,y=0)
root.config(bg="black")
Label(root, text="cAInine", font=("times new roman", 30, "bold"), bg='black', fg='white').pack()
Button1=Button(root,text="Add Harmful Ingredient",command=addharmful)
Button1.pack()
Button2=Button(root,text="Scan",command=scan)
Button2.pack()
Button5=Button(root,text="Upload Image",command=upload).pack()
root.mainloop()

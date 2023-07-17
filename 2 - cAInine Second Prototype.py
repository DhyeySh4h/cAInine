import numpy as np
import cv2
import pytesseract
def ocrcore(img):
    text=pytesseract.image_to_string(img)
    return text


cap = cv2.VideoCapture(0)

while True:

    ret, img = cap.read()

    cv2.imshow('Video', img)

    textlist = ocrcore(img).split(':')
    if len(textlist)>1:
        textlist = textlist[1]
        textlist = textlist.split(' ')
        harmful = ['ONIONS', 'GARLIC', 'CHIVES', 'CHOCOLATE', 'MACADAMIA NUTS', 'CORN ON THE COB', 'AVOCADO',
               'ARTIFICIAL SWEETENER ,XYLITOL',
               'ALCOHOL', 'COOKED BONES', 'GRAPES AND RAISINS', 'GRAPES AND RAISINS', 'Apricot pits', 'Cherry pits',
               'Candy', 'Candy', 'Gum', 'Hops',
               'Mouldy foods',
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
        cAInine = []
        for word in harmful:
            for ing in textlist:
                if word.lower() in ing.lower():
                    cAInine.append(word)
        print(cAInine)

    if (cv2.waitKey(10) & 0xFF == ord('b')):
        break
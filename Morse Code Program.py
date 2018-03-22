from tkinter import *
from os import system
import time
import subprocess

#subprocess.call(["afplay", "dit.wav"])

#-----------------------------------Fields--------------------------------------#

morseDict = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-.."
             ,"m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-"
             ,"y":"-.--","z":"--..","1":".---","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---.."
             ,"9":"----.","0":"-----",".":".-.-.-",",":"--..--","?":"..--..","!":"..--.",":":"---...",'"':".-..-.","'":".----."}
inputMorse = ""

#-----------------------------------Overall--------------------------------------#

window = Tk()

window.title("Chocolate Machine")
window.configure(background = "gray")

#-----------------------------------Title--------------------------------------#
topFrame = Frame(window, bg = "gray")
topFrame.pack(side = "top", padx=20, pady = 40)

title = Label (topFrame, text="WELCOME TO MY MORSE CODE TRANSLATOR", bg="gray", fg="black", font = "none 60 bold")
title.pack(side = "top")



#-----------------------------------Left Frame--------------------------------------#

leftFrame = Frame(window, bg = "gray", height=500, width=720)
leftFrame.pack(side="left")
leftFrame.pack_propagate(0)


header = Label (leftFrame, text="ENGLISH TO MORSE CODE", bg="gray", fg="black", font = "none 35 bold")
header.pack()

Label(leftFrame, text = "Enter the sentence that you would like to be translated", bg ="gray", fg="black", font = "none 16 bold").pack()

e1 = Entry(leftFrame)
e1.pack()

submit = Button(leftFrame, text = "Translate!", command=lambda: buttonPress(0))
submit.pack()

Label(leftFrame, text = "Morse translation:", bg = "gray", font = "none 16").pack()

morseLeftDisplay = Label(leftFrame, text = "", bg = "gray", font = "none 20")
morseLeftDisplay.pack()





#-----------------------------------Right Frame--------------------------------------#
rightFrame = Frame(window, bg = "gray", height = 500, width = 720)
rightFrame.pack(side = "right")
rightFrame.pack_propagate(0)

header2 = Label (rightFrame, text="MORSE CODE TO ENGLISH", bg="gray", fg="black", font = "none 35 bold")
header2.pack()

Label(rightFrame, text = "Click the buttons below to write in morse", bg ="gray", fg="black", font = "none 20 bold").pack()


Button(rightFrame, text=".", bg="gray", command=lambda: buttonPress(1)).pack()
Button(rightFrame, text="-", bg="gray", command=lambda: buttonPress(2)).pack()
Button(rightFrame, text="End Char", bg="gray", command=lambda: buttonPress(3)).pack()
Button(rightFrame, text="End Word", bg="gray", command=lambda: buttonPress(4)).pack()
Button(rightFrame, text="Clear Sentence", bg="gray", command=lambda: buttonPress(5)).pack()
Button(rightFrame, text="Translate!", bg="gray", command=lambda: buttonPress(6)).pack()


Label(rightFrame, text = 'Your current morse input below ("|" means the end of a character):', bg = "gray", font = "none 16").pack()

morseDisplay = Label(rightFrame, text = "", bg = "gray", font = "none 20")
morseDisplay.pack()

Label(rightFrame, text = "Your English translation: ", bg = "gray", font = "none 16").pack()

englishDisplay = Label(rightFrame, text = "", bg = "gray", font = "none 20")
englishDisplay.pack()

#-----------------------------------Functions--------------------------------------#

def buttonPress(type):
    global inputMorse

    if type is 0:
        translateToMorse(str(e1.get()))

    #add dot
    elif type is 1:
        inputMorse += "."
        morseDisplay.config(text = inputMorse)
    #add dash
    elif type is 2:
        inputMorse  += "-"
        morseDisplay.config(text = inputMorse)
    #end char
    elif type is 3:
        inputMorse += "|"
        morseDisplay.config(text = inputMorse)

    #end word
    elif type is 4:
        inputMorse += " "
        morseDisplay.config(text = inputMorse)
    #clear sentence
    elif type is 5:
        inputMorse = ""
        morseDisplay.config(text = inputMorse)
        englishDisplay.config(text = "")
    elif type is 6:
        translateToEnglish()

def translateToMorse(inputString):
    translatedString = ""

    #This loop loops through each individual character in the string
    #e.g: [h][e][l][l][o]
    for x in range(len(inputString)):
        #binaryString represents either a one or zero from the dictionary morseDict
        #1 represents a dash and a zero represents a dot in morse code
        #inputString[x] represents each individual character in the string

        if inputString[x] is not " ":
            if x > 0:
                translatedString += "|"
            print(morseDict[inputString[x]])
            binaryString = morseDict[inputString[x]]

            #looping through the current character's morse version
            #e.g: a = .-
            for y in range(len(binaryString)):
                #dot
                if binaryString[y] == ".":
                    subprocess.call(["afplay", "dit2.wav"])
                    translatedString += "."
                #dash
                elif binaryString[y] == "-":
                    subprocess.call(["afplay", "dah2.wav"])
                    translatedString += "-"
                #pause for about 1 seconds in between characters
                time.sleep(0.5)

        elif inputString[x] == " ":
            #pause for a bout 2 seconds when in between words
            translatedString += " "
            time.sleep(1)
    #print("translate: " + translatedString)
    morseLeftDisplay.config(text = translatedString)


def translateToEnglish():
    global inputMorse
    lastPos = 0
    translatedString = ""
    tempMorse = ""
    for x in range(len(inputMorse)):

        #if end of a character
        if inputMorse[x] == "|":

            #tempMorse is set to the morse segment equivalent to one character
            tempMorse = inputMorse[lastPos:x]
            #lastPos is moved up
            lastPos = x+1

            #loop to find which character corresponds with the morse
            for key, value in morseDict.items():
                #if found morse with character
                if tempMorse == value:
                    translatedString += key
                    break

        #if there is a new word starting.

        elif inputMorse[x] == " ":
            translatedString += " "
            lastPos  = x+1

    system('say ' + translatedString)
    englishDisplay.config(text = translatedString)




"""""

b = Entry(rightFrame)
b.pack()
"""""





"""
button1 = Button(topFrame, text="Button 1", fg="red", bg="yellow")
button2 = Button(topFrame, text="Button 2", fg="purple")
button3 = Button(topFrame, text="Button 3", fg="blue")
button4 = Button(bottomFrame, text="Button 4", fg="yellow")
button5 = Button(bottomFrame, text="Button 5", fg="yellow")
button6 = Button(bottomFrame, text="Button 6", fg="yellow")

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
"""

window.mainloop()

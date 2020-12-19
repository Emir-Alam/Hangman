from tkinter import *
import random
from PIL import ImageTk, Image
import csv

root = Tk()
root.geometry("900x400")
root.title("Hangman")
root.configure(background="white")
wordDistance = 400

words = ["gang"]

lives = 6
word = words[random.randint(0, len(words) - 1)]
guess = ""
guessString = ""
wordsGuessed = []
lettersinword = []

for char in word:
    lettersinword.append(char)

def enterLetter():
    global lives
    Log["text"] = ""
    guessString = getGuess.get()
    for char in lettersinword:
        if char.lower() == guessString[0].lower():
            if char in wordsGuessed:
                Log["text"] = "You have already guessed this Character!"
            else:
                wordsGuessed.append(char.lower())
                for i in range(len(word)):
                    if word[i] == char:
                        newString = list(underscore['text'])
                        newString[i] = char
                        full_str = ''.join([str(elem) for elem in newString])
                        underscore['text'] = str(full_str)
                        print(underscore['text'])   
    if guessString not in word:
        if lives == 0:
            GameOver.config(font="fangsongti 60", background="red",text="Game Over!")
        else:
            lives = lives -1
            LivesText.configure(text="Lives: {}".format(lives)) 


underscore = Label(root, text="_")
underscore.configure(font="fangsongti 40", background="white")
underscore.place(x=wordDistance,y=150)
underscore.pack_propagate(0)       

for i in range(len(word) - 1):
    underscore['text'] = underscore['text'] + "_"

load = Image.open(r"C:\Users\daxte\Desktop\Python GUI Games\hangman.jpeg")
render = ImageTk.PhotoImage(load)

img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)

getGuess = Entry(root, text="")
getGuess.config(font="fangsongti 18", background="white")
getGuess.place(x= 400, y=320)

EnterButton = Button(root, text="Enter Letter")
EnterButton.config(font="fangsongti 20", background="white", command=enterLetter)
EnterButton.place(x= 700, y=300)

Log = Label(root, text="")
Log.config(font="fangsongti 20", background="white")
Log.place(x= 375, y=0)


LivesText = Label(root, text="Lives: {}".format(lives))
LivesText.config(font="fangsongti 20", background="white")
LivesText.place(x= 750, y=50)


GameOver = Label(root, text="")
GameOver.config(font="fangsongti 60", background="white")
GameOver.place(x= 380, y=175)

root.mainloop()
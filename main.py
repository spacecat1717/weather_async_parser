import parser, words, random, asyncio
from tkinter import *

root = Tk()
root.title('Weather and word')
root.geometry('150x150')
root.configure(bg='#003333')

cities = ['St. Petersburg', 'Moscow']

def num_generator():
    num = random.randint(0, 300) 
    return num

def random_word():
    text = asyncio.run(words.main(num_generator()))
    label = Label(text=text, bg='#006666', fg='white')
    label.pack()


btn = Button(text='Get word', 
            background='#006666', 
            activebackground='#336666', 
            foreground='white', 
            justify=CENTER, command=random_word, relief=GROOVE)
btn.pack()


weather = asyncio.run(parser.main(cities))
lab = Label(text=weather, bg='#006666', fg='white', justify=CENTER)
lab.pack()


root.mainloop()




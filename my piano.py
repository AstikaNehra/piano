from tkinter import *
from winsound import *
import pygame
pygame.init()

root=Tk()

def one():
    pygame.mixer.music.load("no-1.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

def two():
    pygame.mixer.music.load("no-2.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

def three():
    pygame.mixer.music.load("no-3.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

def four():
    pygame.mixer.music.load("no-4.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

def five():
    pygame.mixer.music.load("no-5.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

def six():
    pygame.mixer.music.load("no-6.wav")
    pygame.mixer.music.play()
    pygame.event.wait()

l1=Label(root,text="PIANO",fg="blue",bg="pink")
l1.grid(row=0,columnspan=20)

s = Button(root, text=' sa ', fg='black', bg='red', command=one, height=5, width=2) 
s.grid(row=9, column=2)
r = Button(root, text=' re ', fg='black', bg='red', command=two, height=5, width=2) 
r.grid(row=9, column=4)
g = Button(root, text=' ga ', fg='black', bg='red', command=three, height=5, width=2) 
g.grid(row=9, column=6)
m = Button(root, text=' ma ', fg='black', bg='red', command=four, height=5, width=2) 
m.grid(row=9, column=8)
p = Button(root, text=' pa ', fg='black', bg='red', command=five, height=5, width=2) 
p.grid(row=9, column=10)
d = Button(root, text=' dha ', fg='black', bg='red', command=six, height=5, width=2) 
d.grid(row=9, column=12)
d = Button(root, text=' ni ', fg='black', bg='red', command=one, height=5, width=2) 
d.grid(row=9, column=12)
d = Button(root, text=' sa ', fg='black', bg='red', command=two, height=5, width=2) 
d.grid(row=9, column=12)

root.mainloop()

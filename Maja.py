from tkinter import *

raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=1000, height=600, background="lightblue")
# Maja sein
tahvel.create_rectangle(250, 300, 600, 500, fill="black")
#Maja katus
tahvel.create_line(250, 300, 425, 150, width=5, fill="red")
tahvel.create_line(600, 300, 425, 150, width=5, fill="red")
tahvel.create_polygon(250, 300, 600, 300, 425, 150, fill="red")
#Aken 1
tahvel.create_rectangle(285, 390, 330, 445, width=3, outline="brown", fill="blue")
tahvel.create_line(285, 417.5, 330, 417.5, width=3, fill="white")
tahvel.create_line(307.5, 390, 307.5, 445, width=3, fill="white")
#Aken 2
tahvel.create_rectangle(520, 390, 565, 445, width=3, outline="brown", fill="blue")
tahvel.create_line(520, 417.5, 565, 417.5, width=3, fill="white")
tahvel.create_line(542.5, 390, 542.5, 445, width=3, fill="white")
#Uks
tahvel.create_rectangle(400, 390, 450, 499, width=3, outline="white", fill="white")
tahvel.create_oval(440, 444.5, 445, 444.5, outline="brown", fill="brown")
#Korsten
tahvel.create_rectangle(510, 150, 526, 236, outline="brown", fill="brown")
#Muru
tahvel.create_rectangle(0, 500, 1000, 600, outline="green", fill="green")

tahvel.pack()
raam.mainloop()
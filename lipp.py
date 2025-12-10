from tkinter import *
raam = Tk()
raam.title("Lipp")
tahvel = Canvas(raam, width=1000, height = 600)
#Kadrina valla lipp
tahvel.create_rectangle(0, 0, 1000, 220, fill="white", outline="white")
tahvel.create_rectangle(0, 220, 1000, 350, fill="black", outline="black")
tahvel.create_rectangle(0,350, 1000, 600, fill="green", outline="green")

tahvel.pack()
raam.mainloop()
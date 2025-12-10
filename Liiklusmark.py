from tkinter import *
raam = Tk()
raam.title("Liiklusmark")
#Sissesoidu keelumark
tahvel = Canvas(width = 1000, height = 600)
tahvel.create_oval(350,100,650,400, fill="red", outline="red")
tahvel.create_rectangle(368, 217, 632, 270, fill="white", outline="white")

tahvel.pack()
tahvel.mainloop()
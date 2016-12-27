import os
from tkinter import *
window = Tk()
window.configure(background = 'white')
window.geometry('500x650')
window.title("flags")

next_frame = Frame(window,bg= "blue")
next_frame.pack(side = "top",fill = X)

top_frame = Frame(window,bg = "white")
top_frame.pack(side= BOTTOM)
bottom_frame = Frame(window,bg = "white")
bottom_frame.pack(side = BOTTOM)
global counter,canvas
counter = 0
canvas = Canvas(window,width = 250,height = 130,bg = 'white')
canvas.pack()
canvas.place(relx=0.25, rely= 0.3)

def change_flag():
    global counter,canvas,my_image
    directory = 'C:\\Users\\abhayksi\\Desktop\\GUI_python\\'
    country = ['Canada','Australia']
    format_image = '.png'
    location = directory + country[counter] + format_image
    my_image = PhotoImage(file = location)
    canvas.create_image(5,5,anchor = NW,image = my_image)
    counter += 1
        
def print_result(number):
    if number == 2:
        print("Right answer {0}".format(number))
    else:
        print("Wrong answer")

button1 = Button(top_frame,width = 20, text = "Australia", fg = "black",command = lambda: print_result(1))
button2 = Button(top_frame,width = 20, text = "Canada", fg = "black",command = lambda: print_result(2))
button3 = Button(bottom_frame,width = 20, text = "Belgium", fg = "black",command = lambda: print_result(3))
button4 = Button(bottom_frame,width = 20, text = "Russia", fg = "black",command = lambda: print_result(4))
button5 = Button(next_frame,width = 20, text = "next", fg = "black",command = lambda: change_flag())

button1.pack(side = LEFT,padx = 5,pady = 5)
button2.pack(side = RIGHT,padx = 5,pady = 5)
button3.pack(side = LEFT,padx = 5,pady = 5)
button4.pack(side = RIGHT,padx = 5,pady = 5)
button5.pack(side = RIGHT,padx = 5,pady = 5)

window.mainloop()

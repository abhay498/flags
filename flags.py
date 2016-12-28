from tkinter import *

LARGE_FONT = ("Verdana",12)
global counter,canvas,country
counter = 0
country = {"Australia":6,"Canada":2,"Russia":1,"India":7,"Argentina":8}

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

class game_wrapper(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.geometry('500x650')
        self.title("flags")
        self.frames = {}

        container = Frame(self,background="white")
        container.pack(side = "top",fill = "both",expand = True)
        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        for F in (start_page,flags_page,score_page):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row= 0,column = 0,sticky = "nsew")
            
        self.show_frame(start_page)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class flags_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        global canvas
        canvas = Canvas(self,width = 250,height = 130,bg = 'white')
        canvas.pack()
        canvas.place(relx=0.25, rely= 0.3)
        next_frame = Frame(self,bg= "blue")
        next_frame.pack(side = "top",fill = X)
        top_frame = Frame(self,bg = "white")
        top_frame.pack()
        top_frame.place(relx = 0.2,rely = 0.75)
        bottom_frame = Frame(self,bg = "white")
        bottom_frame.pack()
        bottom_frame.place(relx = 0.2,rely = 0.8)
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

class start_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text = "Start page",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)
        play_button = Button(self,width = 20, text = "Next", fg = "black" \
                             ,command = lambda:controller.show_frame(flags_page))
        play_button.pack()

class score_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        pass

app = game_wrapper()
app.mainloop()

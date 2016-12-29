from tkinter import *

LARGE_FONT = ("Verdana",12)
global counter,canvas,country
counter = 0
country = {"Australia":6,"Canada":2,"Russia":1,"India":7,"Argentina":8}

def change_flag():
    global counter,canvas,my_image
    directory = 'C:\\Users\\abhayksi\\Desktop\\GUI_python\\'
    country = ['Canada','Australia','India']
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

    def exit(self):
        self.destroy()
        
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
        score_page_button = Button(self,width = 20, text = "Scores", fg = "black" \
                             ,command = lambda:controller.show_frame(score_page))
        score_page_button.pack()

class start_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text = "Start page",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)
        play_button = Button(self,width = 20, text = "Play", fg = "black" \
                             ,command = lambda:controller.show_frame(flags_page))
        play_button.pack()

class score_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        user_one = 46
        score_canvas= Canvas(self,width=500, height=700, bg="white")
        score_canvas.pack()
        J_one = score_canvas.create_text(200,100, text=("python", user_one), font=("Comic Sans", 20))
        J_two = score_canvas.create_text(200,200, text=("ruby", user_one), font=("Comic Sans", 20))
        J_three = score_canvas.create_text(200,300, text=("java", user_one), font=("Comic Sans", 20))
        J_four = score_canvas.create_text(200,400, text=("sqlite", user_one), font=("Comic Sans", 20))
        J_five = score_canvas.create_text(200,500, text=("openCV", user_one), font=("Comic Sans", 20))
        bottom_frame = Frame(self,bg = "white")
        bottom_frame.pack()
        bottom_frame.place(relx = 0.2,rely = 0.9)
        start_button = Button(bottom_frame,width = 20, text = "Start", fg = "black",\
                              command = lambda:controller.show_frame(start_page))
        exit_button = Button(bottom_frame,width = 20, text = "Exit", fg = "black",\
                             command = lambda:app.exit())
        start_button.pack(side = LEFT,padx = 5,pady = 5)
        exit_button.pack(side = RIGHT,padx = 30,pady = 5)

app = game_wrapper()
app.mainloop()

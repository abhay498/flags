from tkinter import *
import random
LARGE_FONT = ("Verdana",12)
global counter,canvas,country
global background_image
global background_label
global svalue
global userscore_canvas
global shuffled_country
counter = 0
country = ['Canada','Australia','Belarus','Croatia','Estonia','Ethiopia']
random.shuffle(country)
print(country)

global chosen

def change_flag():
    global counter,canvas,my_image,chosen
    directory = 'C:\\Users\\abhayksi\\Desktop\\GUI_python\\'
    format_image = '.png'
    location = directory + country[counter] + format_image
    my_image = PhotoImage(file = location)
    canvas.create_image(5,5,anchor = NW,image = my_image)
    chosen = country[counter]
    print(chosen)
    counter += 1
    
def print_result(number,id_2):
    global userscore_canvas
    if number == 2:
        userscore_canvas.itemconfigure(id_2, text = "Right")
    else:
        userscore_canvas.itemconfigure(id_2, text = "Wrong")

def user_name():
    print ("Hey {0},lets get started".format(svalue.get()))

def about():
    window = Toplevel()
    window.title("About flags")
    window.geometry("400x400")
    window.iconbitmap('C:\\Users\\abhayksi\\Desktop\\GUI_python\\favicon.ico')
    canvas = Canvas(window,width = 400,height = 400,bg = 'white')
    canvas.pack()
    J_one = canvas.create_text(150,150, text=("File version : 1.0\rEmail : abskumar798@gmail.com"), font=("Comic Sans", 10))
    exit_button = Button(canvas,width = 20, text = "Close", fg = "black",\
                             command = lambda:app.exit_window(window))
    exit_button.place(relx=.78, rely=.93, anchor="c")

class game_wrapper(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.geometry('500x650')
        self.title("flags")
        self.frames = {}
        self.configure(bg="white")
        
        container = Frame(self)
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
        
    def exit_window(self,window):
        window.destroy()

class flags_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        global canvas,score,userscore_canvas,counter,country,shuffled_country
        score = 870
        self.configure(bg="white")
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
        
        userscore_canvas= Canvas(self,width=500, height=100, bg="white")
        userscore_canvas.pack()
        id_1 = userscore_canvas.create_text(40,30, text=("Score", score), font=("Comic Sans",10))
        id_2 = userscore_canvas.create_text(45,45, font=("Comic Sans",10))

        button1 = Button(top_frame,width = 20, text = "Australia", fg = "black",command = lambda: print_result(1,id_2))
        button2 = Button(top_frame,width = 20, text = "Canada", fg = "black",command = lambda: print_result(2,id_2))
        button3 = Button(bottom_frame,width = 20, text = "Belgium", fg = "black",command = lambda: print_result(3,id_2))
        button4 = Button(bottom_frame,width = 20, text = "Russia", fg = "black",command = lambda: print_result(4,id_2))
        button5 = Button(next_frame,width = 20, text = "next", fg = "black",command = lambda: change_flag())
        
        button1.pack(side = LEFT,padx = 5,pady = 5)
        button2.pack(side = RIGHT,padx = 5,pady = 5)
        button3.pack(side = LEFT,padx = 5,pady = 5)
        button4.pack(side = RIGHT,padx = 5,pady = 5)
        button5.pack(side = RIGHT,padx = 5,pady = 5)
        score_page_button = Button(self,width = 20, text = "Scores", fg = "black" \
                             ,command = lambda:controller.show_frame(score_page))
        score_page_button.pack()

        menubar = Menu(self)
        #****** file 
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="Start",command = lambda:controller.show_frame(start_page))
        filemenu.add_command(label="Play",command = lambda:controller.show_frame(flags_page))
        filemenu.add_command(label="Exit",command = lambda:app.exit())
        menubar.add_cascade(label="File",menu = filemenu)

        #****** options
        options = Menu(menubar,tearoff=0)
        options.add_command(label="Scores",command = lambda:controller.show_frame(score_page))
        menubar.add_cascade(label="Options",menu = options)

        #****** help
        helps = Menu(menubar,tearoff=0)
        helps.add_command(label="About",command = lambda: about())
        menubar.add_cascade(label="Help",menu = helps)
        
        controller.configure(menu = menubar)

class start_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        global background_image
        global background_label
        global svalue

        background_image = PhotoImage(file = 'C:\\Users\\abhayksi\\Desktop\\GUI_python\\white.png')
        background_label = Label(self, image=background_image)
        background_label.pack(side='top', fill='both', expand='yes')
        label = Label(background_label,text = "Start page",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)
        play_button = Button(background_label,width = 20, text = "Play", fg = "black" \
                             ,command = lambda:controller.show_frame(flags_page))
        play_button.pack()
        self.configure(bg="white")
        svalue = StringVar()
        w = Entry(self,textvariable=svalue)
        w.pack()
        
        foo = Button(self,text="Username", command = lambda: user_name())
        foo.pack()
        
class score_page(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.configure(bg="white")
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
        exit_button = Button(bottom_frame,width = 20, text = "Close", fg = "black",\
                             command = lambda:app.exit())
        start_button.pack(side = LEFT,padx = 5,pady = 5)
        exit_button.pack(side = RIGHT,padx = 30,pady = 5)

if __name__ == "__main__":
    app = game_wrapper()
    app.resizable(0,0)
    app.iconbitmap('C:\\Users\\abhayksi\\Desktop\\GUI_python\\favicon.ico')
    background_label.image = background_image
    app.mainloop()

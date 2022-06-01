from time import sleep
import pdb
from random import shuffle
import copy
from tkinter import *
from tkinter import font
import random
LARGE_FONT = ('Verdana', 12)
global counter, canvas, country
global background_image
global background_label
global svalue
global userscore_canvas
global shuffled_country
global counter
counter = 0
country = ['Switzerland', 'Canada', 'Australia', 'Vietnam']
random.shuffle(country)
global chosen
global button1, button2, button3, button4
global top_frame, bottom_frame
global flag
global difficulty_level
difficulty_level = 'country_hard'


def func_options(chosen):
    country_1 = ['Switzerland', 'Canada', 'Australia', 'Vietnam']
    country_2 = copy.copy(country_1)
    country_2.remove(chosen)
    options = []
    options.append(chosen)
    shuffle(country_2)
    total = 0
    while total < 3:
        item = country_2.pop()
        options.append(item)
        total += 1

    shuffle(options)
    del country_2[:]
    return options


def change_flag(top_frame, bottom_frame, button1, button2, button3, button4, controller):
    global counter, canvas, my_image, chosen, flag, directory
    canvas.delete('all')
    directory = 'national_flags\\'
    format_image = '.png'
    
    try:
        location = directory + country[counter] + format_image
    except:
        controller.show_frame(PlayAgainExit)
        
    my_image = PhotoImage(file=location)
    canvas.create_image(5, 5, anchor=NW, image=my_image)
    chosen = country[counter]
    options_text = func_options(chosen)

    for i in range(0, 4):
        if chosen == options_text[i]:
            flag = i
            break
        
    flag = flag + 1
    button1["text"] = options_text[0]
    button2["text"] = options_text[1]
    button3["text"] = options_text[2]
    button4["text"] = options_text[3]

    counter += 1


def print_result(number, id_2, id_1, controller):
    global userscore_canvas, chosen, flag, score, difficulty_level
    if flag == number:
        userscore_canvas.itemconfigure(id_2, text="Right")
        if difficulty_level == 'country_easy':
            score = score + 10
        elif difficulty_level == 'country_medium':
            score = score + 15
        else:
            score = score + 20

        userscore_canvas.itemconfigure(id_1, text=("Score", score))
    else:
        userscore_canvas.itemconfigure(id_2, text="Wrong")
        controller.show_frame(PlayAgainExit)


def about():
    window = Toplevel()
    window.title("About flags")
    window.geometry("400x400")
    window.iconbitmap('icon.ico')
    window.resizable(0, 0)
    canvas = Canvas(window, width=400, height=400, bg='white')
    canvas.pack()
    J_one = canvas.create_text(
        150,
        150,
        text=("File version : 1.0\r\rEmail : abskumar798@gmail.com"),
        font=(
            "Comic Sans",
            10))


def scores():
    window = Toplevel()
    window.title('Scores')
    window.geometry("400x400")
    window.iconbitmap('icon.ico')
    window.resizable(0, 0)
    canvas = Canvas(window, width=400, height=400, bg='white')
    canvas.pack()
    J_one = canvas.create_text(
        150,
        150,
        text=("Ram       40 \r\rShyam       60"),
        font=(
            "Comic Sans",
            10))


class game_wrapper(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('500x550')
        self.title("flags")
        self.frames = {}
        self.configure(bg="white")

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (start_page, flags_page, PlayAgainExit):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(start_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def exit(self):
        self.destroy()

    def exit_window(self, window):
        window.destroy()


class flags_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        global canvas, score, userscore_canvas, counter, country, shuffled_country
        score = 0
        canvas = Canvas(self, width=300, height=150, bg='white')
        canvas.pack()
        canvas.place(relx=0.25, rely=0.3)

        filename = PhotoImage(file="national_flags\\Switzerland.png")
        Frame.filename = filename
        image_container = canvas.create_image(5, 5, anchor=NW, image=filename)

        next_frame = Frame(self, bg="blue")
        next_frame.pack(side="top", fill=X)
        top_frame = Frame(self, bg="white")
        top_frame.pack()
        top_frame.place(relx=0.2, rely=0.75)
        bottom_frame = Frame(self, bg="white")
        bottom_frame.pack()
        bottom_frame.place(relx=0.2, rely=0.8)

        userscore_canvas = Canvas(self, width=500, height=100, bg="white")
        userscore_canvas.pack()
        id_1 = userscore_canvas.create_text(
            40, 30, text=(
                "Score", score), font=(
                "Comic Sans", 10))
        id_2 = userscore_canvas.create_text(200, 30, font=("Comic Sans", 10))

        # Set the options here
        options = options_text = func_options('Australia')
        button1 = Button(
            top_frame,
            width=20,
            text=options[0],
            fg="black",
            command=lambda: print_result(
                1,
                id_2,
                id_1,
                controller))
        button2 = Button(
            top_frame,
            width=20,
            text=options[1],
            fg="black",
            command=lambda: print_result(
                2,
                id_2,
                id_1,
                controller))
        button3 = Button(
            bottom_frame,
            width=20,
            text=options[2],
            fg="black",
            command=lambda: print_result(
                3,
                id_2,
                id_1,
                controller))
        button4 = Button(
            bottom_frame,
            width=20,
            text=options[3],
            fg="black",
            command=lambda: print_result(
                4,
                id_2,
                id_1,
                controller))
        button1.pack(side=LEFT, padx=5, pady=5)
        button2.pack(side=RIGHT, padx=5, pady=5)
        button3.pack(side=LEFT, padx=5, pady=5)
        button4.pack(side=RIGHT, padx=5, pady=5)

        button5 = Button(
            next_frame,
            width=20,
            text="next",
            fg="black",
            command=lambda: change_flag(
                top_frame,
                bottom_frame,
                button1,
                button2,
                button3,
                button4,
                controller))

        button5.pack(side=RIGHT, padx=5, pady=5)

        menubar = Menu(self)

        # File
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Start",
                             command=lambda: controller.show_frame(start_page))
        filemenu.add_command(label="Exit", command=lambda: app.exit())
        menubar.add_cascade(label="File", menu=filemenu)

        # Options
        options = Menu(menubar, tearoff=0)
        options.add_command(label="Scores", command=lambda: scores())
        menubar.add_cascade(label="Options", menu=options)

        # Help
        helper = Menu(menubar, tearoff=0)
        helper.add_command(label="About", command=lambda: about())
        menubar.add_cascade(label="Help", menu=helper)

        controller.configure(menu=menubar)


class start_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        global background_image
        global background_label
        global svalue

        background_image = PhotoImage(file='white.png')
        background_label = Label(self, image=background_image)
        background_label.pack(side='top', fill='both', expand='yes')
        label = Label(background_label, text="Name", font=LARGE_FONT)
        label.pack(pady=200, padx=100)
        play_button_font = font.Font(family='Verdana', size=10)
        play_button = Button(
            background_label,
            width=30,
            text="Play",
            fg="black",
            command=lambda: controller.show_frame(flags_page),
            height=5,
            font=play_button_font)
        play_button.pack(padx=0, pady=0, expand=True)
        play_button.pack()
        self.configure(bg="white")
        svalue = StringVar()
        w = Entry(self, textvariable=svalue)
        w.pack()


class PlayAgainExit(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="white")
        global counter
        score_canvas = Canvas(self, width=500, height=700, bg="white")

        if counter == 3:
            score_canvas.create_text(
                300,
                50,
                text="Wrong answer",
                fill="black",
                font=('Helvetica 15 bold'))
        else:
            score_canvas.create_text(
                300,
                50,
                text="Congratulations, you have \r identified all flags correctly.",
                fill="black",
                font=('Helvetica 15 bold'))
            
        score_canvas.pack()
        bottom_frame = Frame(self, bg="white")
        bottom_frame.pack()
        bottom_frame.place(relx=0.2, rely=0.9)
        start_button = Button(
            bottom_frame,
            width=20,
            text="Play Again",
            fg="black",
            command=lambda: controller.show_frame(start_page))
        exit_button = Button(bottom_frame, width=20, text="Exit", fg="black",
                             command=lambda: app.exit())
        start_button.pack(side=LEFT, padx=5, pady=5)
        exit_button.pack(side=RIGHT, padx=30, pady=5)

if __name__ == "__main__":
    app = game_wrapper()
    app.resizable(0, 0)
    app.iconbitmap('icon.ico')
    background_label.image = background_image
    app.mainloop()

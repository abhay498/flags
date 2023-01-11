import pdb
from random import shuffle
import copy
import sys
import os
from tkinter import *
from tkinter import font
import random
LARGE_FONT = ('Verdana', 12)
global canvas
global background_image
global background_label
global svalue
global userscore_canvas
global shuffled_country
global counter
global right_answer_flag
from threading import Thread
global number_of_countries
counter = 0

easy_guess_country = ['Brazil', 'India', 'Belgium', 'Canada']
medium_guess_country = ['Colombia', 'Senegal', 'Wales']
hard_guess_country = ['Cambodia', 'Fiji','Laos', 'Latvia']

##easy_guess_country = ['Brazil', 'India', 'Belgium', 'Argentina', 'France', 'England', 'Spain', 'Italy', 'Netherlands', 'Portugal',
##                      'Denmark', 'Germany', 'Mexico', 'Uruguay', 'Croatia', 'Switzerland', 'Sweden', 'Japan', 'Australia', 'Ukraine',
##                      'South_Korea', 'Austria', 'Russia', 'Pakistan', 'Canada']
##
##medium_guess_country = ['Colombia', 'Senegal', 'Wales', 'Peru', 'Iran', 'Morocco', 'Serbia', 'Chile', 'Norway',
##                        'Nigeria', 'Czech_Republic', 'Costa_Rica', 'Hungary', 'Poland', 'Egypt']
##
##hard_guess_country = ['Cambodia', 'Fiji','Laos', 'Latvia', 'Lithuania', 'Malta','Moldova', 'Somalia', 'Tonga', 'Tunisia']

number_of_countries = len(easy_guess_country) + len(medium_guess_country) + len(hard_guess_country)

global chosen
global button1, button2, button3, button4, button5
global top_frame, bottom_frame
global difficulty_level
global directory
global format_image
directory = 'national_flags\\'
format_image = '.png'

def get_right_answer_flag(chosen, options_text):
    global right_answer_flag
    for i in range(0, 4):
        if chosen == options_text[i]:
            right_answer_flag = i + 1
            break
    return right_answer_flag
    
def get_difficulty_level():
            
    difficulty_level = 'easy_guess_country'
    if counter < len(easy_guess_country):
        difficulty_level = 'easy_guess_country'
    elif counter > len(easy_guess_country) - 1 and counter < len(easy_guess_country) + len(medium_guess_country):
        difficulty_level = 'medium_guess_country'
    else:
        difficulty_level = 'hard_guess_country'
        
    return difficulty_level

def function_options():

    difficulty_level = get_difficulty_level()
    if difficulty_level == 'easy_guess_country':
        active_country_list = easy_guess_country
        idx = counter
    elif difficulty_level == 'medium_guess_country':
        active_country_list = medium_guess_country
        idx = counter - len(easy_guess_country)
    else:
        active_country_list = hard_guess_country
        idx = counter - len(easy_guess_country) - len(medium_guess_country)

    chosen = active_country_list[idx]
    options_text = []
    options_text.append(chosen)
    copy_active_country_list = copy.copy(active_country_list)

    shuffle(copy_active_country_list)
    i = 0
    while len(options_text) != 4:
        if copy_active_country_list[i] == chosen:
            continue
        options_text.append(copy_active_country_list[i])
        i += 1
    shuffle(options_text)
    del copy_active_country_list[:]
    return chosen, options_text


def change_flag(top_frame, bottom_frame, button1, button2, button3, button4, controller):
    global counter, canvas, my_image, chosen, flag, directory
    canvas.delete('all')
    #button5['state'] = DISABLED
    counter += 1

    if counter == number_of_countries:
        controller.show_frame(PlayAgainExit)
        return None
    chosen, options_text = function_options()
    right_answer_flag = get_right_answer_flag(chosen, options_text)

    location = directory + chosen + format_image

    my_image = PhotoImage(file=location)
    #canvas.create_image(160, 100, anchor=CENTER, image=my_image)
    t1= Thread(target=canvas.create_image, args =(160, 100),kwargs={'anchor':CENTER, 'image':my_image})
    t1.start()
    
    button1["text"] = options_text[0]
    button2["text"] = options_text[1]
    button3["text"] = options_text[2]
    button4["text"] = options_text[3]

    button1['state'] = NORMAL
    button2['state'] = NORMAL
    button3['state'] = NORMAL
    button4['state'] = NORMAL


def print_result(number, id_2, id_1, controller):
    global userscore_canvas, chosen, right_answer_flag, score, difficulty_level
    global button1, button2, button3, button4

    #button5['state'] = NORMAL
    
    button1['state'] = DISABLED
    button2['state'] = DISABLED
    button3['state'] = DISABLED
    button4['state'] = DISABLED

    if right_answer_flag == number:
        userscore_canvas.itemconfigure(id_2, text="Right")
        difficulty_level = get_difficulty_level()
        if difficulty_level == 'easy_guess_country':
            score = score + 10
        elif difficulty_level == 'medium_guess_country':
            score = score + 15
        else:
            score = score + 25

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
        text=("File version : 1.0\r\rEmail : hello@gmail.com"),
        font=(
            "Comic Sans",
            10))

class GameWrapper(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('500x550')
        self.title("flags")
        self.frames = {}
        self.configure(bg="white")
        self.name = ''
        
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (StartPage, FlagsPage, PlayAgainExit):
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

class FlagsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        global canvas, score, userscore_canvas, counter, country, shuffled_country
        global button1, button2, button3, button4, right_answer_flag, button5
        score = 0
        canvas = Canvas(self, width=320, height=200)
        canvas.pack()
        canvas.place(relx=0.20, rely=0.3)

        location = directory + easy_guess_country[0] + format_image
        
        filename = PhotoImage(file=location)
        Frame.filename = filename
        image_container = canvas.create_image(160, 100, anchor=CENTER, image=filename)

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
        id_2 = userscore_canvas.create_text(300, 30, font=("Comic Sans", 10))

        # Set the options here
        chosen, options_text = function_options()
        right_answer_flag = get_right_answer_flag(chosen, options_text)

        button1 = Button(
            top_frame,
            width=20,
            text=options_text[0],
            fg="black",
            #command=lambda: print_result(1,id_2,id_1,controller))
            command= lambda: Thread(target=print_result, args =(1, id_2, id_1, controller)).start())
        button2 = Button(
            top_frame,
            width=20,
            text=options_text[1],
            fg="black",
            #command=lambda: print_result(2,id_2,id_1,controller))
            command=lambda: Thread(target=print_result, args =(2, id_2, id_1, controller)).start())
        button3 = Button(
            bottom_frame,
            width=20,
            text=options_text[2],
            fg="black",
            #command=lambda: print_result(3,id_2,id_1,controller))
            command= lambda: Thread(target=print_result, args =(3, id_2, id_1, controller)).start())
        button4 = Button(
            bottom_frame,
            width=20,
            text=options_text[3],
            fg="black",
            #command=lambda: print_result(4,id_2,id_1,controller))
            command= lambda: Thread(target=print_result, args =(4, id_2, id_1, controller)).start())
        button1.pack(side=LEFT, padx=5, pady=5)
        button2.pack(side=RIGHT, padx=5, pady=5)
        button3.pack(side=LEFT, padx=5, pady=5)
        button4.pack(side=RIGHT, padx=5, pady=5)

        button5 = Button(
            next_frame,
            width=20,
            text="next",
            fg="black",
            #command=lambda: change_flag(top_frame,bottom_frame,button1,button2,button3,button4,controller))
            command=lambda: Thread(target=change_flag, args =(top_frame,bottom_frame,button1,button2,button3,button4,controller)).start())
            
        button5.pack(side=RIGHT, padx=5, pady=5)

        menubar = Menu(self)

        # File
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Start", command=lambda: restart_program())
        filemenu.add_command(label="Exit", command=lambda: app.exit())
        menubar.add_cascade(label="File", menu=filemenu)

        # Help
        helper = Menu(menubar, tearoff=0)
        helper.add_command(label="About", command=lambda: about())
        menubar.add_cascade(label="Help", menu=helper)

        controller.configure(menu=menubar)


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.configure(bg="white")
        play_button_font = font.Font(family='Arial', size=10)
        play_button = Button(
            self,
            width=50,
            text='Play',
            fg='black',
            command=lambda: controller.show_frame(flags_page),
            height=4,
            font=play_button_font)
        play_button.pack(side=BOTTOM, padx = 10, pady = 150)
        
        label = Label(self, text='Name', font=("Arial ", 15))
        label.pack(side=LEFT, padx = 40, pady = 30)

        name_variable = StringVar()
        name_entry = Entry(self,width=30,textvariable = name_variable, font=('Arial 15'))
        name_entry.pack(side=LEFT, padx = 10)

class PlayAgainExit(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg="white")
        global counter, app, number_of_countries
        score_canvas = Canvas(self, width=500, height=700, bg="white")
        
        score_canvas.create_text(
                300,
                50,
                text="End of the game",
                fill="black",
                font=('Arial 15 bold'))
            
        score_canvas.pack()
        bottom_frame = Frame(self, bg="white")
        bottom_frame.pack()
        bottom_frame.place(relx=0.2, rely=0.9)
        start_button = Button(
            bottom_frame,
            width=20,
            text="Play Again",
            fg="black",
            command=lambda: restart_program())
        exit_button = Button(bottom_frame, width=20, text="Exit", fg="black",
                             command=lambda: app.exit())
        start_button.pack(side=LEFT, padx=5, pady=5)
        exit_button.pack(side=RIGHT, padx=30, pady=5)

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    app = GameWrapper()
    app.resizable(0, 0)
    app.iconbitmap('icon.ico')
    app.mainloop()

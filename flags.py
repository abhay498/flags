"""A game where you need to guess the flag of a country.

You can guess the flag of the country using four options presented to you.
This program uses tkinter package.Flags are categorized into three categories
easy, medium and hard.Each correct answer fetches you points that will be displayed
on the GUI.All the flag images are stored in national_flags directory in .png format.
mainloop() method puts everything on the display, and responds to user input until
the program terminates.app is an instance of GameWrapper class which inherits Tk.

Typical usage example:

  app = GameWrapper()
  app.mainloop()
"""

##########################################################################
#           import statement section
##########################################################################

import pdb

import os
import sys
import copy
from random import shuffle
from threading import Thread
from tkinter import font, Tk, Frame, Button, BOTTOM, Label, LEFT, RIGHT
from tkinter import Entry, Canvas, PhotoImage, CENTER, X, Menu, NORMAL
from tkinter import DISABLED, Toplevel, StringVar

##########################################################################

canvas = None
background_image = None
background_label = None
svalue = None
userscore_canvas = None
right_answer_flag = None
counter = 0
score = None

easy_guess_country = [
    "Brazil",
    "India",
    "Belgium",
    "Argentina",
    "France",
    "England",
    "Spain",
    "Italy",
    "Netherlands",
    "Portugal",
    "Denmark",
    "Germany",
    "Mexico",
    "Uruguay",
    "Croatia",
    "Switzerland",
    "Sweden",
    "Japan",
    "Australia",
    "Ukraine",
    "South_Korea",
    "Austria",
    "Russia",
    "Pakistan",
    "Canada"]

medium_guess_country = [
    "Colombia",
    "Senegal",
    "Wales",
    "Peru",
    "Iran",
    "Morocco",
    "Serbia",
    "Chile",
    "Norway",
    "Nigeria",
    "Czech_Republic",
    "Costa_Rica",
    "Hungary",
    "Poland",
    "Egypt"]

hard_guess_country = [
    "Cambodia",
    "Fiji",
    "Laos",
    "Latvia",
    "Lithuania",
    "Malta",
    "Moldova",
    "Somalia",
    "Tonga",
    "Tunisia"]

number_of_countries = len(easy_guess_country) + \
    len(medium_guess_country) + len(hard_guess_country)

button_one = button_two = button_three = button_four = button_five = None
top_frame = bottom_frame = None
difficulty_level = None
DIRECTORY = 'national_flags\\'
FORMAT_IMAGE = '.png'


def get_right_answer_flag(chosen, options_text):
    """Fetches country's name of the displayed flag from the options.

    Retrieves country's name of the displayed flag from a list of options.

    Args:
        chosen: An open smalltable.Table instance.
        options_text: A list of four countries name wherein one is the name of
                      the country to which the displayed flag belongs.

    Returns:
        A string referencing the name of the correct country of the flag.
    """
    global right_answer_flag
    for i in range(0, 4):
        if chosen == options_text[i]:
            right_answer_flag = i + 1
            break
    return right_answer_flag


def get_difficulty_level():
    """Fetches the level of difficulty of the country's name to guess

    Retrieves the level of difficulty of the flag country's name to guess

    Args:
        None

    Returns:
        A string which tells how easy or difficult is to guess the name of the
        country of the displayed flag.

    """
    difficulty_level = "easy_guess_country"
    if counter < len(easy_guess_country):
        difficulty_level = "easy_guess_country"
    elif len(easy_guess_country) - 1 < counter < len(easy_guess_country) + \
            len(medium_guess_country):

        difficulty_level = "medium_guess_country"
    else:
        difficulty_level = "hard_guess_country"

    return difficulty_level


def function_options():
    """Gives the list of options along with the correct country name

    Gives the list of options which are countries name and also the correct
    name of the country to which the flag belongs.

    Args:
        None

    Returns:
        A list of options of four countries and the correct country name
        to which the flag belongs to.
    """
    difficulty_level = get_difficulty_level()
    if difficulty_level == "easy_guess_country":
        active_country_list = easy_guess_country
        idx = counter
    elif difficulty_level == "medium_guess_country":
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
    return (chosen, options_text)


def change_flag(button_one, button_two, button_three, button_four, controller):
    """Changes the picture of the flag in the frame

    Changes the picture of the flag in the frame along with the
    options.

    Args:
        button_one: Represents the first option
        button_two: Represents the second option
        button_three: Represents the third option
        button_four: Represents the fourth option
        controller: GameWrapper object used here to bring PlayAgainExit Page to the top
                    when all answers are correct.

    Returns:
        None
    """
    global counter, canvas, my_image
    canvas.delete("all")
    # button_five['state'] = DISABLED
    counter += 1

    if counter == number_of_countries:
        controller.show_frame(PlayAgainExit)
        return

    chosen, options_text = function_options()
    right_answer_flag = get_right_answer_flag(chosen, options_text)

    location = DIRECTORY + chosen + FORMAT_IMAGE

    my_image = PhotoImage(file=location)
    # canvas.create_image(160, 100, anchor=CENTER, image=my_image)
    thread_canvas_create = Thread(
        target=canvas.create_image, args=(
            160, 100), kwargs={
            'anchor': CENTER, 'image': my_image})
    thread_canvas_create.start()

    button_one["text"] = options_text[0]
    button_two["text"] = options_text[1]
    button_three["text"] = options_text[2]
    button_four["text"] = options_text[3]

    button_one["state"] = NORMAL
    button_two["state"] = NORMAL
    button_three["state"] = NORMAL
    button_four["state"] = NORMAL


def print_result(number, id_2, id_1, controller):
    """Prints whether the answer is right or wrong and if right increments the score.

    Prints whether the answer is right or wrong and if the answer is right increments the score
    according the level of difficulty.Disables the options.

    Args:
        number: Represents which button is clicked.
        id_2: Creates Right / Wrong text as per the answer inside the frame using Canvas class.
        id_1: Creates text Score and the current score value in text inside the frame using
              Canvas class.
        controller: GameWrapper object used here to bring PlayAgainExit Page to the top
                    if any answer is wrong.

    Returns:
        None
    """
    global userscore_canvas, score, difficulty_level
    global button_one, button_two, button_three, button_four

    # button_five['state'] = NORMAL

    button_one["state"] = DISABLED
    button_two["state"] = DISABLED
    button_three["state"] = DISABLED
    button_four["state"] = DISABLED

    if right_answer_flag == number:
        userscore_canvas.itemconfigure(id_2, text="Right")
        difficulty_level = get_difficulty_level()
        if difficulty_level == "easy_guess_country":
            score = score + 10
        elif difficulty_level == "medium_guess_country":
            score = score + 15
        else:
            score = score + 25

        userscore_canvas.itemconfigure(id_1, text=("Score", score))
    else:
        userscore_canvas.itemconfigure(id_2, text="Wrong")
        controller.show_frame(PlayAgainExit)


def about():
    """Opens a window which gives respective information about the version.

    Opens About window of the game when top level option about is clicked.
    Gives information about file version and mail id of the author.

    Args:
        None

    Returns:
        None
    """
    window = Toplevel()
    window.title("About flags")
    window.geometry("400x400")
    window.iconbitmap('icon.ico')
    window.resizable(0, 0)
    canvas = Canvas(window, width=400, height=400, bg='white')
    canvas.pack()
    canvas.create_text(
        150,
        150,
        text=("File version : 1.0\r\rEmail : hello@gmail.com"),
        font=(
            "Comic Sans",
            10))


class GameWrapper(Tk):
    """Inherits Tk class

    Sets the geometry, title, number of frames, background colour
    of the application.Instantiates the Frame class.

    Attributes:
        geometry: Sets the dimensions of the GUI.
        title: Sets the title of the application which is flags.
        frames: Dictionary of frames
        configure: Configures the background of the Frame with white color.
    """

    def __init__(self, *args, **kwargs):
        """Inits GameWrapper Class"""
        Tk.__init__(self, *args, **kwargs)
        self.geometry('500x550')
        self.title("flags")
        self.frames = {}
        self.configure(bg="white")

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Populating the tuple with all the possible pages to the game.
        for F in (StartPage, FlagsPage, PlayAgainExit):
            # pdb.set_trace()
            frame = F(container, self)
            self.frames[F] = frame
            # "nsew" corresponds to directions (north, south, east, west).
            frame.grid(row=0, column=0, sticky="nsew")

        # (Pdb) F
        # <class '__main__.StartPage'>
        ##
        # (Pdb) container
        # <tkinter.Frame object .!frame>
        ##
        # (Pdb) self
        # <__main__.GameWrapper object .>
        ##
        # (Pdb) frame
        # <__main__.StartPage object .!frame.!startpage>
        ##
        # (Pdb) self.frames
        # {<class '__main__.StartPage'>: <__main__.StartPage object .!frame.!startpage>}
        # (Pdb) StartPage
        # <class '__main__.StartPage'>
        # (Pdb)

        self.show_frame(StartPage)

    def show_frame(self, controller_key):
        """Brings the frame to the top for the user to see.

        Brings the frame to the top for the user to see using tkraise().

        Args:
            controller_key: Key to the value in dictionary self.frames.
                            Key represents the class corresponding to a Page.
                            Value here is an object.Value represents the frame
                            to be brought to the top for user to see.

        Returns:
            None
        """
        frame = self.frames[controller_key]
        frame.tkraise()

    def exit(self):
        """Destroys the window of the game."""
        self.destroy()


class FlagsPage(Frame):
    """Frame where the flag and respective options are displayed

    Frame where the flag and respective four options are displayed.
    Button objects are created.File menu and help menu are created.

    Attributes:
        parent: Frame object
        controller: GameWrapper object
    """

    def __init__(self, parent, controller):
        """Inits FlagsPage"""
        Frame.__init__(self, parent)
        global canvas, score, userscore_canvas, counter
        global button_one, button_two, button_three, button_four, right_answer_flag, button_five
        score = 0
        canvas = Canvas(self, width=400, height=400)
        canvas.pack()
        canvas.place(relx=0.20, rely=0.3)

        location = DIRECTORY + easy_guess_country[0] + FORMAT_IMAGE

        filename = PhotoImage(file=location)
        Frame.filename = filename
        canvas.create_image(160, 100, anchor=CENTER, image=filename)

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

        # Options are set here
        chosen, options_text = function_options()
        right_answer_flag = get_right_answer_flag(chosen, options_text)

        button_one = Button(
            top_frame,
            width=20,
            text=options_text[0],
            fg="black",
            command=lambda: Thread(
                target=print_result,
                args=(
                    1,
                    id_2,
                    id_1,
                    controller)).start())
        button_two = Button(
            top_frame,
            width=20,
            text=options_text[1],
            fg="black",
            command=lambda: Thread(
                target=print_result,
                args=(
                    2,
                    id_2,
                    id_1,
                    controller)).start())
        button_three = Button(
            bottom_frame,
            width=20,
            text=options_text[2],
            fg="black",
            command=lambda: Thread(
                target=print_result,
                args=(
                    3,
                    id_2,
                    id_1,
                    controller)).start())
        button_four = Button(
            bottom_frame,
            width=20,
            text=options_text[3],
            fg="black",
            command=lambda: Thread(
                target=print_result,
                args=(
                    4,
                    id_2,
                    id_1,
                    controller)).start())
        button_one.pack(side=LEFT, padx=5, pady=5)
        button_two.pack(side=RIGHT, padx=5, pady=5)
        button_three.pack(side=LEFT, padx=5, pady=5)
        button_four.pack(side=RIGHT, padx=5, pady=5)

        button_five = Button(
            next_frame,
            width=20,
            text="next",
            fg="black",
            command=lambda: Thread(
                target=change_flag,
                args=(
                    button_one,
                    button_two,
                    button_three,
                    button_four,
                    controller)).start())

        button_five.pack(side=RIGHT, padx=5, pady=5)

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
    """Presents the first interface of the game.

    Presents the first interface of the game where you fill in your name
    and click on play buttong to start the game.

    Attributes:
        parent: Frame object
        controller: GameWrapper object
    """

    def __init__(self, parent, controller):
        """Inits StartPage with parent and controller."""
        Frame.__init__(self, parent)

        self.configure(bg="white")
        play_button_font = font.Font(family="Arial", size=10)
        play_button = Button(
            self,
            width=50,
            text="Play",
            fg="black",
            command=lambda: controller.show_frame(FlagsPage),
            height=4,
            font=play_button_font)
        play_button.pack(side=BOTTOM, padx=10, pady=150)

        label = Label(self, text="Name", font=("Arial ", 15))
        label.pack(side=LEFT, padx=40, pady=30)

        name_variable = StringVar()
        name_entry = Entry(
            self,
            width=30,
            textvariable=name_variable,
            font=('Arial 15'))
        name_entry.pack(side=LEFT, padx=10)


class PlayAgainExit(Frame):
    """Last frame of the game.

    Last frame of the game where you are presented with the option
    of Play again button which when clicked start the game from start
    and exit button which when clicked destroys the window and ends the game.

    Attributes:
        parent: Frame object
        controller: GameWrapper object
    """

    def __init__(self, parent, controller):
        """Inits PlayAgainExit with parent."""
        Frame.__init__(self, parent)
        self.configure(bg="white")
        score_canvas = Canvas(self, width=500, height=700, bg="white")

        score_canvas.create_text(
            300,
            50,
            text="End of the game",
            fill="black",
            font=("Arial 15 bold"))

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

    Restarts the program when Play again is clicked.
    Note: this function does not return. Any clean up action
    (like saving data) must be done before calling this function.

    Args:
        None

    Returns:
        None
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)


if __name__ == "__main__":
    app = GameWrapper()
    app.resizable(0, 0)
    app.iconbitmap("icon.ico")
    app.mainloop()

import webbrowser
from functools import partial
from threading import Thread
from time import sleep
from tkinter import *

import pyautogui

running_job = False
# Creating the main Window
win = Tk()
win.config(bg="#010101")
win.title("LOL Queue Search | A Eco Community Project")
win.geometry("450x350")

# win.wm_iconbitmap('icon.ico')
icon = PhotoImage(file = 'icon.png') # Set the icon for the program
win.iconphoto(False, icon) # Set the icon for the program

win.columnconfigure(0, weight=1)   # Set weight to row and 
win.rowconfigure(0, weight=1)      # column where the widget is

container = Frame(win, background='#010101')   # bg color to show extent
container.grid(row=0, column=0)     # Grid cell with weight

my_menu = Menu(win) # Menu
win.config(menu=my_menu)

# Function to move the mouse
def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Function to check if the queue appears in screen
def check_screen():
    matches = ['queue.png', 'accept.png']
    for image in matches:
        button_pos = pyautogui.locateOnScreen(image, confidence=0.4)
        if button_pos != None:
            print("Image found at coordinates:", button_pos.left, button_pos.top)
            click(button_pos.left, button_pos.top)
            return True
    return False

def experiment():
    queue_counter = 0
    lbl = Label(container, text = "I'm Looking The Queue...") 
    lbl.grid(row=4, pady=15, sticky='ew')
    lbl.config(bg="#21AD02", font=('Poppins 10 bold'), fg="white")
    while running_job:
       if check_screen():
        queue_counter += 1
        lbl.destroy() 
        lbl1 = Label(container,text = "Queue Accepted") 
        lbl1.grid(row=4, pady=15, sticky='ew')
        lbl1.config(bg="#21AD02", font=('Poppins 10 bold'), fg="white")
        # Queue Counter Label
        lblqc = Label(container,text = f'Queues Accepted: {queue_counter}') 
        lblqc.grid(row=5, pady=8, sticky='ew')
        lblqc.config(bg="#000", font=('Poppins 10 bold'), fg="white")
        # I changed it to 1 sec to make it easier to test
        sleep(16)
        
class GUI:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        
        command = partial(run_threaded, experiment)
        self.button1 = Button(container, text="Search Queue", command=command, bg="#010101", font=('Poppins 10 bold'), fg="white", cursor="hand2")
        self.button1.grid(pady=10, padx=20, sticky='ew')
        self.button2 = Button(container, text="Stop Search", command=stop_button, bg="#010101", font=('Poppins 10 bold'), fg="white", cursor="hand2")
        self.button2.grid(pady=10, padx=20, sticky='ew')

        # Create a Menu File
        file_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Search Queue", command=command)
        file_menu.add_command(label="Stop Search", command=stop_button)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=win.quit)
        # Create a Help Menu
        help_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)
        # file_menu.add_separator()
        help_menu.add_command(label="Discord", command=lambda : webbrowser.open_new_tab("https://discord.com/invite/HahR7qjQ7s"))

        # Create a Donate Menu
        donate_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Donate", menu=donate_menu)
        # file_menu.add_separator()
        donate_menu.add_command(label="Patreon", command=lambda : webbrowser.open_new_tab("https://www.patreon.com/EcoBot791"))

def run_threaded(job_func):
    global running_job
    running_job = True
    job_thread = Thread(target=job_func, daemon=True)
    job_thread.start()

def stop_button():
    lbl = Label(container, text = "Stop Looking At The Queue") 
    lbl.grid(row=4, pady=15, sticky='ew')
    lbl.config(bg="#21AD02", font=('Poppins 10 bold'), fg="white")
    global running_job
    running_job = False



# Window Title
label=Label(container, text="LoL Queue Search", font=('Poppins 16 bold'),fg="white", bg="#010101")
label.grid(pady=10, padx=20)

# Create a label for the footer 
footer_label = Label(win, text="A Eco Community Project", bg="#035419", fg="white",font=('Poppins 9'))
footer_label.grid(sticky='ew')

# Create a grid for the footer 
for i in range(3): 
    Grid.columnconfigure(container, i, weight=1) 

for i in range(2): 
    Grid.rowconfigure(container, i, weight=1) 

# Executando o loop da win
app = GUI(win)
win.mainloop()
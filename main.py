from cProfile import label
from cgitb import text
from concurrent.futures import thread
from datetime import datetime, timedelta
from glob import glob
from struct import pack
from time import sleep, strptime
from tkinter import Button
import tkinter as tk
from tkinter import *
from tkinter import ttk
from threading import Thread
from click import command



class Counter():
    '''Periodically print counter value to stdout'''
    def __init__(self, parent, end, start=0, increment=1, interval=1000):
        self.parent = parent
        self.start_value = start
        self.end_value = end
        self.increment = -increment if (end - start) * increment < 0 else increment
        self.interval = interval
        self.value = start
        self.running = True

    def start(self):
        '''Start counter'''
        self.value = self.start_value
        self.running = True
        self.doit()
 
    def stop(self):
        '''Stop counter'''
        self.running = False

running = True

txt_open = open('tomorrow-time.txt', 'r')

'Functions:'

# gets the time 24h from now and saves it to a txt
def set_time_tomorrow():
    global stop
    stop = 0
    global text
    txt_open = open('tomorrow-time.txt', 'w+')
    tomorrow = datetime.now() + timedelta(hours=23, minutes=59, seconds=59, microseconds=999999)
    txt_open.write(str(tomorrow))
    txt_open = open('tomorrow-time.txt', 'r')
    time_txt = open('time-left.txt', 'w+')
    get_date = txt_open.read()
    conv_date = datetime.strptime(get_date, '%Y-%m-%d %H:%M:%S.%f')
    today = datetime.now()
    tm_lft = conv_date - today
    time_txt.write(str(tm_lft))
    time_txt.close()
    time_txt = open('time-left.txt', 'r')
    get_time = time_txt.read()
    text = tk.Label(root, text=str(get_time))
    text.pack()

def set_time_btn():
    root.after(250, set_time_tomorrow())

# makes a text label with the data from time-left.txt
def draw():
    global text
    time_txt = open('time-left.txt', 'r')
    get_time = time_txt.read()
    text = tk.Label(root, text=str(get_time))
    text.pack()

# reads and writes to time-left.txt every second and refreshes the message box
def refresh():
    global text
    txt_open = open('tomorrow-time.txt', 'r')
    time_txt = open('time-left.txt', 'w+')
    get_date = txt_open.read()
    conv_date = datetime.strptime(get_date, '%Y-%m-%d %H:%M:%S.%f')
    today = datetime.now()
    tm_lft = conv_date - today
    time_txt.write(str(tm_lft))
    time_txt.close()
    time_txt = open('time-left.txt', 'r')
    get_time = time_txt.read()
    text.configure(text=str(get_time))
    time_txt.close()
    root.after(1000, refresh)

# to get rid of old times
def on_click():
    root.after(10, text.destroy)

# to stop it from refreshing. Not working
# def stop():
#     nope = thread._shutdown
#     return nope

    


'Messagebox'
root = tk.Tk()
root.title('Elite chest cooldown')

# not working
# counter = Counter(root, 0, 10)

# def button_stop():
#     counter.stop()


# box layot and buttons
root.geometry("300x150+50+50")
txt_open = open('tomorrow-time.txt', 'r')
ttk.Button = Button(root, text = 'Start timer', command = lambda:[on_click(), set_time_btn(), refresh()]).pack()
ttk.Button = Button(root, text = 'Continue', command = lambda:[on_click(), draw(), refresh()]).pack()
ttk.Button = Button(root, text = 'Clear', command = lambda:[on_click()]).pack()

draw()


root.mainloop()
from cProfile import label
from cgitb import text
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




txt_open = open('tomorrow-time.txt', 'r')

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
    get_date = txt_open.read(microsecond = 0)
    conv_date = datetime.strptime(get_date, '%Y-%m-%d %H:%M:%S.%f')
    today = datetime.now()
    tm_lft = conv_date - today
    ms_remove = tm_lft.replace()
    time_txt.write(str(ms_remove))
    time_txt.close()
    time_txt = open('time-left.txt', 'r')
    get_time = time_txt.read()
    text = tk.Label(root, text=str(get_time))
    text.pack()

# reads the txt and subtract current time from it
# def time_left():
#     global tm_lft
#     txt_open = open('tomorrow-time.txt', 'r')
#     time_txt = open('time-left.txt', 'w+')
#     get_date = txt_open.read()
#     conv_date = datetime.strptime(get_date, '%Y-%m-%d %H:%M:%S.%f')
#     today = datetime.now()
#     tm_lft = conv_date - today
#     time_txt.write(str(tm_lft))
#     time_txt.close()
#     return tm_lft



def draw():
    global text
    global stop
    stop = 0
    time_txt = open('time-left.txt', 'r')
    get_time = time_txt.read()
    text = tk.Label(root, text=str(get_time))
    text.pack()

def refresh():
    global stop
    stop = 0
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

def on_click():
    root.after(1, text.destroy)

def stop():
    global stop
    sleep(1)
    stop = 1



#print('Press "T" to set timer \n Press "N" To see time left')

# waits for the right inputs and runs the corresponing inputs
#while i == 0:

    #while i == 0:


        #inp = input('Set timet or show time left?\n')
root = tk.Tk()
i = 0



root.geometry("300x150+50+50")
txt_open = open('tomorrow-time.txt', 'r')
ttk.Button = Button(root, text = 'Set Timer', command = lambda:[on_click(), set_time_tomorrow(), stop()]).pack()
ttk.Button = Button(root, text = 'Start', command = lambda:[on_click(), draw(), refresh()]).pack()
ttk.Button = Button(root, text = 'Clear', command = lambda:[on_click(), stop()]).pack()


# txt_open = open('tomorrow-time.txt', 'r')
# time_txt = open('time-left.txt', 'r')
# get_time = time_txt.read()


draw()

root.mainloop()
        # if set_time_btn.pre:
        #     set_time_tomorrow()
        #     txt_open.close()
        #     print('Timer set')
        #     #break
        
        # elif inp.lower() == 'n':
        #     time_left()
        #     #break
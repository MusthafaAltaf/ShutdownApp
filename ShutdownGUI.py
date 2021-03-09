##stuff to figure out
##change the button and label sizes 
##change this gui app to an exe file 

import tkinter as tk
from tkinter import Text,Tk
import os

##function that runs the shutdown command
def Shutdown() :
    hours_int = int(hours.get())
    minutes_int = int(minutes.get())
    total_time_in_minutes = hours_int*60 + minutes_int
    total_time_in_seconds = total_time_in_minutes*60

    os.system("shutdown /s /t " + str(total_time_in_seconds))


def AbortShutdown() :
    os.system("shutdown /a")


##Gui start
master = tk.Tk()

master.geometry("400x300")
master.title("Shutdown")

tk.Label(master, text = "Hours", height="4", width="15").grid(row=1)
tk.Label(master, text = "Minutes", height="4", width="15").grid(row=3)

hours = tk.Entry(master)
minutes = tk.Entry(master)

hours.grid(row=1, column=1)
minutes.grid(row=3, column=1)

tk.Button(master, text = "Quit", command = master.quit, width="15", height="2").grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(master, text = "run", command = Shutdown, width="15", height="2").grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(master, text = "Abort Shutdown", command = AbortShutdown, width="15", height="2").grid(row=4, column=3, sticky=tk.W, pady=4)

master.mainloop()
##Gui end





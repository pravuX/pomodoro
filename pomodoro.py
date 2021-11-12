#!/usr/bin/env python3
import sys
import os
import re
from time import sleep
from notifypy import Notify
import add_sessions

clear = lambda: os.system("clear")
alarm_clock = "alarm_clock.mp3"
# --really-quiet flag is passed to keep the terminal clean
play = lambda: os.system(f"mpv --really-quiet {alarm_clock}")

def getTime(time):
        # time is provided in seconds and returned as mm:ss
        mins = str(time // 60)
        secs = str(time % 60)
        fmt_min = "0" + mins if len(mins) == 1 else mins
        fmt_sec = "0" + secs if len(secs) == 1 else secs
        return f"{fmt_min}:{fmt_sec}"

def notify(type):
    # type is the type of notification to send i.e. Break or Session
    sleep(0.5)
    notification = Notify()
    notification.title = "PoPy - Notify"
    notification.message = f"{type} Completed"
    notification.send()
    play()

def timer(set_session, type):
    # type is Break or Session
    clear()
    print(f"Starting {type}... ")
    sleep(0.5)
    for i in range(int(set_session)*60, 0, -1):
        clear()
        print(getTime(i))
        sleep(1)
    clear()
    notify(type)

# Exactly one argument must be provided
    # and in the proper format for the program to work
if 1 < len(sys.argv) < 3:
    # Set necessary variables
    set_time = sys.argv[1]
    set_session = re.split(r"\+", set_time)[0]
    set_break = re.split(r"\+", set_time)[1]
    # Then start the session
    timer(set_session, "Session")
    add_sessions.update_or_add_pomodoro_count()
    # Prompt user for break
    print("Start Break(type yes, or no): ")
    ans = input()
    if ans == "yes":
        timer(set_break, "Break")
    sys.exit()
else:
    print(
"""Invalid Argument. Please specify a session in the following format.
session_length+break_length
For example: 25+5, 90+10""")
    sys.exit()

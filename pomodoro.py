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
        mins = time // 60
        secs = time % 60
        return f"{mins:02d}:{secs:02d}"

def notify(type):
    # type is the type of notification to send i.e. Break or Session.
    print(f"{type} Completed", end="\r")
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
        print(getTime(i), end="\r") # overwrites previous line
        sleep(1)
    clear()
    notify(type)

def start_pomdoro_session(set_time):
    set_session = re.split(r"\+", set_time)[0]
    set_break = re.split(r"\+", set_time)[1]
    # Start the session
    timer(set_session, "Session")
    # Then start the break.
    start_break(set_break)
    # Update session counter.
    add_sessions.update_or_add_pomodoro_count()


def start_prompt():
    while True:
        session_info = ''
        input_pattern = re.compile(r"\d+\+\d+")
        # Keep asking for session info untill right info is provided
        while not input_pattern.match(session_info):
            print("Enter Session Info: ")
            session_info = input("> ")
        start_pomdoro_session(session_info)
        print("Start another session? (yes or no)")
        ans = input("> ")
        # Break out of the loop is answer is no.
        if not ans.lower().startswith('y'):
            break

def start_break(set_break):
    # Prompt user for break
    print("Start Break(type yes, or no): ")
    ans = input("> ")
    if ans.lower().startswith("y"):
        timer(set_break, "Break")


def main():
    """Exactly one argument must be provided and in the proper format for the program to work"""
    arg_pattern = re.compile(r"\d+\+\d+")
    if 1 < len(sys.argv) < 3 and arg_pattern.match(sys.argv[1]):
        # Time provided by user as argument.
        set_time = sys.argv[1]
        # Start the session.
        start_pomdoro_session(set_time)
        # After the break, prompt for new session.
        print("Start a new session? (yes or no)")
        ans = input("> ")
        # Exit if answer is not yes.
        if not ans.lower().startswith('y'):
            sys.exit()
        # Else start the prompt.
        start_prompt()
    else:
        print(
    """Invalid Argument. Please specify a session in the following format.
    session_length+break_length
    For example: 25+5, 90+10""")

if __name__ == "__main__":
    main()

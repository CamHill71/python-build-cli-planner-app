# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:27:50 2022

@author: Cameron Hill
"""


import csv
from src.reminder import PoliteReminder
from src.deadlined_reminders import Datereminder


def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text,date):
    reminder = Datereminder(text,date)

    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(reminder)

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:27:50 2022

@author: Cameron Hill
"""

from abc import ABCMeta,abstractmethod,ABC
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime


class DeadlinedMetaReminder(Iterable,metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(ABC,Iterable):

    @abstractmethod
    def is_due(self):
        pass

    def __iter__(self,text,formatted_date):       
        return iter([text, formatted_date])


class Datereminder(DeadlinedReminder):
    def __init__(self,text,date) -> None:        
        self.date = parse(date,dayfirst=True)
        self.text = text

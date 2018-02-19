#!/usr/bin/env python

""" This is an example Python script for in-class editing."""


import os
import random


class Student:
    """A Student Class object for keeping track of Assignments"""
    def __init__(self, uni, github_id):

        self.uni = uni
        self.github_id = github_id
        self.repo = "https://github.com/" + self.github_id
        self.grades = {}


    ## notes with spaces at end  
    def assignment(self, index):
        self.grades[index] = random.randint(0, 100)


    def failed(self):
        if sum(self.grades.values()) < 60:
            return True
        else:
            return False

    def participation(self):
        if self.showed_up_to_class:
            return True

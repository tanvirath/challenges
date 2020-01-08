"""
Load module to filter data on fly
"""
from __future__ import print_function
import os
import sys


class Load(object):
    """
    Load class is used for exclusive dataframe filtering
    which takes `df` a csv file and convert into dataframe
    """
    def __init__(self, filename):
        self.version = open('VERSION').readlines()[0]
        self.data = """W_A11,2000-02,Moving average,59.66666667,50.92582302,
                        68.40751031,Injuries,Number,Assault,Validated,Whole 
                        pop,All ages,FatalW_A11,2001-03,Moving average,60,10,
                        20,30,33,31,12,51.23477459,68.76522541,Injuries,
                        Number,Assault,Validated,Whole pop,All ages,Fatale 
                        50, 50, 60,pop,All ages,Fatal"""


    def get_version(self):
        """ Get current `version` of library"""
        return self.version


    def pick_numbers(self):
        """

        From self.data extract all numbers as a list
        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"

        :returns: [59.66666667,50.92582302,68.40751031]

        Usage:
        ======
            >> df = Load()
            >> df.pick_numbers()
            >> [1,2,3,4,5,6]

        """
        # complete code here


    def sum_all_numbers(self):
        """
        From `self.data` extract all numbers and return the sum of all numbers

        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"
        :returns 179.0

        Usage:
        ======
            >> df = Load()
            >> df.sum_all_numbers()
            >> 179.0


        """
        # complete code here


    def extract_vowels(self):
        """
        Return all vowels in the given string `self.data`

        :returns [] all vowels as list

        Usage:
        ======
            >> df = Load()
            >> df.extract_vowels()
            >> ['A', 'E', 'I', 'O']
        """


    def pick_odd_numbers(self):
        """
        Take the string from `self.data` and extract all odd numbers and return
        list of all odd numbers from the string

        :returns: [1, 3, 5]

        Usage:
        ======
            >> df = Load()
            >> df.pick_odd_numbers()
            >> [1, 3, 5]

        """
        # complete code here


    def get_mean(self):
        """
        Take the string from `self.data` and extract all numbers and return
        the mean of extracted list of numbers.

        :returns: 50

        Usage:
        ======
            >> df = Load()
            >> df.get_mean()
            >> 50
        """
        # complete code here



if __name__ == '__main__':
    # instantiate the object
    df = Load()

"""
Load module to filter data on fly
"""
from __future__ import print_function
#import os
#import sys
import re
import pandas as pd
import numpy as np



class Load(object):
    """
    Load class is used for exclusive dataframe filtering
    which takes `df` a csv file and convert into dataframe
    """

    def __init__(self, filename):
        self.version = open('VERSION').readlines()[0]
        self.df = pd.read_csv(filename)
        self.data = """W_A11,2000-02,Moving average,59.66666667,50.92582302,
                        68.40751031,Injuries,Number,Assault,Validated,Whole 
                        pop,All ages,FatalW_A11,2001-03,Moving average,60,10,
                        20,30,33,31,12,51.23477459,68.76522541,Injuries,
                        Number,Assault,Validated,Whole pop,All ages,Fatale,
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
            >> df = Load('data.csv')
            >> df.pick_numbers()
            >> [1,2,3,4,5,6]

        """
        data1 = re.sub(r'\s', '', self.data)
        arr = data1.split(',')
        global arr3 #pylint: disable=W0601
        arr3 = []
        for i in arr:
            if re.match(r'^[\d.]+[\d]$', i):
                arr3.append(i)
        print(arr3)



    def sum_all_numbers(self):  # pylint: disable=R0201
        """
        From `self.data` extract all numbers and return the sum of all numbers

        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"
        :returns 179.0

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.sum_all_numbers()
            >> 179.0


        """
        # complete code here
        global n #pylint: disable=W0601
        n = [float(i) for i in arr3]
        print(sum(n))




    def extract_vowels(self):
        """
        Return all vowels in the given string `self.data`

        :returns [] all vowels as list

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.extract_vowels()
            >> ['A', 'E', 'I', 'O']
        """
        print(re.findall(r'[aeiou]+', self.data))



    def pick_odd_numbers(self): # pylint: disable=R0201
        """
        Take the string from `self.data` and extract all odd numbers and return
        list of all odd numbers from the string

        :returns: [1, 3, 5]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_odd_numbers()
            >> [1, 3, 5]

        """
        # complete code here
        print([ele for ele in n if ele%2 != 0])


    def get_mean(self): # pylint: disable=R0201
        """
        Take the string from `self.data` and extract all numbers and return
        the mean of extracted list of numbers.

        :returns: 50

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_mean()
            >> 50
        """
        # complete code here
        print(np.average(n))


    def get_all_categorical(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which are categorical variables

        :returns:   All categorical.
        :rtype:     List

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_categorical()
            >> ['Series_reference', 'Type']
        """
        # complete code here
        print(set(self.df.columns)-set(self.df._get_numeric_data().columns)) # pylint: disable=W0212




    def get_all_continuous(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which contain categorical variables

        :returns:   All continuous.
        :rtype:    List

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_continuous()
            >> ['Lower_CI', 'Upper_CI', 'Units']
        """
        # complete code here
        print(set(self.df._get_numeric_data().columns)) # pylint: disable=W0212



    def addition(self, x, y): # pylint: disable=R0201
        """
        Take X and Y as input and now return the sum of both

        :param      x:    { parameter_description }
        :type       x:    { type_description }
        :param      y:    { parameter_description }
        :type       y:    { type_description }

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.addition(10, 20)
            >> 30
        """
        return x+y



if __name__ == '__main__':
    # instantiate the object
    df = Load('data.csv')
    print(df.addition(2, 3))
    df.pick_numbers()
    df.sum_all_numbers()
    df.extract_vowels()
    df.pick_odd_numbers()
    df.get_mean()
    df.get_all_categorical()
    df.get_all_continuous()

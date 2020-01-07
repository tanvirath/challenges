import os
import sys
import pandas as pd 
import numpy as np 



class Load:
    
    # instance attributes
    def __init__(self, df):
        self.version = open('VERSION').readlines()[0]
        self.data = pd.read_csv(df)
   
    def get_version(self):
        """ Get current `version` of library"""
        print(self.version)


    def features(self):
        """
        Take the data from the `data` attribute using `self.data`
        
        :returns:   List of all columns
        """
        return self.data.columns


    def categorical(self):

        """
        Take the dataframe from `self.data` and return the list of
        all categorical variables
        :returns: list of all columns having only continous variables `float or int`
        """

        # write code logic here


    def continuous(self):

        """
        Return the list of all continous variable from the given 
        data frame `self.data`

        :returns: list of all columns having only continous variables `float or int`
        """

        # write code logic here






# instantiate the object
load = Load('data.csv')
load.get_version()
print(load.features())
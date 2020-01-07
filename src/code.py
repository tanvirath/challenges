"""
Load module to filter data on fly
"""
import os
import sys
import pandas as pd
import numpy as np


class Load(object):
    """
    Load class is used for exclusive dataframe filtering
    which takes `df` a csv file and convert into dataframe
    """

    def __init__(self, df):
        self.version = open('VERSION').readlines()[0]
        self.data = pd.read_csv(df)


    def get_version(self):
        """ Get current `version` of library"""
        return self.version


    def features(self):
        """
        Take the data from the `data` attribute using `self.data`

        :returns:   List of all columns
        """
        return tuple(self.data.columns)


    def categorical(self):

        """
        Take the dataframe from `self.data` and return the list of
        all categorical variables
        :returns: list of all columns having only continous variables `float or int`
        """

        # code here


    def continuous(self):

        """
        Return the list of all continous variable from the given
        data frame `self.data`

        :returns: list of all columns having only continous variables `float or int`
        """

        # code here


    def discrete(self):
        """
        Return the list of all columns which contain discrete data 
        such as `age`, `marks` ..etc

        :returns: list of all columns having discrete values
        """

        # code here


    def filter(self, keys={}):
        """
        Takes the keys as `Dict` which contains the columns names and values to 
        filter
        
        :param      keys:  The keys
        :type       keys:  { type_description }
        """

        # code here





if __name__ == '__main__':
    
    # instantiate the object
    load_df = Load('data.csv')
    print(load_df.get_version())

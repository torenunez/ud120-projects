#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import os
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
dname = '/home/torenunez/Projects/ud120-projects/datasets_questions/'
os.chdir(dname)

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data.keys())

print len(enron_data['METTS MARK'].keys())

poi = 0

for key in enron_data.iterkeys():
    if enron_data[key]["poi"] == 1:
        poi += 1
print poi

for key in enron_data.iterkeys():
    if 'prentice' in key.lower():
        print key
        for key2 in enron_data[key].iterkeys():
            if 'stock' in key2.lower():
                print key2

print enron_data['PRENTICE JAMES']['total_stock_value']


for key in enron_data.iterkeys():
    if 'colwell' in key.lower():
        print key
        for key2 in enron_data[key].iterkeys():
            print key2

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

for key in enron_data.iterkeys():
    if 'skilling' in key.lower():
        print key
        for key2 in enron_data[key].iterkeys():
            print key2

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


for key in enron_data.iterkeys():
    if 'lay' in key.lower() or 'skilling' in key.lower() or 'fastow' in key.lower():
        print key
        print enron_data[key]['total_payments']


import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict(enron_data, orient ='index')
df = df.replace('NaN', np.nan)
print df.info()

print df.shape
print df.isnull().sum()

print df[df.poi]['total_payments'].isnull().sum()


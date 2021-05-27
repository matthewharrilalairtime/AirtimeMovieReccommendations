# import libraries 

import csv
from io import UnsupportedOperation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

meta_path = '/Users/addisonpolcyn/Downloads/movies_metadata.csv'
ratings_path = '/Users/addisonpolcyn/Downloads/ratings_small.csv'    

meta = {}
with open(meta_path, newline='') as csvfile:
  csv_reader = csv.reader(csvfile, quotechar='"', delimiter=',',
                          quoting=csv.QUOTE_ALL, skipinitialspace=True)
  for row in csv_reader:
    id = row[5]
    name = row[8]
    meta[id] = name

# loading csv file into pandas dataframe
# read ratings file

for key, value in meta.items():
    print(key)
    print(value)

ratings = pd.read_csv(ratings_path)

print(ratings.head())

from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(ratings, test_size = 0.40, random_state = 42)

print(X_train.shape)

# pivot ratings into movie features
user_data = X_train.pivot(index = 'userId', columns = 'movieId', values = 'rating').fillna(0)
print(user_data.head())





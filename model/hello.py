# import libraries 

import csv
from io import UnsupportedOperation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users/addisonpolcyn/airtime/tools/hackathon/AirtimeMovieReccommendations/csv/youtube_reduced_indexed_minimized.csv'

# read ratings file
user_youtube_duration_csv = pd.read_csv(path)

print(user_youtube_duration_csv.head())
print(user_youtube_duration_csv.info())


from sklearn.model_selection import train_test_split

user_youtube_duration_csv.columns = user_youtube_duration_csv.columns.str.strip()
X_train, X_test = train_test_split(user_youtube_duration_csv, test_size = 0.30, random_state = 42)

print(X_train.shape)
print(X_test.shape)


# pivot ratings into movie features
user_data = X_train.pivot(index = "userIdx", columns = "youtube", values = 'duration').fillna(0)
print(user_data.head())


# make a copy of train and test datasets
dummy_train = X_train.copy()
dummy_test = X_test.copy()

dummy_train['duration'] = dummy_train['duration'].apply(lambda x: 0 if x > 0 else 1)
dummy_test['duration'] = dummy_test['duration'].apply(lambda x: 1 if x > 0 else 0)

# The movies not rated by user is marked as 1 for prediction 
dummy_train = dummy_train.pivot(index = "userIdx", columns = "youtube", values = 'duration').fillna(1)

# The movies not rated by user is marked as 0 for evaluation 
dummy_test = dummy_test.pivot(index = "userIdx", columns = "youtube", values = 'duration').fillna(0)

print(dummy_train.head())
print(dummy_test.head())

from sklearn.metrics.pairwise import cosine_similarity

# User Similarity Matrix using Cosine similarity as a similarity measure between Users
user_similarity = cosine_similarity(user_youtube_duration_csv)
user_similarity[np.isnan(user_similarity)] = 0
print(user_similarity)
print(user_similarity.shape)
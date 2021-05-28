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
user_data = user_youtube_duration_csv.pivot(index = "userIdx", columns = "youtube", values = 'duration').fillna(0)
print('this shape')
print(user_data.shape)
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
user_similarity = cosine_similarity(user_data)
user_similarity[np.isnan(user_similarity)] = 0
print(user_similarity)
print(user_similarity.shape)

user_predicted_ratings = np.dot(user_similarity, user_data)
# user_predicted_ratings

print(user_predicted_ratings.shape)

# np.multiply for cell-by-cell multiplication 

# user_final_ratings = np.multiply(user_predicted_ratings, dummy_train)
# user_final_ratings.head()
# user_final_ratings = np.multiply(user_predicted_ratings, 1)
print(user_predicted_ratings)
# user_final_ratings.iloc[0].sort_values(ascending = False)

# normalize predictions results per user
# calculates users average duration and predicted average duration
# real_avg / pred_avg * pred_score
def normalize_predictions_per_user(user_predicted_ratings, user_data):
  print('userdata')
  print(user_data)
  print('userdata row')

  for i in range(len(user_data)):
    def calculate_row_avg(row):
      def count_non_zero_entries(row):
        count = 0
        for column in row:
          if column > 0:
            count += 1
        return count
      non_zero_entries = count_non_zero_entries(row)
      row_sum = row.sum()
      row_avg = row_sum / non_zero_entries
      return row_avg

    real_row_avg = calculate_row_avg(user_data.iloc[i])
    pred_row_avg = calculate_row_avg(user_predicted_ratings[i])
    # print('row-avg')
    # print(real_row_avg)
    # print('pred-row-avg')
    # print(pred_row_avg)
    user_predicted_ratings[i] = user_predicted_ratings[i] * (real_row_avg / pred_row_avg)
  return user_predicted_ratings

def write_json_model(user_similarity, user_predicted_ratings):
  import csv

  rows = []
  with open('/Users/addisonpolcyn/airtime/tools/hackathon/AirtimeMovieReccommendations/csv/youtube_reduced_indexed.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      rows.append(row)

  content_ids = {}
  for row in rows:
    content_idx = row[2]
    content_id = row[3]
    content_ids[int(content_idx)] = content_id

  final_results = {}

  for i in range(len(user_predicted_ratings)):
    print('user id=' + str(i))
    similarities = {}
    predictions = {}

    for j in range(len(user_similarity[i])):
      num = user_similarity[i][j]
      if num != 0:
        if num < 0.0001:
          num = 0.00011
        similarities[j] = num
    for j in range(len(user_predicted_ratings[i])):
      num = user_predicted_ratings[i][j]
      if num != 0:
        if num < 0.0001:
          num = 0.00011
        predictions[content_ids[j]] = num
      
    final_results[i] = {}
    final_results[i]['user_similarity'] = similarities
    final_results[i]['duration_predictions'] = predictions

  import json
  with open('model_results.json', 'w', encoding='utf-8') as f:
      json.dump(final_results, f, ensure_ascii=False)


print('before normalization ------------')
print(user_predicted_ratings)
user_predicted_ratings = normalize_predictions_per_user(user_predicted_ratings, user_data)

print('after ============')
print(user_predicted_ratings)
#write_json_model(user_similarity, user_predicted_ratings)



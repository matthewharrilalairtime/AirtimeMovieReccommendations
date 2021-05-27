import csv

rows = []
with open('cleaned_complete_youtube_data.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    rows.append(row)

user_dict = {}
content_dict = {}

for row in rows:
    user_id = row[1]
    content_id = row[2]

    if user_id in user_dict.keys():
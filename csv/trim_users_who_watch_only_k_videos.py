import csv

file = 'youtube_reduced.csv'
# file = 'youtube_cleaned_combined.csv'

rows = []
with open(file, newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    rows.append(row)

user_dict = {}
content_dict = {}

for row in rows:
    user_id = row[1]
    content_id = row[2]

    if user_id in user_dict.keys():
        user_dict[user_id] += 1
    else:
        user_dict[user_id] = 1

    if content_id in content_dict.keys():
        content_dict[content_id] += 1
    else:
        content_dict[content_id] = 1

cleaned_rows = []
for row in rows:
    user_id = row[1]
    if user_dict[user_id] > 2:
        cleaned_rows.append(row)


print(len(user_dict))
print(len(content_dict))

'''
# name of csv file 
filename = "youtube_reduced.csv"

# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    # writing the fields 
    # csvwriter.writerow(fields) 

    # writing the data rows 
    csvwriter.writerows(cleaned_rows)
'''
import csv

rows = []
with open('youtube_reduced.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    rows.append(row)

user_dict = {}
content_dict = {}

user_idx = 0
content_idx = 0

for row in rows:
    user_id = row[0]
    content_id = row[1]

    if user_id not in user_dict.keys():
        user_dict[user_id] = user_idx
        user_idx += 1
    if content_id not in content_dict.keys():
        content_dict[content_id] = content_idx
        content_idx += 1

print(user_dict)
print(content_dict)

new_rows = []
for row in rows:
    new_row = []

    usr = row[0]
    content = row[1]
    duration = row[2]

    new_row.append(user_dict[usr])
    new_row.append(usr)
    new_row.append(content_dict[content])
    new_row.append(content)
    new_row.append(duration)
    new_rows.append(new_row)


# name of csv file 
filename = "youtube_reduced_indexed.csv"

# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    # writing the fields 
    # csvwriter.writerow(fields) 

    # writing the data rows 
    csvwriter.writerows(new_rows)



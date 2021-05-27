import csv

rows = []
with open('raw_cleaned_hackathon.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    rows.append(row)

# 000,5,60ac27dfe8f3277f52176181,movies,0,https://deathstar.signal.is/api/v1/media/redirect/dice/video/158202/playback,173

cleaned_rows = []

for row in rows:
    timestamp = row[0]
    # user_idx = row[1]
    user_id = row[1]
    content = row[2]
    # content_idx = row[4]
    content_id = row[3]
    duration = row[4]

    # print(row)

    error = False
    # if not user_idx:
    #     error = True
    if not user_id:
        error = True
    if not timestamp:
        error = True
    if not content_id:
        error = True
    if not content:
        error = True
    # if not content_idx:
    #     error = True
    if not int(duration):
        error = True

    if error:
        print('dirty data!!!')
        print(row)
    else:
        if content == 'movies':
            cleaned_rows.append(row)

# name of csv file 
filename = "movies222_raw_cleaned_hackathon.csv"

# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    # csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(cleaned_rows)

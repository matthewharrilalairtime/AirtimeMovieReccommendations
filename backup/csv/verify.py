import csv

rows = []
with open('cleaned_complete_youtube_data.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    rows.append(row)

cleaned_rows = []
row_dict = {}

for row in rows:
    user_id = row[1]
    content_id = row[2]
    key = user_id + content_id
    ct = 0
    duration = 0
    for r in rows:
        usr_id = r[1]
        cont_id = r[2]
        if user_id == usr_id and content_id == cont_id:
            duration += int(r[3])
            ct += 1
    if ct > 1:
        print('dirty!')
        print(row)

    if key not in row_dict.keys():
        # doesnt exist, add it
        row_cpy = row
        row_cpy[3] = duration
        cleaned_rows.append(row_cpy)
        row_dict[key] = True

# name of csv file 
filename = "youtube222_raw_cleaned_hackathon.csv"

# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 

    # writing the fields 
    # csvwriter.writerow(fields) 

    # writing the data rows 
    csvwriter.writerows(cleaned_rows)

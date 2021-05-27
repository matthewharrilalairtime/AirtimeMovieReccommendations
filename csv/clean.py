import csv

rows = []
with open('movies_cleaned_w_id_id.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    rows.append(row)

# 000,5,60ac27dfe8f3277f52176181,movies,0,https://deathstar.signal.is/api/v1/media/redirect/dice/video/158202/playback,173

for row in rows:
    timestamp = row[0]
    user_idx = row[1]
    user_id = row[2]
    content = row[3]
    content_idx = row[4]
    content_id = row[5]
    duration = row[6]

    # print(row)

    error = False
    if not user_idx:
        error = True
    if not user_id:
        error = True
    if not timestamp:
        error = True
    if not content_id:
        error = True
    if not content:
        error = True
    if not content_idx:
        error = True
    if not duration:
        error = True

    if error:
        print('dirty data!!!')
        print(row)

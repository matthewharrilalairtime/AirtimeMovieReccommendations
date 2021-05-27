import csv

#ts,user_id,channel,media_url,duration

rows = []
with open('youtube222_raw_cleaned_hackathon.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    # print(', '.join(row))
    rows.append(row)

content_ids = {}

mint_id = 0

for ct, row in enumerate(rows):
    content_id = row[1]
    print(ct, row)
    print(content_id)

    if content_id in content_ids.keys():
        print('already exists with value: ')
        print(content_ids[content_id]) 
    else:
        print('giving content:' + content_id + ' new id: ' + str(mint_id))
        content_ids[content_id] = mint_id
        mint_id += 1

    #if row[2] != 'movies' and row[2] != 'youtube':
    #    print('delete this row its bad ^^^')
    #    rows.pop(ct)

print(content_ids)


for row in rows:
    content_id = row[1]
    row.append(content_ids[content_id])

# name of csv file 
filename = "youtube_raw_cleaned.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    # csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)


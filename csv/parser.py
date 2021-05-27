import csv

#ts,user_id,channel,media_url,duration


rows = []
with open('raw_hackathon.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    # print(', '.join(row))
    rows.append(row)

print('-------------')

for row in rows:
    print(row)
print('-------------')

print(rows[0])

print('-------------')
print(rows[1])

user_ids = {}

mint_id = 0

for ct, row in enumerate(rows):
    user_id = row[1]
    user_ids
    print(ct, row)
    print(user_id)
    if user_id in user_ids.keys():
        print('already exists with value: ')
        print(user_ids[user_id]) 
    else:
        print('giving user:' + user_id + ' new id: ' + str(mint_id))
        user_ids[user_id] = mint_id
        mint_id += 1
    #if row[2] != 'movies' and row[2] != 'youtube':
    #    print('delete this row its bad ^^^')
    #    rows.pop(ct)

print(user_ids)

for row in rows:
    user_id = row[1]
    row.append(user_ids[user_id])

# name of csv file 
filename = "raw_hackathon_cleaned.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    # csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

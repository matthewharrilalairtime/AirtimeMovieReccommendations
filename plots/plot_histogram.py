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
        user_dict[user_id] += 1
    else:
        user_dict[user_id] = 1

    if content_id in content_dict.keys():
        content_dict[content_id] += 1
    else:
        content_dict[content_id] = 1

print(user_dict)
print(content_dict)

user_values = []
for value in user_dict.values():
    user_values.append(value)

content_values = []
for value in content_dict.values():
    content_values.append(value)


import matplotlib.pyplot as plt


print('user values')
print(user_values)

# plt.hist(user_values, bins = 100)
# plt.show()

print('content values')
print(content_values)

plt.hist(content_values, bins = 1000)
plt.show()

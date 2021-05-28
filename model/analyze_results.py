import json

print('LOADING JSON FILE ===========')

with open('model_results.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)

# id = "4"
# sim = data[id]["user_similarity"]
# youtube = data[id]["duration_predictions"]

def get_user_results(id):
    sim = data[id]["user_similarity"]
    youtube = data[id]["duration_predictions"]    

    def get_top_n(dict, limit=10):
        count = 0
        print('-----------------')
        for w in sorted(dict, key=dict.get, reverse=True):
            count += 1
            if count > limit:
                break
            print(w, dict[w])
    print('|-----USER ' + id + '------|')
    get_top_n(sim)
    get_top_n(youtube)
    print()

# get_user_results("4")
# get_user_results("295")

while True:
    idx = input("Enter user_id index to read: ")
    get_user_results(idx)
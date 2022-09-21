with open('amazon_reviews.txt', mode='r', encoding="utf-8") as f:
    reviews = f.read().split("\n")
print(reviews[500])

for i in range(len(reviews)):
    reviews[i] = reviews[i].split("\t")

users = set()

for i in range(len(reviews)):
    users.add(reviews[i][0])
    # print(reviews[i][0])

print(users, "\n", len(users), len({k[0] for k in reviews}))

print(reviews[500])

raters = dict()

for r in reviews:
    if r[1] not in raters:
        raters[r[1]] = 1
    else:
        raters[r[1]] += 1
print(raters)

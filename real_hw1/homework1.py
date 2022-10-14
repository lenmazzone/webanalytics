# Question 1
# Politifact purports to fact-check journalists and politicians by rating specific statements by
# politicians for accuracy. They are a non-profit owned by the Poynter Institute for Media Studies.

# Question 2
with open("politifact_data.txt", mode="r", encoding="utf-8") as f:
    statements = f.read().split("\n")

statements_len = len(statements)

for i in range(statements_len):
    statements[i] = statements[i].split("\t")
    statements[i][5] = statements[i][5].split("|")

print(statements[37])

# Question 3
ratings = set()

for i in range(statements_len):
    ratings.add(statements[i][0])

print(ratings)

# Question 4
distribution = dict()

for rating in statements:
    if rating[0] not in distribution:
        distribution[rating[0]] = 1
    else:
        distribution[rating[0]] += 1

print(distribution)

# Question 5
new_statements = list()
bool_statements = {"False": 0, "Mostly False": 0, "Pants on Fire!": 0, "Mostly True": 1, "True": 1}

for i in range(statements_len):
    # print(statements[i][0], bool_statements.keys(), statements[i][0] in bool_statements.keys())
    if statements[i][0] in bool_statements.keys():
        new_statements.append(statements[i])

for item in new_statements:
    item[0] = bool_statements[item[0]]

print(new_statements[0])


# Question 6
def count_truths(name):
    lie_counter = 0
    truth_counter = 0
    for s in new_statements:
        if s[2] == name:
            # print(f"in a {name} file")
            if s[0] == 0:
                # print("One lie!")
                lie_counter += 1
            else:
                # print("One Truth!")
                truth_counter += 1
    print(f"Total {name} lies: {lie_counter}\nTotal {name} truths: {truth_counter}\n")


count_truths("donald-trump")

# Question 7
# See function defined for Question 6
count_truths("hillary-clinton")

count_truths("barack-obama")

# Question 8
subjects = dict()
for s in new_statements:
    if s[2] == "barack-obama":
        for item in s[5]:
            if item not in subjects:
                subjects[item] = 1
            else:
                subjects[item] += 1

# print(subjects)
sorted_tuples = sorted(subjects.items(), key=lambda item: item[1], reverse=True)
# In theory the answer could be: print(sorted_tuples[0:10]) but I think the below is a little cleaner.
top_ten_subjects = {k: v for k, v in sorted_tuples[0:10]}
print(f"The top ten subjects and # of mentions are: {top_ten_subjects}")

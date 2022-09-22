# Question 1
#   Politifact purports to fact-check journalism by rating specific statements by politicians for accuracy.
#   They are a non-profit owned by the Poynter Institute for Media Studies.

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

for r in statements:
    if r[0] not in distribution:
        distribution[r[0]] = 1
    else:
        distribution[r[0]] += 1

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
for item in new_statements:
    lie_counter = 0
    truth_counter = 0

    if item[2] == "donald=trump":
        if item[0] == 0:
            print("One lie!")
            lie_counter += 1
        else:
            print("One Truth!")
            truth_counter += 1

print(f"Total lies: {lie_counter}\nTotal truths: {truth_counter}")

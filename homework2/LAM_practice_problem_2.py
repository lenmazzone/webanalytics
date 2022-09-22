best_dictionary = {100: [1, 2, 3], 200: [2, 2, 3], 300: [3, 2, 3]}

for item in best_dictionary.values():
    print(item)
    if type(item) is list:
        item.append(5)
        print(item)

print(best_dictionary, "\n")

print(best_dictionary[200][2:], "\n")

print(best_dictionary[300][1:3], "\n")

best_dictionary[300].sort()
print(best_dictionary[300], "\n")

best_dictionary[100].sort(reverse=True)
print(best_dictionary[100], "\n")

print(best_dictionary[200])
best_dictionary[200][1] = 3
print(best_dictionary[200], "\n")

print("contents of key 200 == contents of key 300?", best_dictionary[200] == best_dictionary[300], "\n")


def season_finder():
    print("Please input the month you'd like to know the season for:")
    month = str(input()).lower().strip()

    months = {"Winter": ["december", "january", "february"],
              "Spring": ["march", "april", "may"],
              "Summer": ["june", "july", "august"],
              "Fall": ["september", "october", "november"]}

    for season, possible_months in months.items():
        for m in possible_months:
            if m == month:
                print("\n", season)
                break


season_finder()

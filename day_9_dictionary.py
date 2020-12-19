# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# # create an empty dict or use dict()
# student_grade = {}

# # Loop through a dictionary
# for student in student_scores:
#     # print(key)
#     # print(student_scores[key]) dic value
#     score = student_scores[student] #make easier to read code
#     if score >= 91 and score <= 100:
#         score = "Outstanding"
#     elif score >= 81:
#         score = "Exceeds Expections"
#     elif score >= 71:
#         score = "Acceptable"
#     else:
#         score = "Fail"
#     #adding new items to dictionary i.e. key = student and value = score
#     student_grade[student] = score

# print(student_grade)

# Nesting Lists and Dictionaires.
# { key: [List], Key2: {Dict},}
capitals = {"France": "Paris", "Germany": "Berlin"}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 23,
    },
}

# Nesting Dictionary in List
travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(new_country, new_visit, new_cities):
    entry = {"country": new_country, "visits": new_visit, "cities": new_cities}
    travel_log.append(entry)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

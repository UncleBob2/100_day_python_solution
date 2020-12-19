# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇

# print(student_heights)
# total = 0
# num = 0
# for student in student_heights:
#     total += int(student)
#     num += 1
# print(round(total / num))

####################################################################
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇

# h_score = 0
# for student in student_scores:
#     if student > h_score:
#         h_score = student

# print("The highest score in the class is: ", h_score)

# total = 0
# for num in range(1, 101): #make sure not including 101 but stopped at 100
#     if num % 2 == 0:
#         total += num

# print(total)

# 1 to 100
# div both 3 & 5
# fizz at 3
# buzz at 5
for num in range(1, 101):
    if (
        num % 3 == 0 and num % 5 == 0
    ):  # make sure to check fizzbuzz first else will miss it
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

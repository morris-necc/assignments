class1, class2, class3 = 32, 45, 51
quotient1, quotient2, quotient3 = class1//5, class2//7, class3//6
leftover1, leftover2, leftover3 = class1%5, class2%7, class3%6

print("Number of students in each group:\n"
    "Class 1:", quotient1,"\n"
    "Class 2:", quotient2,"\n"
    "Class 3:", quotient3)
print("Number of students in each group:\n"
    "Class 1:", leftover1,"\n"
    "Class 2:", leftover2,"\n"
    "Class 3:", leftover3)

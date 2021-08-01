last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#'Merge' the list
gradebook = [["physics", 89], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

# Append
print("\n")
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

print("\n")
gradebook[5][1] = 98
print(gradebook)

gradebook.remove(["visual arts", 98])
gradebook.append(["visual arts", "pass"])

full_gradebook = last_semester_gradebook + gradebook
print("\n")
print(full_gradebook)

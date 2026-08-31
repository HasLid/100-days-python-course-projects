# using the sum() function to calculate the total of a list of student scores

student_scores = [85, 90, 78, 92, 88]
# total_score = sum(student_scores)
# print("Total scores: ", total_score)

# How to loop through and pick max score from the list of student scores
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print("Maximum score: ", max_score)
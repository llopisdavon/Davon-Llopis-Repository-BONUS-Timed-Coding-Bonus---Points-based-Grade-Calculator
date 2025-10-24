print("Grade Calculator")
print("----------------")

num_assignments = int(input("How many assignments are in this class? "))
total_points_earned = 0
total_points_possible = num_assignments * 100

for i in range(1, num_assignments + 1):
    score = float(input(f"What is the score for assignment no. {i}? "))
    total_points_earned += score

    final_score = (total_points_earned / total_points_possible) * 100 
    print(f"The final score is {final_score:.1f}%")
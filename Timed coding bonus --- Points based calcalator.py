def grade_calculator():
    print("Grade Calculator")
    print("----------------")
    print("This program calculatores your fianl percetage score.")

    POINTS_POSSIBLE_PER_ASSIGNMENT= 100

    while True:
        num_assignments_input = input("/nHow many assignments are in this class?")
        if num_assignments_input.isdigit():num_assignmentsm= int (num_assignments_input> 0:
        if num_assignments > 0:
            break
            else:
            print("Enter a postive number.")
            else:
            print("Invalid input. Enter a whole number.")

            total_points_earned = 0
            total_points_possible =
            num_assignments *
            POINTS_POSSIBLE_PER_ASSIGNMENT

            for i in range( 1, num_assignments + 1):
            
        while True:
        score_input = input(f"What is the score for assignment no. {i}?")

        if all(c.isdigit() or c == '.' for c in score_input) and socre_input.count('.') <= 1 and score_input:
            score = 
        float(score_input)
        if 0 <= score <=
        POINTS_POSSIBLE_PER_ASSIGNMENT:
        total_points_earned += score 
        break
        else: 
        print(f"Score must be between 0 and {POINTS_POSSIBLE_PER_ASSIGNMENT}.")
        else:
        print("Invaild input. Enter a numerical score.")
        if total_points_possible > 0:
        final_score =
        (total_points_earned / total_points_possible) * 100
        else:
        final_score = 0

        print("/n--- Final Results---")
        print(f"Total points earned:
              {total_points_earned} out of {total_points possible} possible points.")
        print(f"The final score is {final_score:.1f}%")

        if __name__ == "__main__":
        grade_calculator():
# grade_checker_functions.py

# Function to get student's name
def get_name():
    name = input("Enter your name: ")
    return name


# Function to get course name
def get_course():
    course = input("Enter your course: ")
    return course


# Function to get a valid score
def get_score():
    while True:
        try:
            score = int(input("Enter your score (0 - 100): "))
            
            # Check if score is within valid range
            if score < 0 or score > 100:
                print("Invalid input! Score must be between 0 and 100.")
            else:
                return score  # valid input
                
        except ValueError:
            # Handles non-integer input
            print("Invalid input! Please enter a number.")


# Function to determine the grade
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


# Function to display full result
def display_result(name, course, score, grade):
    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Course:", course)
    print("Score:", score)
    print("Grade:", grade)


# Main function
def main():
    # Get inputs
    name = get_name()
    course = get_course()
    score = get_score()
    
    # Process grade
    grade = calculate_grade(score)
    
    # Display result
    display_result(name, course, score, grade)


# Run program
if __name__ == "__main__":
    main()
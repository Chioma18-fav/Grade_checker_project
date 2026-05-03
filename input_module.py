# input_module.py

# Function to get student's name
def get_name():
    name = input("Enter your name: ")
    return name


# Function to get course name
def get_course():
    course = input("Enter your course: ")
    return course


# Function to get valid score
def get_score():
    while True:
        try:
            score = int(input("Enter your score (0 - 100): "))
            
            if score < 0 or score > 100:
                print("Invalid input! Score must be between 0 and 100.")
            else:
                return score
                
        except ValueError:
            print("Invalid input! Please enter a number.")
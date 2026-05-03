# main.py

from input_module import get_name, get_course, get_score
from logic_module import calculate_grade
from output_module import display_result


def main():
    # Get inputs
    name = get_name()
    course = get_course()
    score = get_score()
    
    # Process grade
    grade = calculate_grade(score)
    
    # Display result
    display_result(name, course, score, grade)


if __name__ == "__main__":
    main()
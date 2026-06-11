# ============================================================
# UPY - Programming
# Student: Lonardo Ulises Sonda Tec
# Q2 - 2026
# Description: Basic Python program - Functions & User Input
# ============================================================

def greet_user(name):
    """Returns a personalized greeting."""
    return f"Hello, {name}! Welcome to UPY Programming."

def calculate_average(grades):
    """Calculates the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def classify_grade(average):
    """Classifies the grade based on the average score."""
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    elif average >= 70:
        return "Satisfactory"
    elif average >= 60:
        return "Passing"
    else:
        return "Failing"

def main():
    print("=" * 40)
    print("   UPY Grade Calculator")
    print("=" * 40)

    name = input("Enter your name: ")
    print(greet_user(name))

    print("\nEnter your grades (type 'done' when finished):")
    grades = []
    while True:
        entry = input("  Grade: ")
        if entry.lower() == "done":
            break
        try:
            grade = float(entry)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("  Please enter a grade between 0 and 100.")
        except ValueError:
            print("  Invalid input. Please enter a number.")

    if grades:
        avg = calculate_average(grades)
        classification = classify_grade(avg)
        print(f"\nResults for {name}:")
        print(f"  Grades entered : {grades}")
        print(f"  Average        : {avg:.2f}")
        print(f"  Classification : {classification}")
    else:
        print("\nNo grades entered.")

    print("=" * 40)

if __name__ == "__main__":
    main()
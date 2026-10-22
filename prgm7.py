def get_grade(mark):
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def read_mark(name):
    while True:
        try:
            mark = float(input(f"Enter marks for {name} (0-100): "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if 0 <= mark <= 100:
            return mark

        print("Marks must be between 0 and 100.")


def main():
    students = []

    for student_number in range(1, 6):
        name = input(f"Enter the name of student {student_number}: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input(f"Enter the name of student {student_number}: ").strip()
        mark = read_mark(name)
        students.append((name, mark, get_grade(mark)))

    print("\nGrade boundaries: A: 90-100, B: 80-89.9, C: 70-79.9, D: 60-69.9, F: below 60")
    print(f"{'Name':<20}{'Marks':>10}  {'Grade':>5}")
    print("-" * 37)
    for name, mark, grade in students:
        print(f"{name:<20}{mark:>10.1f}  {grade:>5}")


if __name__ == "__main__":
    main()
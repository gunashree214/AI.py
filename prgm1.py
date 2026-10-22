def get_grade(mark):
	"""Return a letter grade using the defined minimum mark boundaries."""
	# Check from the highest boundary downward so each mark gets one grade.
	if mark >= 90:
		return "A"
	if mark >= 80:
		return "B"
	if mark >= 70:
		return "C"
	if mark >= 60:
		return "D"
	return "F"


def test_grade_boundaries():
	"""Check marks at and just below every grade boundary."""
	test_cases = [
		(100, "A"), (90, "A"), (89.9, "B"),
		(80, "B"), (79.9, "C"), (70, "C"),
		(69.9, "D"), (60, "D"), (59.9, "F"), (0, "F"),
	]

	for mark, expected_grade in test_cases:
		assert get_grade(mark) == expected_grade


def read_mark(name):
	"""Keep asking until the student has a numeric mark from 0 to 100."""
	while True:
		try:
			# float() accepts both whole-number marks and decimal marks.
			mark = float(input(f"Enter marks for {name} (0-100): "))
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue

		# Marks at 0 and 100 are valid; anything outside is rejected.
		if 0 <= mark <= 100:
			return mark

		print("Invalid mark. Marks must be between 0 and 100.")


def main():
	students = []

	# Collect five student records.
	for student_number in range(1, 6):
		name = input(f"Enter the name of student {student_number}: ").strip()
		while not name:
			print("Name cannot be empty.")
			name = input(f"Enter the name of student {student_number}: ").strip()

		mark = read_mark(name)
		students.append((name, mark, get_grade(mark)))

	# Display the grade scale and align each student's result in columns.
	print("\nGrade boundaries: A: 90-100, B: 80-89.9, C: 70-79.9, D: 60-69.9, F: below 60")
	print(f"{'Name':<20}{'Marks':>10}  {'Grade':>5}")
	print("-" * 37)
	for name, mark, grade in students:
		print(f"{name:<20}{mark:>10.1f}  {grade:>5}")


if __name__ == "__main__":
	main()

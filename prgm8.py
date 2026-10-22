def calculate_average(marks):
    """Return the arithmetic mean of a list of marks from 0 to 100."""
    if not isinstance(marks, list):
        raise TypeError("marks must be provided as a list")

    if not marks:
        raise ValueError("marks cannot be empty")

    for mark in marks:
        # Booleans are integers in Python, but are not valid marks here.
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise TypeError("each mark must be an integer or a float")

        if not 0 <= mark <= 100:
            raise ValueError("each mark must be between 0 and 100")

    # sum() and len() read the list without changing it.
    return sum(marks) / len(marks)


def _assert_raises(expected_exception, marks):
    try:
        calculate_average(marks)
    except expected_exception:
        return

    raise AssertionError(
        f"Expected {expected_exception.__name__} for {marks!r}"
    )


def test_calculate_average():
    """Test normal, boundary, invalid, and list-preservation behavior."""
    assert calculate_average([70, 80, 90]) == 80

    boundary_marks = [0, 100]
    original_marks = boundary_marks.copy()

    assert calculate_average(boundary_marks) == 50
    assert boundary_marks == original_marks
    assert calculate_average([0]) == 0
    assert calculate_average([100]) == 100

    _assert_raises(ValueError, [])
    _assert_raises(ValueError, [-1])
    _assert_raises(ValueError, [101])
    _assert_raises(TypeError, ["80"])
    _assert_raises(TypeError, (80, 90))


def main():
    """Read comma-separated marks and display their average."""
    raw_marks = input("Enter marks separated by commas (0-100): ").strip()

    try:
        if raw_marks:
            marks = [float(value.strip()) for value in raw_marks.split(",")]
        else:
            marks = []
    except ValueError:
        print("Invalid input: enter numbers separated by commas.")
        return

    try:
        average = calculate_average(marks)
    except (TypeError, ValueError) as error:
        print(f"Invalid marks: {error}")
        return

    print(f"Average mark: {average:.2f}")


if __name__ == "__main__":
    main()
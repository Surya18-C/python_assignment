#Finding the total average
def avg():
    students = [
        {"ID": 1, "Name": "Alice", "Class": 10, "Marks": 85},
        {"ID": 2, "Name": "Bob", "Class": 10, "Marks": 78},
        {"ID": 3, "Name": "Charlie", "Class": 10, "Marks": 92},
        {"ID": 4, "Name": "David", "Class": 10, "Marks": 88},
    ]

    total_mark = 0
    number_students = 0

    for student in students:
        total_mark += student["Marks"]
        number_students += 1

    avg = total_mark / number_students

    return avg


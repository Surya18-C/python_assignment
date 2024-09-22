
def average():
    student = {
        "babu": [20, 30, 40],
        "Anu": [50, 30, 40],
        "rex": [45, 35, 30]
    }

    student_name=input("Enter Student Name : ")
    mark=student[student_name]

    total=0
    for i in mark:
        total+=i

    avg = total/len(student)

    return avg



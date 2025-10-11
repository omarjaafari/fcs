def sum_scores_recursive(scores):
    if len(scores) == 0:
        return 0
    else:
        return scores[0] + sum_scores_recursive(scores[1:])

def get_students():
    students = []
    students_number = int(input("Enter number of students: "))
    for i in range(1, students_number + 1):
        name = input("Enter student " + str(i) + " name: ")
        score = int(input("Enter " + name + "'s score: "))
        students += [(name, score)]
    return students

def print_students(students):
    print("--------------------------------")
    print("All students and scores:")
    for i in range(len(students)):
        print(students[i][0], "-", students[i][1])

def calculate_average(students):
    scores = []
    for i in range(len(students)):
        scores = scores + [students[i][1]]
    total = sum_scores_recursive(scores)
    average = total / len(students)
    return average

def get_top_student(students):
    top_name = students[0][0]
    top_score = students[0][1]
    for i in range(1, len(students)):
        if students[i][1] > top_score:
            top_name = students[i][0]
            top_score = students[i][1]
    return top_name, top_score

def get_failed_students(students):
    failed = []
    for i in range(len(students)):
        if students[i][1] < 60:
            failed += [students[i][0]]
    return failed

def print_failed_students(failed):
    if len(failed) > 0:
        print("Failed students:")
        for i in range(len(failed)):
            if i == len(failed) - 1:
                print(failed[i])
            else:
                print(failed[i])

students = get_students()
print_students(students)

average = calculate_average(students)
print("Average score:", (average))

top_name, top_score = get_top_student(students)
print(f"Top student: {top_name} ({top_score})")

failed_students = get_failed_students(students)
print_failed_students(failed_students)

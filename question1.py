# Question 5

num = int(input("Enter number of integers: "))

even_sum = 0
odd_sum = 0

for i in range(num):
    value = int(input(f"Enter integer {i+1}: "))
    if value % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

# Question 6

def is_perfect(number):
    if number < 1:
        return False

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum == number

num = int(input("Enter a number to check if it's perfect: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    
    
# Question 7

def calculateWeightedScore(assignment, midterm, final):
    weighted_score = (assignment * 0.3) + (midterm * 0.3) + (final * 0.4)
    return weighted_score

def getGradeAndGPA(score):
    if score >= 90:
        return 'A', 4.0
    elif score >= 80:
        return 'B', 3.0
    elif score >= 70:
        return 'C', 2.0
    elif score >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def displayStudentRecord(student_id, name, assignment, midterm, final):
    weighted = calculateWeightedScore(assignment, midterm, final)
    grade, gpa = getGradeAndGPA(weighted)
    print("\n--- Student Record ---")
    print(f"ID: {student_id}")
    print(f"Name: {name}")
    print(f"Assignment Score: {assignment}")
    print(f"Midterm Score: {midterm}")
    print(f"Final Exam Score: {final}")
    print(f"Weighted Score: {weighted:.2f}")
    print(f"Grade Letter: {grade}")
    print(f"GPA: {gpa:.1f}")

student_id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
assignment_score = float(input("Enter Assignment Score: "))
midterm_score = float(input("Enter Midterm Score: "))
final_score = float(input("Enter Final Exam Score: "))

displayStudentRecord(student_id, name, assignment_score, midterm_score, final_score)

#Question 8

def stuResults(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    name, mark_str = line.strip().split(',')
                    mark = int(mark_str)

                    if mark >= 50:
                        res = "Passed"
                    else:
                        res = "Failed"

                    print(f"{name} - {res} ({mark})")

                except ValueError:
                    print(f"Data conversion error in line: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

stuResults("students.txt")

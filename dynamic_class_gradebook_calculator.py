#dynamic Grade-book:
#Takes in number of students and number of tests
#can input each test score for each student
#individual average and class average is calculated

while True:
    student_count = int(input("How many students are in your class? "))
    if student_count < 0:
        print("Invalid # of students, try again.")
    else:
        break

while True:
    test_count = int(input("How many tests in this class? "))
    if test_count < 0:
        print("Invalid # of tests, try again.")
    else:
        break

print("Here we go!")
test_sum = 0
test_number = 1
student_sum = 0
total_average = 0
student_average = 0
s = 0
for s in range(student_count):
    s +=1
    i = 0
    print("**** Student #" +str(s)+"****")
    test_number = 1

    for i in range(test_count):
        while True:
            test_score = int(input("Enter score for test " + str(test_number) + ": "))
            if test_score < 0:
                print("Invalid score, try again")
            else:
                break
        student_sum += test_score
        test_sum += test_score
        test_number +=1
        student_average = student_sum/test_count
        total_average += student_average
    print("Average student score for student #",s,"is", format(student_average, '.2f'))
    i += 1
    s +=1
    student_sum = 0
print()
answer = test_sum/test_count/student_count
print("Average score for all students is: ",format(answer, '.2f'))

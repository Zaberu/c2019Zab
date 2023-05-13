from students import Student
#1 single student
'''
student = Student("Daniil", 14, "C2019")
print(f"Name: {student.name} \n"
      f"Age: {student.age} \n"
      f"Group: {student.group} \n")
print("Call method ShowInfo")
student.ShowInfo()
'''
#2 list of students
dimaS = Student("Dima", 14, "C2019")
antonS = Student("Anton", 10, "C2019")
dariiS = Student("Darii", 11, "C2019")
tarasS = Student("Taras", 14, "C2019")
tymurS = Student("Tymur", 13, "C2019")
students = list()
students.append(dimaS)
students.append(antonS)
students.append(dariiS)
students.append(tarasS)
students.append(tymurS)
for student in students:
    student.ShowInfo()
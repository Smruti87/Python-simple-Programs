n=int(input("Enter the number of students"))
student={}
for i in range(n):
    name=input("Enter the name")
    marks=float(input("Enter the marks"))
    student[name]=marks

print(student)

maxstudent=max(student,key=student.get)

print("Students with Highst Marks ",student[maxstudent])
x=0.0
print(f'Topper name is',{maxstudent})
for values in student.values():
    x=float(values)+x
avg=x/len(student)
print("Avarage marks are:" ,avg)

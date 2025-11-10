l=[4, 16, 36, 64, 100]
double=list(map(lambda x:x*x,l))
print(double)
students = [("Asha", 85), ("Ravi", 92), ("Meena", 78), ("Kiran", 88)]
sorted_list=sorted(students,key=lambda x:x[1],reverse=True)
print(sorted_list)
marks = {"Asha": 85, "Ravi": 92, "Meena": 78, "Kiran": 88}
maximum=max(marks,key=lambda x:marks[x])
print(f'Maximum marks from the list is', maximum,'marks are',marks[maximum])
numbers=[3, 7, 10, 15, 20]
tri=list(map(lambda x:x*3,numbers))
print(tri)
greater=list(filter(lambda x:x>30,tri))
print(greater)
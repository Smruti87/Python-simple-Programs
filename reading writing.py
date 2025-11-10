file=open("text.txt","w")

word = " Name\t Marks"


file.write(word)
print("Enter the number the number of students:  ")
n=int(input())
for i in range(n):
    file.write("\n")
    name=input("Enter the Name: ")
    file.write(name)
    file.write("\t")
    marks= (input("Enter the marks"))

    file.write(marks)
file.close()
file=open("text.txt","r")
for data in file:
    print(data)

file.close()
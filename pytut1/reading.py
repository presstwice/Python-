employee_file = open("employee.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

#r = read, w = write, a = append, r+ = read/write
#print(employee.file.readable()) tells you if the file is readable
#print(employee_file.readlines()) puts everything in the file into a list
#you can then search for the index in the list like this print(employee_file.readlines()[1])
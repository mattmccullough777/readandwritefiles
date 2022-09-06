def main():
    import csv

    infile = open("EmployeePay.csv","r")

    csvfile = csv.reader(infile,delimiter=",")

    next(csvfile) #this skips the first line

    for record in csvfile:
        print("Employee ID:", record[0])
        print("First Name:", record[1])
        print("Last Name:", record[2])
        print("Salary",record[3])
        print("Bonus:",record[4])

        input() #this shows each employee individually when you click

main()
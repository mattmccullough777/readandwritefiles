def main():
    import csv

    infile = open("customers.csv","r")

    csvfile = csv.reader(infile, delimiter=",")

    next(csvfile) #this skips the first line

    outfile = open("customer_country.csv","w")

    for record in csvfile:
        outfile.write("Full name: " + record[1] + " "+record[2] + "\n")
        outfile.write("Country: " + record[3] + "\n")

    infile.close()
    outfile.close()


main()
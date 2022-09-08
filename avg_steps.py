def main():
    import csv

    infile = open("steps.csv","r")

    csvfile = csv.reader(infile, delimiter=",")

    next(csvfile)

    outfile = open("avg_steps.csv","w")

    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    sum_steps = 0

    days = 0

    counter = 1

    x=0

    for record in csvfile:
        if record[0] == str(counter):
            sum_steps += float(record[1])
            days+=1
            average = sum_steps/days
            average = round(average,2)
            

        else: 
            counter+=1
            outfile.write(months[x]+ " Average Steps: ")
            outfile.write(str(average)+"\n")
            x+=1
       
    

    infile.close()
    outfile.close()
        

        

main()
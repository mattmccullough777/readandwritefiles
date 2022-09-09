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

    x=-1
    
    first_variable = 0

    for record in csvfile:

        if record[0] == str(counter):
            sum_steps += float(record[1])  
            days+=1
                

        else: 
            average = 0
            sum_steps += first_variable #this adds the first row of the new month
            days+=1 #this adds 1 day 
            average = sum_steps/days
            average = round(average,2)
            x+=1
            outfile.write(months[x]+ " Average Steps: "+str(average)+"\n")
            days = 0
            first_variable = float(record[1])
            sum_steps = 0 #this skips the first row of the new month
            counter+=1

    sum_steps = 0
    days = 0

    if record[0] == "12":
        sum_steps += float(record[1])  
        days+=1


    average = sum_steps/days
    average = round(average,2)
    
    outfile.write("December Average Steps: "+str(average))
        



            

    infile.close()
    outfile.close()
        

        

main()
def main():
    infile = open("clients.txt","r")

    i = 0

    for line in infile:
        i = i+1
        print (str(i)+".",line.rstrip("\n"))

    infile.close()

main()

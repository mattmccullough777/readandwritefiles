def main():
    infile = open("philosophers.txt","r")

    line1 = infile.readline().rstrip("\n")
    line2 = infile.readline().rstrip("\n")
    line3 = infile.readline().rstrip("\n")

    print(line1)
    print(line2)
    print(line3)

    infile.close()


main()


# def test():
#     infile = open("philosophers.txt","r")

#     lines = infile.read()

#     print(lines)



# test()
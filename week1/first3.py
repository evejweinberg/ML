def encode(string):
    # print string
    # print ( len( string ) )
    newstring = list(string)
    # print newstring
    x = newstring[0]
    y = newstring[1]
    index = 0
    sameCt = 1

    for z in range (len(newstring)-1) :
        x = newstring[z]
        y = newstring[z+1]

        if (x == y):
            sameCt = sameCt + 1


        if (x != y):

            print sameCt
            print x
            sameCt = 1




if __name__ == "__main__":
    encode("MMMMMXGGHHHWWIGIFFFFFFFFMM")

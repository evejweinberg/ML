def encode(string):
    # print string
    # print ( len( string ) )

    x = string[0]
    y = string[1]
    index = 0
    while index < (len( string )):
        same = 1
        while (x == y):
            valToPrint = x
            # print 'they are same'
            same = same + 1

            # if index < len(string):
            #     x = string[index+1]
            #     y = string[index+2]
            #     index = index+1


        print same
        print valToPrint





        if (x != y):
            same = 1
            valToPrint = y
            # if index< len( string ):
            #     x = string[index+1]
            #     y = string[index+2]
            #     index = index+1




if __name__ == "__main__":
    encode("MMMMMXGGHHHWWIGIFFFFFFFFMM")

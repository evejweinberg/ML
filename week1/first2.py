

def encode(string):
    sameCount = 1
    index = 0
    for n in range (0, len(string)):
        if string[index] == string[index+1]:
            sameCount = sameCount +1
            index = index +1
            print "same"
        else:
            sameCount = 1
            print "diff"
            index = index +1






if __name__ == "__main__":
    encode("MMMMMXGGHHHWWIGIFFFFFFFFMM")

#yield - next time you come into the for loop, it starts after the yield

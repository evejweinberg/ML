def encode(string):

    result = []

    prevLetter = ''
    firsttimethough = True


    sameCt = 1

    for char in string :


        if (char == prevLetter):
            sameCt = sameCt + 1



        if (char != prevLetter):

            if firsttimethough == False:
                # print len(str(sameCt)
                # if len(str(sameCt)) > 1:
                #     print 'greater'
                #     ''.join(str(sameCt))
                result += str(sameCt)
                result += prevLetter
                # print result
                sameCt = 1


            firsttimethough = False



        prevLetter = char
        # print result
    result += str(sameCt)
    print result
    result += prevLetter

    # print result
    # return ''.join(result)
    return result
    # print prevLetter

if __name__ == "__main__":
    print encode("EEEEEEvvvvvEEEEEEEEEEEEEEEEEEEEEEE")
    # print (encode)

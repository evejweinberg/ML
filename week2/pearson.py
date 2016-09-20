import numpy as np
from math import sqrt
import reclist

##gives you a scale from -1 to 1

def pearson(prefs,p1,p2):
    si = {}
    for item in prefs[p1]:
        #if same item exists in the other person
        if item in prefs[p2]:
            #make a new list of just the overlapping values, set them all to 1
            si[item]=1
    n = len(si)


    if n==0: return 0
    #get the sums of all the ratings
    #get the value for each key/value pair that they had overlap in, add them up
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    # print sum1, sum2

    #square each answer and add them up
    sum1Sq=sum([pow(prefs[p1][it],2)for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2)for it in si])

    #(a*b)+(a*b)+(a*b)
    pSum=sum([prefs[p1][it]*prefs[p2][it]for it in si])


    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))

    if den ==0: return 0
    r=num/den

    return r

print pearson(reclist.critics, "Debbie Downer", "Debbie Upper")




#then run this to test one person against everyone else
def topMatches(prefs,person,n=5):
    scores=[(pearson(prefs,person,other),other) for other in prefs if other !=person]

    scores.sort()
    scores.reverse()
    return scores [0:n]

print (topMatches(reclist.critics,'Eve Weinberg',n=3))

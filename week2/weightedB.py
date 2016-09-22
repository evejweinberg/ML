import numpy as np
from math import sqrt
import reclist
from pprint import pprint

# import pearson

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

# print pearson(reclist.critics, "Debbie Downer", "Debbie Upper")




#then run this to test one person against everyone else
def topMatches(prefs,person,n=5):
    scores=[(pearson(prefs,person,other),other) for other in prefs if other !=person]

    scores.sort()
    scores.reverse()
    return scores [0:n]

def getRecs(prefs, person, similarity=pearson):
    totals={}
    simSums = {}
    for other in prefs:
        print other
        if other==person:
            continue
        sim=similarity(prefs,person,other)
        print '\t', sim
        if sim<=0: continue

        for item in prefs[other]:
            print '\t\t', item
            #if it's not our person, or if it's not but it's empty
            if item not in prefs[person] or prefs[person][item]==0:
                print '\t\t\t', item
                #similarity times score
                # totals.setdefault(item,0)
                if item not in totals:
                    totals[item] = 0
                totals[item]+=prefs[other][item]*sim
                pprint(totals)
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings =[( total/ simSums[ item], item) for item, total in totals.items( )]
    #
    rankings.sort()
    rankings.reverse()
    return rankings

results = getRecs(reclist.critics, "Eve Weinberg")
print results
# print (getRecs(reclist.critics, "Eve Weinberg"))

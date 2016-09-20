import numpy as np
from math import sqrt
import reclist
import pearson


def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        #if item exists in the other person
        if item in prefs[person2]:
            si[item]=1
    if len(si) == 0: return 0

    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
            for item in si])
    return 1/(1+sqrt(sum_of_squares))

print sim_distance(reclist.critics, "Gene Seymore", "Eve Weinberg")


# def topMatches(prefs,person,n=5,similarity=sim_pearson):
#     scores=[(similarity(prefs,person,other),other) for other in prefs if other !=person]
#
#     scores.sort()
#     scores.reverse()
#     return scores [0:n]
#
# print (topMatches(reclist.critics,'Eve Weinberg',n=3))

import numpy as np
from math import sqrt
import reclist
import pearson

def getRecs(prefs, person, similarity=sim_pearson):
    totals={}
    simSums = {}
    for other in prefs:
        if other==person:
            continue
        sim=similarity(prefs,person,other)

        if sim<=0: continue

    for item in prefs[other]:
        #if it's not our person, or if it's not but it's empty
        if item not in prefs[person] or prefs[person][item]==0:
            #similarity times score
            totals.setdefault(item,0)totals[item]+=prefs[other][item]*sim
            print totals
            simSums.setdefault(item,0)
            simSums[item]+=sim
            rankings=[total/simSums[item],item] for item,total in totals.item()]

            rankings.sort()
            rankings.reverse()
            return rankings

getRecs(reclist.critics, "Eve Weinberg")
print (getRecs(reclist.critics, "Eve Weinberg"))

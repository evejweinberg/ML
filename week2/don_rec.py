import numpy as np
import math as mt



activity = ['hiking','reading','driving','watching movie']

user1 = []
user2 = []

for i in range (0,len(activity)):
    answer1= raw_input("Do USER1 like " + activity[i] + "? Rate from 1.0 to 5.0 " +"\n")

    user1.append(answer1)


for i in range (0,len(activity)):
    answer2= raw_input("Do USER2 like " + activity[i] + "? Rate from 1.0 to 5.0 " +"\n")

    user2.append(answer2)


user1=np.array(user1,dtype=float)
user2=np.array(user2,dtype=float)
euuser = user1 - user2

eucompare = mt.sqrt( np.dot(euuser,euuser) )


print 'Euclidean Similarity is ' , float(1/eucompare)


pdividend = (len(user1) * np.dot(user1, user2) - np.sum(user1) * np.sum(user2) )
pdevisor = (len(user1) * np.dot(user1, user1) - np.square(np.sum(user1)) ) * (len(user1) * np.dot(user2, user2) - np.square(np.sum(user2)) )

pcompare = pdividend / np.sqrt(pdevisor)

print 'Pearson Correaltion is ' , float(pcompare)

import matplotlib.pyplot as mp
import numpy as np
"""
#line graph
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20]
mp.title("New graph")
mp.xlabel("X")
mp.ylabel("Y = 2X")
mp.plot(x,y,marker = "o",color = "Black", linestyle = "--")
# : = dotted line
# - = solid line
# -- = dashed line
# color with first letter
# shape = O...
#plot the linegraph
mp.show()

#bar graph
x = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y = [3,4,2,4,1,3,3]
mp.title("Study hours per day")
mp.xlabel("Day")
mp.ylabel("Hours")
mp.bar(x,y)
mp.show()


#horizontal bar graph
x = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y = [3,4,2,4,1,3,3]
mp.title("Study hours per day")
mp.xlabel("Day")
mp.ylabel("Hours")
mp.barh(x,y)
mp.show()


#piechart
subjects = ["Economics","Math","German","English","PE"]
time = [1,2,1,1,2]
mp.title("Time per subject")
mp.pie(time,labels=subjects,autopct="%1.1f%%",colors=["Blue","Red","Yellow","Orange","Green"],startangle=0,shadow=True)
mp.show()

#scatterplot
x = [1,2,3,4,5,6,7,8,9,10]
y = [3,16,2,7,18,24,3,0,8,7]
mp.title("Scatterplot")
mp.scatter(x,y)
mp.show()

#stackplot
subjects = ["Economics","Math","German","English","PE"]
monday = [2,2,1,1,2]
tuesday = [1,0,2,3,0]
wednesday = [3,1,2,3,2]
thursday = [0,2,1,2,0]
friday = [0,1,2,1,0]
saturday = [1,1,1,1,0]
sunday = [2,4,3,1,0]

mp.stackplot(subjects,monday,tuesday,wednesday,thursday,friday,saturday,sunday,colors=["Red","Green","Blue","Pink","Green","Yellow","Purple"],labels=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
mp.xlabel("Subjects")
mp.ylabel("Hours")
mp.legend()
mp.show()


#histogram
list = []
age = np.random.randint(1,100,100)
intervals = [10,20,30,40,50,60,70,80,90,100]
mp.hist(age,intervals)
mp.show()
"""

#subplot
mp.figure()
mp.subplot(121)

x = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y = [3,4,2,4,1,3,3]
mp.title("Study hours per day")
mp.xlabel("Day")
mp.ylabel("Hours")
mp.bar(x,y)

mp.subplot(122)
list = []
age = np.random.randint(1,100,100)
intervals = [10,20,30,40,50,60,70,80,90,100]
mp.hist(age,intervals)
mp.show()


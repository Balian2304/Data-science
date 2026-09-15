import matplotlib.pyplot as mp
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
"""
#scatterplot
x = [1,2,3,4,5,6,7,8,9,10]
y = [3,16,2,7,18,24,3,0,8,7]
mp.title("Scatterplot")
mp.scatter(x,y)
mp.show()


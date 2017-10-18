import sqlite3


f="discobandit.db"

db = sqlite3.connect(f)
c = db.cursor() 

#list used for everything
id =[]
names =[]
average = []



#---- HELPER FUNCS ----------------------------------

#getting the scores for the IDs
def getScores(id):
	numbClass=0
	total=0
	command = "SELECT mark FROM courses WHERE id ="+str(id)+";"
	#print command
	c.execute(command)
	tempScores = c.fetchall()
	for each in tempScores:
		numbClass+=1
		total+=each[0]
	return avg (numbClass, total)

#avg func
def avg(numbClass, total):
	return (total/numbClass)

def getName(id):
	command = "SELECT name FROM peeps WHERE id ="+str(id)+";"
	c.execute(command)
	return c.fetchone()[0]


#main bit
def makeLists():
	#fetches the number of students and therefore their IDs
	command="SELECT * FROM peeps;"
	c.execute(command)
	length = len(c.fetchall())

	#builds all the lists + prints
	i = 1 
	while (i<=length):
		id.append(i)
		average.append(getScores(i))
		names.append(getName(i))
		print "ID= "+str(i-1)+" Name= "+names[i-1]+" Avg= "+str(average[i-1])
		i+=1

def buildTable():
	#creates actual table
	try:
		command = "CREATE TABLE peeps_avg (id integer, names text, average numeric);" 
		c.execute(command)
		insertVal();

	except:
		print "Table exists; Values updated"
		updateAvg();

#inserts
def insertVal():
	i=0
	while (i<len(average)):
		command="INSERT INTO peeps_avg VALUES ("+str(id[i-1])+",'"+names[i-1]+"',"+str(average[i-1])+");"
		c.execute(command)
		#print command
		i+=1

def updateAvg():
	i=0
	while (i<len(average)):
		command = "UPDATE peeps_avg SET average ="+ str(average[i-1]) + " WHERE id ="+ str(id[i-1]) +";"
		c.execute(command)
		i+=1

#---------------------------------------------------------



makeLists()
buildTable()		




#==========================================================
db.commit() #save changes
db.close()  #close database







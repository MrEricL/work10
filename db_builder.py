import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

peeps = csv.DictReader(open("peeps.csv"))

courses = csv.DictReader(open("courses.csv"))


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops



#==========================================================

def insertP():
	for key in peeps:

		command="INSERT INTO peeps VALUES ("
		for inner in key:
			command+=("'"+key[inner]+"'")
			command+=','
		command = command[:-1] #goodbye last comma 
		command+=');'
		c.execute(command)


def insertC():
	for key in courses:

		command="INSERT INTO courses VALUES ("
		for inner in key:
			command+=("'"+key[inner]+"'")
			command+=','
		command = command[:-1] #goodbye last comma 
		command+=');'
		c.execute(command)

#checks if the tables exist
try:
	command = "CREATE TABLE peeps (age integer, name text, id integer);"        	
	c.execute(command)    #run SQL statement
	print "Peep table made!"

except:
	print "Peep table exists; Updating values"
	command = "DROP TABLE peeps;"
	c.execute(command)

	command = "CREATE TABLE peeps (age integer, name text, id integer);"       
	c.execute(command)  

try:
	command = "CREATE TABLE courses (code text, id integer, mark integer);"          #put SQL statement in this string
	c.execute(command)    #run SQL statement
	print "Course table made!"

except:
	print "Courses table exists; Updating values"
	command = "DROP TABLE courses;"
	c.execute(command)

	command = "CREATE TABLE courses (code text, id integer, mark integer);" 
	c.execute(command)

insertP()
insertC()

#loops through and inserts




#==========================================================
db.commit() #save changes
db.close()  #close database



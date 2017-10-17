import sqlite3


f="discobandit.db"

db = sqlite3.connect(f)
c = db.cursor() 

dict={}
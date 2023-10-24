import sqlite3 

# connect to a database 
# implicitly creates database since it doesn't exist 
conn = sqlite3.connect("userAccounts.db")

# close connection 
conn.close() 



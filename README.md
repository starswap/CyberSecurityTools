# CyberSecurityTools
Some Cyber Security tools I have coded. Use ethically!


Blind SQLi Tools:
- You may need to look for tables that are not in the current database - remove the TABLE_SCHEMA where clauses and put the required A.tableName instead of just tableName when leaking data. You will first need to find the db name for the table. This is the TABLE_SCHEMA value in the INFORMATION_SCHEMA.COLUMNS table

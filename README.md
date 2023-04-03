# Personal Finance Database 

Learning about python path development & init
Creating a personal financial management database in the process 

Good python path tutorial: 
https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355


TODO: 
- [] add below code to home directory? Note, utils hardcoded may be an issue
- [] add string split on SQL semi colon & iteration

`export PYTHONPATH=$PYTHONPATH:$(pwd)/utils`


# Read the contents of the .sql file
with open('example.sql', 'r') as sql_file:
    sql_content = sql_file.read()

# Split the SQL statements into a list
sql_statements = sql_content.split(';')

# Execute the SQL statements
with connection.cursor() as cursor:
    for statement in sql_statements:
        # Strip any leading/trailing whitespaces and check if the statement is not empty
        if statement.strip():
            cursor.execute(statement)
            connection.commit()

# Close the connection when done
connection.close()

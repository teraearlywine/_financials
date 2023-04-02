import parse_config as pc 
import utils

# sql = "%s"
# sql = "SELECT 1"

connection = pc.pymysql.connect(
    host = pc.db_host,
    port = pc.db_port,
    user = pc.db_username,
    password = pc.db_password
)

# Execute a given SQL string & print in console
# todo: fix tuple formatting, output as pretty table

def execute_sql(sql_string):
    m_cursor = connection.cursor() 
    m_cursor.execute(sql_string)
    results = m_cursor.fetchall() 
    print(results)

# Commit a given SQL string to the local database
def commit_sql(sql_string):
    m_cursor = connection.cursor() 
    m_cursor.execute(sql_string)
    connection.commit()

# with open('example.sql', 'r') as sql_file:
#     sql_content = sql_file.read()

# # Split the SQL statements into a list
# sql_statements = sql_content.split(';')

# # Execute the SQL statements
# with connection.cursor() as cursor:
#     for statement in sql_statements:
#         # Strip any leading/trailing whitespaces and check if the statement is not empty
#         if statement.strip():
#             cursor.execute(statement)
#             connection.commit()


# def executeScriptsFromFile(filename):
#     # Open and read the file as a single buffer
#     fd = open(filename, 'r')
#     sqlFile = fd.read()
#     fd.close()

#     # all SQL commands (split on ';')
#     sqlCommands = sqlFile.split(';')

#     # Execute every command from the input file
#     for command in sqlCommands:
#         # This will skip and report errors
#         # For example, if the tables do not yet exist, this will skip over
#         # the DROP TABLE commands
#         try:
#             c.execute(command)
#         except OperationalError, msg:
#             print("Command skipped: ", msg)

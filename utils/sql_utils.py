import parse_config as pc 

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
    results = [results[0] for results in m_cursor.fetchall()]
    # results = m_cursor.fetchall() 

    print(results)

# Commit a given SQL string to the local database
def commit_sql(sql_string):
    m_cursor = connection.cursor() 
    m_cursor.execute(sql_string)
    connection.commit()

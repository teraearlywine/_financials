import sql_utils
import sql 

def output_data(filepath):
    # Read sql file, add to sql_content variable
    with open(filepath, 'r') as sql_file:
        sql_content = sql_file.read()
    # Using sql utils, execute sql_content variable
    sql_utils.execute_sql(sql_content)

# read_sql_filename('sql/sample.sql')
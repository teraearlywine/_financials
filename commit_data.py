import sql_utils
import sql 

## Commit data to connected database
def commit_data(filepath):
    # Read sql file, add to sql_content variable
    with open(filepath, 'r') as sql_file:
        sql_content = sql_file.read()
    # Using sql utils, execute sql_content variable
    sql_utils.commit_sql(sql_content)

# commit_data('sql/create_table.sql')

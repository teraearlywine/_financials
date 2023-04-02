#!/usr/bin/env python 
import sql_utils
import sys

def output_data(filepath):
    # Read sql file, add to sql_content variable
    with open(filepath, 'r') as sql_file:
        sql_content = sql_file.read()
    # Using sql utils, execute sql_content variable
    sql_utils.execute_sql(sql_content)

# in the CLI, add sql filepath to argument 1 
if __name__ == '__main__':
    output_data(sys.argv[1])

# Create some function that appends an argument to the sql file path maybe?
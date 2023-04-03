#!/usr/bin/env python 
import sql_utils
import sys

def execute_sql(filepath):
    # Read sql file, add to sql_content variable
    with open(filepath, 'r') as sql_file:
        sql_content = sql_file.read()
    # Using sql utils, execute sql_content variable
    sql_utils.execute_sql(sql_content)


# in the CLI, add sql filepath to argument 1 
if __name__ == '__main__':
    # todo: add to own subdirectory
    def cli_function():
        # Set file path to directory variables
        sql_directory = 'sql/'
        sql_file_name = sys.argv[1]
        file_suffix = '.sql'
        # Join Variables
        full_file_path = sql_directory + sql_file_name + file_suffix
        # Process sql
        execute_sql(file_string)

    cli_function()

# Create some function that appends an argument to the sql file path maybe?
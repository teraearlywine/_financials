#!/usr/bin/env python 

# Trying to make the  data output more readable in cli tool
import pandas as pd
import sys
import sql_utils

def format_data(filepath):

    with open(filepath, 'r') as sql_file:
        import_sql = sql_file.read()

    generate_output = sql_utils.execute_sql(import_sql)
    df = pd.DataFrame(generate_output)
    return df


if __name__ == '__main__':
    # format_data(sys.argv[1])
    # todo: add to own subdirectory
    def cli_function():
        # Set file path to directory variables
        sql_directory = 'sql/'
        sql_file_name = sys.argv[1]
        file_suffix = '.sql'
        # Join Variables
        full_file_path = sql_directory + sql_file_name + file_suffix
        # Process sql
        format_data(full_file_path)

    cli_function()


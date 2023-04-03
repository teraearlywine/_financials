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
    format_data(sys.argv[1])

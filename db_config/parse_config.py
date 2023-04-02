import yaml
import pymysql

# Read and parse the YAML config file
with open('db_config.yaml', 'r') as config_file:
    config_data = yaml.load(config_file, Loader=yaml.SafeLoader)

# Access data from the parsed YAML
app_name = config_data['app']['name']
app_version = config_data['app']['version']

db_host = config_data['mysql_config']['host']
db_port = config_data['mysql_config']['port']
db_username = config_data['mysql_config']['username']
db_password = config_data['mysql_config']['password']
db_database = config_data['mysql_config']['database']

connection = pymysql.connect(
    host = db_host,
    port = db_port,
    user = db_username,
    password = db_password
)


# connect to db info


# lo
# with open('example.sql', 'r') as sql_file:
#     sql_content = sql_file.read()

# # Print the contents of the .sql file
# print(sql_content)

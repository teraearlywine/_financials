import yaml
import pymysql

# Read and parse the YAML config file

with open('/Users/teraearlywine/Code/teraearlywine/_financials/utils/db_config.yaml', 'r') as config_file:
    config_data = yaml.safe_load(config_file)

db_host = config_data['mysql_config']['host']
db_port = config_data['mysql_config']['port']
db_username = config_data['mysql_config']['username']
db_password = config_data['mysql_config']['password']
db_database = config_data['mysql_config']['database']

# This file should only be used if configuration file doesn't work :(
from configparser import ConfigParser
config = ConfigParser()

config['settings'] = {
    'bot_type': 'woodcutting',
    'woodcutting_find_tree_attempts': '20',
    'chop_and_drop_time_seconds': '15',
    'drop_number_of_logs_per_cycle': '4',
}

with open('./dev.ini', 'w') as f:
    config.write(f)
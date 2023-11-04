import logging

log_file = 'cf4.log'

# Create a file handler to log a file
# Default mode 'a' which means 'append'

file_handler = logging.FileHandler(log_file, mode='a')

# create a list of handlers for the logger
handlers = [file_handler]

# name the logger
logger = logging.getLogger('search-app')

# config the root logger with the handlers
logging.basicConfig(
    handlers=handlers,
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

nums = [1, 2, 3, 4, 5]
num_to_find = 20

try:
    index = nums.index(num_to_find)
except ValueError as e:
    logger.error(f'{e}', exc_info=True)

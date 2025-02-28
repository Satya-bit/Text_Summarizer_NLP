# import os
# import sys
# import logging

# log_dir="logs"
# logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# log_filepath = os.path.join(log_dir,"continuos_logs.log")

# os.makedirs(log_dir,exist_ok=True)# If that directory already exists not going to create it again


# # Configuring the logging settings
# logging.basicConfig(
#     level=logging.INFO,  # Sets the logging level to INFO, meaning it will log INFO and higher-level messages
#     format=logging_str,  # Defines the log message format 
    
#     handlers=[
#         logging.FileHandler(log_filepath),  # Logs messages to a file specified by log_filepath
#         logging.StreamHandler(sys.stdout)  # Also prints log messages to the console (stdout)
#     ]
# )

# # Creating a logger instance named "summarizerlogger"
# logger = logging.getLogger("summarizerlogger")

import os
import sys
import logging

# Define the directory where logs will be stored
log_dir = os.path.join("/tmp", "logs")  # Change log directory to /tmp to avoid permission issues
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the log file path inside the log directory
log_filepath = os.path.join(log_dir, "continuos_logs.log")

# Create the log directory if it does not exist
os.makedirs(log_dir, exist_ok=True)  # If that directory already exists, it will not create it again

# Configuring the logging settings
logging.basicConfig(
    level=logging.INFO,  # Sets the logging level to INFO, meaning it will log INFO and higher-level messages
    format=logging_str,  # Defines the log message format 
    
    handlers=[
        logging.FileHandler(log_filepath),  # Logs messages to a file specified by log_filepath
        logging.StreamHandler(sys.stdout)  # Also prints log messages to the console (stdout)
    ]
)

# Creating a logger instance named "summarizerlogger"
logger = logging.getLogger("summarizerlogger")

###

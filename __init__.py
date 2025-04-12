import os
import sys 
import logging 

logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO, #logs info which is >= info ie info,warning,error, critical
    format=logging_str,
    handlers=[ #specifies where logs should go
        logging.FileHandler(log_filepath), #logs to file
        logging.StreamHandler(sys.stdout) #logs to console
    ]
)

logger=logging.getLogger("datascienceLogger")  #this var will be called elsewhere in imported form
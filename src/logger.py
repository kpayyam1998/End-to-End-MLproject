""""
    Logger which is nothing but whenever excuting our program it will track everything 
    Even custom excepton error also we can log

    If want to learn more gothrouth document

"""


import os
import logging

from datetime import datetime

LOGFILE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log" # Getting current date time with extension  .log filename
log_path=os.path.join(os.getcwd(),"logs",LOGFILE) # combine with path and file name
os.makedirs(log_path,exist_ok=True) # crating directory


LOGS_FILE_PATH=os.path.join(log_path,LOGFILE) # full path and file name

logging.basicConfig(
    filename=LOGS_FILE_PATH,

    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO # this line going to write my exitre msg

)

# if __name__=="__main__":
#     logging.info("Logging started...")
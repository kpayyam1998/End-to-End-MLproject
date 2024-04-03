import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

list_of_files=[
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/predict_pipeline.py",
    "src/pipeline/train_pipeline.py",
    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",
    "static/style.css",
    "templates/index.html",

]


for file_path in list_of_files:
    file_path=Path(file_path) # Converting file path
    file_dir,file_name=os.path.split(file_path) # spilit dir and fileanem

    if file_dir!="": #it contains some path 
        os.makedirs(file_dir,exist_ok=True) #It create new folder
        logging.info(f"Creating directory :{file_dir} for the file is{file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0): # dire and file not exists it will crete empty file
        with open(file_path,'w') as f:
            pass
            logging.info(f"Creating empty file:{file_path}")
    else:
        logging.info(f"{file_name} is already created")
    
    

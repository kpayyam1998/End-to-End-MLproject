""""
This is file is completely explain about data part like loading the data

"""
import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
#import hera below
from src.components.data_transformation import DataTransformation,DataTranformation_Config

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

# When we call this class below class those three path will be stored
# Ingestion variable

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() 

    #using this function to load data from various source
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion part (Method or component)")
        try:
            df=pd.read_csv("../../notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")
            
            # below line will create direcoty
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #write a raw data in that path
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test split started")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_tranformation=DataTransformation()
    data_tranformation.initiate_data_transformation(train_data,test_data)
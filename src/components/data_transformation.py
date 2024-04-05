"""
This file contains data filtering,data convertion (cat to num)

"""

import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer # this is help to create pipeline  like one hot encode,standard scalar
from sklearn.impute import SimpleImputer # This help to replace missing values
from sklearn.pipeline import Pipeline # this can use to perform multitask at the same time
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object




@dataclass
class DataTranformation_Config:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTranformation_Config()

    def get_data_transformer_object(self):
        try:
            """
                This function is responsible for data transformation based on the data
            """    

            numerical_columns=["reading_score",	"writing_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
            	"parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            # Created Pipeline  which is doing 2 tasks
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="mean")), #handling missing values
                    ("scalar",StandardScaler()) # Doing standard scalar of numerical data 
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()), # convert cat values to o to 1
                    ("scalar",StandardScaler(with_mean=False)) # Scaling
                ]
            )
            logging.info(f"Numeical standard scaling completed:{numerical_columns} ")
            logging.info(f"Categorical onehot encoding standard scaling completed:{categorical_columns} ")

            # which is combination numerical & categorical pipeline
            preprocessor=ColumnTransformer(
                [   #pipeline name,pipeline,column name
                    ("numerical",num_pipeline,numerical_columns),
                    ("categorcial",cat_pipeline,categorical_columns)
                ]
            )
            
            # Done Preprocessing

            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data is completed")

            logging.info("Obtaining preprocessing object")

            # calling preprocessor
            preprocessor_obj=self.get_data_transformer_object()

            # Target column
            target_col="math_score"

            # numerical_columns=["reading_score",	"writing_score"]

            input_feature_train_df=train_df.drop(columns=[target_col],axis=1)
            target_feature_train_df=train_df[target_col]
            
            input_feature_test_df=test_df.drop(columns=[target_col],axis=1)
            target_feature_test_df=test_df[target_col]


            logging.info(

                f"Applying preprocessing object on training and testing dataframe"
            )

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)



            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info("saving preprocessing object")

            # where we are going to write this function Utils
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )

            return(
                train_arr,test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
    

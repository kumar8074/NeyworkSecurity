from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
import sys

if __name__=="__main__":
    try:
        trainingpipelinelineconfig=TrainingPipelineConfig()
        
        dataingestionconfig=DataIngestionConfig(trainingpipelinelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        print(dataingestionartifact)
        
        data_validation_config=DataValidationConfig(trainingpipelinelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation complete")
        print(data_validation_artifact)
        
        data_transformation_config=DataTransformationConfig(trainingpipelinelineconfig)
        data_transformation=DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiate Data Transformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Complete")
        print(data_transformation_artifact)
         
    except Exception as e:
        raise NetworkSecurityException(e,sys)
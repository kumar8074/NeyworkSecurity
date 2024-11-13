from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
import sys

if __name__=="__main__":
    try:
        trainingpipelineline=TrainingPipelineConfig()
        datainfestionconfig=DataIngestionConfig(trainingpipelineline)
        data_ingestion=DataIngestion(datainfestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
         
    except Exception as e:
        raise NetworkSecurityException(e,sys)
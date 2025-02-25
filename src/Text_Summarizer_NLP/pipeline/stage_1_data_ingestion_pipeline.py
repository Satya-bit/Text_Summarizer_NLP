#Step-5

from src.Text_Summarizer_NLP.components.data_ingestion import DataIngestion
from src.Text_Summarizer_NLP.config.configuration import ConfigurationManager
from src.Text_Summarizer_NLP.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config=ConfigurationManager() #Initializing the config manager where the config and 
        #param files will be read  
        data_ingestion_config=config.get_data_ingestion_config() #It will be assigned to DataIngestionConfig where the values will be stored.
        data_ingestion=DataIngestion(config=data_ingestion_config) #Initializing the data ingestion and 
        #storing outputs in the paths assigned inside the DataIngestionConfig 

        data_ingestion.download_file() #Downloading the file
        data_ingestion.extract_zip_file() #Extracting the zip file



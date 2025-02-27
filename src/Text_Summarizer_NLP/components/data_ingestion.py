#Step-4
#######
import os
import urllib.request as request
import zipfile
from src.Text_Summarizer_NLP.logging import logger
from src.Text_Summarizer_NLP.entity import DataIngestionConfig

class DataIngestion: #Defining the functionalities of data ingestion
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            ) #This will return the filename as data dataset.zip and headers which 
            #contains content like the size/type of the file 
            logger.info(f"Filename downloaded")
        else:
            logger.info(f"File already exists of size")
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir  #Defining unzip path
        os.makedirs(unzip_path, exist_ok=True) #Creating unzip folder
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
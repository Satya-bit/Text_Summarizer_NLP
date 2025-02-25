#Step-3
from src.Text_Summarizer_NLP.constants import * #We will be requiring Config.yaml and params.yaml 
#before the execution of any model(ingestion,validation,training,etc)

from src.Text_Summarizer_NLP.utils.common import read_yaml, create_directories

from src.Text_Summarizer_NLP.entity import DataIngestionConfig,DataTransformationConfig



class ConfigurationManager: # There are some functionalities in every component like data ingestion, etc
    #For example extract the zip file and unzip it and store it in artifacts folder. So all functionalities are defined here
    # are written in configuration manager.
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH, 
        params_filepath = PARAMS_FILE_PATH): 

        self.config = read_yaml(config_filepath)#Reading config file
        self.params = read_yaml(params_filepath)#Reading params file

        create_directories([self.config.artifacts_root]) #Creating artifacts folder

    def get_data_ingestion_config(self) -> DataIngestionConfig: #Reading data ingestion fields and assigning to data_ingestion_config to data ingestion config where the values will be stored
        config = self.config.data_ingestion #Reading data ingestion from the config.yaml

        create_directories([config.root_dir]) #Creating data_ingestion folder

        data_ingestion_config = DataIngestionConfig( #Reading the values from config and assigning it to DataIngestionConfig
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    


    def get_data_transformation_config(self)-> DataTransformationConfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config



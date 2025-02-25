#Step-2
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig: #Dataclass for data ingestion. 
    #In order to create what all ouptuts will be there need to create some fields beacuse in 
    #that fields we will store the values
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path
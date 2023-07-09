from src.YOLO_V8.constants import *
from src.YOLO_V8.utils.common import read_yaml, create_directories
from src.YOLO_V8.entity.config_entity import DataIngestionConfig, DataProcessingConfig

# creating configuration class 
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_process_config(self) -> DataProcessingConfig:
        config = self.config.data_processing
        params = self.params

        data_processing_config = DataProcessingConfig(
            source_dir= config.source_dir,
            raw_data_dir= config.raw_data_dir,
            processed_data_dir= config.processed_data_dir,
            split_data_dir = config.split_data_dir,
            image_size= params.image_size,
            train_data_size= params.train_data_size,
            val_data_size= params.val_data_size
        )

        return data_processing_config
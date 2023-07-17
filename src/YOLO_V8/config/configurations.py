import os
from src.YOLO_V8.constants import *
from src.YOLO_V8.utils.common import read_yaml, create_directories
from src.YOLO_V8.entity.config_entity import ( DataIngestionConfig,
                                               DataProcessingConfig, 
                                               BaseModelConfig, 
                                               TrainModelConfig, 
                                               ModelEvaluateConfig )

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

        create_directories([config.raw_data_dir, config.processed_data_dir, config.split_data_dir])

        data_processing_config = DataProcessingConfig(
            source_dir= config.source_dir,
            raw_data_dir= config.raw_data_dir,
            processed_data_dir= config.processed_data_dir,
            split_data_dir = config.split_data_dir,
            image_size= params.IMAGE_SIZE,
            train_data_size= params.TRAIN_DATA_SIZE,
            val_data_size= params.VAL_DATA_SIZE
        )

        return data_processing_config
    
    def get_base_model_config(self) -> BaseModelConfig:
        config = self.config.base_model
        params = self.params.BASE_MODEL
    
        create_directories([config.base_model_dir])

        base_model_config = BaseModelConfig(
            base_model_dir = Path(config.base_model_dir),
            base_model_name = params.MODEL_NAME
        )

        return base_model_config
    
    def get_train_model_config(self) -> TrainModelConfig:

      base_model_path = os.path.join(self.config.base_model.base_model_dir,
                                     self.params.BASE_MODEL.MODEL_NAME)
      config = self.config.train_model
      params = self.params.TRAIN_MODEL_PARAMS

      create_directories([config.savel_model_dir])

      model_training_config = TrainModelConfig(
          base_model = Path(base_model_path),
          data_file = config.data_file_path,
          saved_model_dir = config.saved_model_dir,
          epochs = params.EPOCHS,
          batch_size= params.BATCH_SIZE,
          image_size = params.IMAGE_SIZE,
          optimizer = params.OPTIMIZER )

      return model_training_config
    
    def get_model_evaluate_config(self) -> ModelEvaluateConfig:
      config = self.config.model_evaluation
      params = self.params.MODEL_EVALUATE_PARAMS
      model_evaluate_config = ModelEvaluateConfig(
          best_model = config.best_model,
          data_file = config.data_file_path,
          batch_size= params.BATCH_SIZE,
          image_size = params.IMAGE_SIZE,
          confidence = params.CONFIDENCE
      )
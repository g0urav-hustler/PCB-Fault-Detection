from src.YOLO_V8.config.configurations import ConfigurationManager
from src.YOLO_V8.components.data_processing import DataProcessing
from src.YOLO_V8 import logger

STAGE_NAME = "Data Processing Stage"

class DataProcessingTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_processing_config = config.get_data_process_config()
        data_processing = DataProcessing(data_processing_config)
        
        logger.info("Gettinng Raw Dataset ---->")
        data_processing.get_raw_data()

        logger.info("Getting Processed Dataset ---->")
        data_processing.processed_data()

        logger.info("Getting Split Dataset ---->")
        data_processing.split_data()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataProcessingTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

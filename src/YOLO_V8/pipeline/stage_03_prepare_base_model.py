from src.YOLO_V8.config.configurations import ConfigurationManager
from src.YOLO_V8.components.prepare_base_model import BaseModel
from src.YOLO_V8 import logger

STAGE_NAME = "Preparing Base Model Stage" 

class BaseModelPreparePipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        prepare_base_model = BaseModel(base_model_config)
        prepare_base_model.download_base_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = BaseModelPreparePipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
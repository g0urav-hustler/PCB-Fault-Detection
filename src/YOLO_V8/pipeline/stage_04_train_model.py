from src.YOLO_V8.config.configurations import ConfigurationManager
from src.YOLO_V8.components.train_model import TrainModel
from src.YOLO_V8 import logger

STAGE_NAME = "Training Model "

class TrainModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        train_model_config = config.get_train_model_config()
        model_training = TrainModel(train_model_config)
        model_training.train_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
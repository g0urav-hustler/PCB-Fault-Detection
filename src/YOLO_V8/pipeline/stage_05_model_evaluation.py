from src.YOLO_V8 import logger
from src.YOLO_V8.components.model_evaluation import EvaluateModel
from src.YOLO_V8.config.configurations import ConfigurationManager

STAGE_NAME = "Model Evaluation"

def ModelEvaluationPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluate_config = config.get_model_evaluate_config()
        model_evaluation = EvaluateModel(model_evaluate_config)
        model_evaluation.evaluate_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
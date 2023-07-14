from src.YOLO_V8 import logger
from src.YOLO_V8.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.YOLO_V8.pipeline.stage_02_data_processing import DataProcessingTrainingPipeline
from src.YOLO_V8.pipeline.stage_03_prepare_base_model import BaseModelPrepareTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

###### Next Stage ######

STAGE_NAME = "Data Processing Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataProcessingTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

###### Next Stage ######

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = BaseModelPrepareTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


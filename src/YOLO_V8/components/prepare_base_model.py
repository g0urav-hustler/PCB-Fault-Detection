import os
import shutil
from ultralytics import YOLO
from src.YOLO_V8 import logger
from src.YOLO_V8.utils.common import get_size
from src.YOLO_V8.entity.config_entity import BaseModelConfig


class BaseModel:
    def __init__(self, config: BaseModelConfig):

        self.base_model_dir = config.base_model_dir
        self.base_model_name = config.base_model_name
        self.save_model_path = os.path.join(self.base_model_dir,
                                            self.base_model_name)

    
    def download_base_model(self):
        if not os.path.isfile(self.save_model_path):
            try:
                model = YOLO(self.base_model_name)
                shutil.move(self.base_model_name, self.save_model_path)
                logger.info(f"{self.base_model_name} download sucessfully at: {self.save_model_path} .")
            except Exception as e:
                raise e
        else:
            logger.info(f"{self.base_model_name} model already exists at {self.save_model_path} . ")

from ultralytics import YOLO
from src.YOLO_V8 import logger
from src.YOLO_V8.entity.config_entity import ModelEvaluateConfig
class EvaluateModel:
  def __init__(self, config: ModelEvaluateConfig):
    self.config = config

  def evaluate_model(self):
    try:
      model = YOLO(self.config.best_model)
      model.val(
          data = self.config.data_file,
          imgsz = self.config.image_size,
          batch = self.config.batch_size,
          conf = self.config.confidence,
          save_json = True
      )
      logger.info(f"{self.config.best_model} has validate and result are stored in runs directory.")
    except Exception as e:
      raise e

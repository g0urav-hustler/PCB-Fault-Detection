import torch
from ultralytics import YOLO
from src.YOLO_V8 import logger
from src.YOLO_V8.entity.config_entity import TrainModelConfig

class TrainModel:
  def __init__(self, config: TrainModelConfig):
    self.config = config

  def train_model(self):
    try:
      model = YOLO(self.config.base_model)
      device = 0 if torch.cuda.is_available() else "cpu"
      model.train(
          data = self.config.data_file,
          imgsz = self.config.image_size,
          epochs = self.config.epochs,
          batch = self.config.batch_size,
          project = self.config.saved_model_dir,
          device = device,
          optimizer= self.config.optimizer
      )
      logger.info(f"{self.config.base_model} has been train successefully.")
    except Exception as e:
      raise e

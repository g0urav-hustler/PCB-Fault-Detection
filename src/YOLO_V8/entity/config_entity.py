from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataProcessingConfig:
    source_dir: Path
    raw_data_dir: Path
    processed_data_dir: Path
    split_data_dir: Path
    image_size: list
    train_data_size: float
    val_data_size: float

@dataclass(frozen=True)
class BaseModelConfig:
    base_model_dir: Path
    base_model_name :str

@dataclass(frozen = True)
class TrainModelConfig:
  base_model: Path
  data_file: Path
  saved_model_dir: Path
  epochs: int
  batch_size: int
  image_size: int
  optimizer: str
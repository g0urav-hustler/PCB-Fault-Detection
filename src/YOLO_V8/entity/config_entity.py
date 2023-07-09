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
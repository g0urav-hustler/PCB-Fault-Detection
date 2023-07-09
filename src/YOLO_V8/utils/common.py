from src.YOLO_V8 import logger
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any
import yaml
import os
import json
import joblib
import shutil



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
    """
    for path in path_to_directories:
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)
            logger.info(f"created directory at: {path}")
        else:
            logger.info(f"already created directory: {path}")

@ensure_annotations
def join_path(current_path: str, add_folder: str) :
    """Add folder to exist path 
    Args: 
        current_path (Path): the current path
        add_folder (str): folder which has to added 
    Returns:
        ResultPath: path with added folder
    """
    ResultPath = os.path.join(current_path, add_folder)

    return ResultPath

@ensure_annotations
def copy_files( files_names : list, source_dir :str, target_dir: str, file_extension):
    """Copy files form source dir to target dir
    Args:
        file_names (list): list of files
        source_dir (str): source directory path
        target_dr (str): target directory path
        file_extension (str): particular extension of file
    """
    file_count = 0
    for files in files_names:
            
        if file_extension:
            files = files + file_extension

        file_source_path = join_path(source_dir, files)
        file_target_path = join_path(target_dir, files)

        if not os.path.isfile(file_target_path):
            shutil.copy(file_source_path, file_target_path)
            file_count = file_count + 1
        
    if file_count:
        logger.info(f"{file_count} Files copied from {source_dir} to {target_dir}.")
    else:
        logger.info(f"All files are already in {target_dir}.")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
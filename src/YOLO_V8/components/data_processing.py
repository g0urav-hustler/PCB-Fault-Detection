import os
import shutil
import random
import pybboxes as pbx
from src.YOLO_V8 import logger
from src.YOLO_V8.utils.common import get_size
from src.YOLO_V8.entity.config_entity import DataProcessingConfig
from src.YOLO_V8.utils.common import create_directories, copy_files, join_path


class DataProcessing:
    def __init__(self, config: DataProcessingConfig):
        self.config = config
        self.image_width = int(self.config.image_size.split(",")[0])
        self.image_height = int(self.config.image_size.split(",")[1])
        self.train_data_size = self.config.train_data_size
        self.val_data_size = self.config.val_data_size
    
    def get_raw_data(self):
        source_dir = self.config.source_dir
        target_dir = self.config.raw_data_dir

        for groups in os.listdir(source_dir):
            groups_path = os.path.join(source_dir, groups)
            
            for folder in os.listdir(groups_path):

                files_source_dir = join_path(groups_path,folder)

                files_target_dir = join_path(target_dir, folder)

                create_directories([files_target_dir])

                files = os.listdir(files_source_dir)

                logger.info(f"Start Getting Raw {folder} from {groups_path}.")
                copy_files(files, files_source_dir, files_target_dir, file_extension = None)

    def get_proper_coordinate_line(self, line):
        coordinates = line.split(" ")
        box_class = coordinates[-1].split("\n")[0]

        coordinates = list(map(int,coordinates[:-1]))

        W = self.image_width
        H = self.image_height

        converted_coordinates = pbx.convert_bbox(coordinates, from_type="voc", to_type="yolo",
                                                image_size=(W,H))
        converted_coordinates = list(map(str,converted_coordinates))

        converted_coordinates.insert(0,box_class)
        result_coordinate_line = " ".join(converted_coordinates) + "\n"
        
        return result_coordinate_line
    
    def get_processed_labels(self, labels_source_dir, labels_target_dir):

        labels_file_count = 0
        for labels_file in os.listdir(labels_source_dir):
            labels_source_file_path = join_path(labels_source_dir, labels_file)
            labels_target_file_path = join_path(labels_target_dir, labels_file)

            if not os.path.isdir(labels_target_file_path) or get_size(labels_source_file_path) != get_size(labels_target_file_path):
                label_source_file = open(labels_source_file_path, "r")
                label_target_file = open(labels_target_file_path, "w")
                save_lines = []
                for lines in label_source_file.readlines():
                    processed_line = self.get_proper_coordinate_line(lines)
                    save_lines.append(processed_line)
                
                label_target_file.writelines(save_lines)
                label_source_file.close()
                label_target_file.close()

                labels_file_count = labels_file_count + 1
        
        logger.info(f"{labels_file_count} labels files created from {labels_source_dir} to {labels_target_dir}.")

    
    def processed_data(self):
        source_dir = self.config.raw_data_dir 
        target_dir = self.config.processed_data_dir 


        for folder in os.listdir(source_dir):

            if folder == "images":
                image_source_dir = join_path(source_dir, folder)
                image_target_dir = join_path(target_dir, folder)
                
                create_directories([image_target_dir])

                image_files = os.listdir(image_source_dir)

                logger.info(f"Start Getting Processed {folder} from {image_source_dir}.")

                copy_files(image_files, image_source_dir, image_target_dir, file_extension= None)
                

            if folder == "labels":
                labels_source_dir = join_path(source_dir, folder)
                labels_target_dir = join_path(target_dir, folder)

                create_directories([labels_target_dir])

                logger.info(f"Start Getting Processed {folder} from {labels_source_dir}")
                
                self.get_processed_labels(labels_source_dir, labels_target_dir)
        
    def get_file_names(self, directory):
        file_name_list = []
        for files in os.listdir(directory):
            file_name = files.split(".")[0]
            file_name_list.append(file_name)
    
        return file_name_list
    
    
    def split_data(self):
        source_dir = self.config.processed_data_dir 
        target_dir = self.config.split_data_dir

        
        files_names = self.get_file_names(join_path(source_dir, "images"))

        random.shuffle(files_names)

        train_dir = join_path(target_dir, "train_data")
        if os.path.isdir(train_dir):
            shutil.rmtree(train_dir, ignore_errors=True)

        val_dir = join_path(target_dir, "val_data")
        if os.path.isdir(val_dir):
            shutil.rmtree(val_dir, ignore_errors=True)
        
        create_directories([train_dir, val_dir])
        
        train_size = int((len(files_names) * self.train_data_size))
        val_size = int(len(files_names) * self.val_data_size)

        logger.info(f"Traning files = {train_size} and Validation files = {val_size}")

        for folders in os.listdir(source_dir):
            
            if folders == "images":
                file_extension = ".jpg"
            if folders == "labels":
                file_extension = ".txt"
            
            files_source_dir = join_path(source_dir, folders)
            files_train_dir = join_path(train_dir, folders)
            files_val_dir = join_path(val_dir, folders)

            create_directories([files_train_dir, files_val_dir])

            logger.info(f"Splitting {folders} files into {files_train_dir} and {files_val_dir}.")

            logger.info(f"Creating training files ")
            copy_files(files_names[:train_size], files_source_dir, files_train_dir, file_extension)

            logger.info(f"Creating validation files ")
            copy_files(files_names[train_size:], files_source_dir, files_val_dir, file_extension)

